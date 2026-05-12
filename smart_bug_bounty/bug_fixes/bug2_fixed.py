import sqlite3

def get_connection():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'alice', 'hash_alice', 'admin')")
    conn.execute("INSERT OR IGNORE INTO users VALUES (2, 'bob', 'hash_bob', 'user')")
    conn.commit()
    return conn

def get_user_by_username(conn, username):
    cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def authenticate(conn, username, password):
    cursor = conn.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None

if __name__ == "__main__":
    conn = get_connection()
    user = get_user_by_username(conn, "alice")
    assert user is not None and user[1] == "alice"
    print("Test 1 passed")
    user = get_user_by_username(conn, "' OR '1'='1")
    assert user is None
    print("Test 2 passed")
    auth = authenticate(conn, "' OR 1=1 --", "anything")
    assert not auth
    print("Test 3 passed")
    conn.close()
    print("All tests passed for bug2_fixed.py")
