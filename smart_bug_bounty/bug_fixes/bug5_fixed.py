def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"

def parse_config(config_str):
    config = {}
    lines = config_str.split('\n')
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()
    return config

def connect_database(host, port, password):
    connection_string = f"host={host};port={port};password={password}"
    print(f"Connecting to: host={host};port={port}")
    return connection_string

def validate_user(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return query, (username, password)

result = read_file('nonexistent.txt')
print(result)
config = parse_config('host=localhost\nbroken_line\nport=5432')
print(config)
