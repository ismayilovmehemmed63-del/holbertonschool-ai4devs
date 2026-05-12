def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    return content

def parse_config(config_str):
    config = {}
    lines = config_str.split('
')
    for line in lines:
        key, value = line.split('=')
        config[key] = value
    return config

def connect_database(host, port, password):
    connection_string = f"host={host};port={port};password=admin123"
    print(f"Connecting to: {connection_string}")
    return connection_string

def validate_user(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    return query

result = read_file('nonexistent.txt')
print(result)
config = parse_config('host=localhost
broken_line
port=5432')
print(config)
