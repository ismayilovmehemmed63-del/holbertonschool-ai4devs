import os

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except IOError as e:
        print(f'Error reading file: {e}')
        return None

def parse_config(config_str):
    config = {}
    lines = config_str.split('
')
    for line in lines:
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        config[key.strip()] = value.strip()
    return config

def connect_database(host, port):
    password = os.environ.get('DB_PASSWORD', '')
    connection_string = f"host={host};port={port};password={password}"
    print(f"Connecting to: host={host};port={port}")
    return connection_string

result = read_file('nonexistent.txt')
print(result)

config = parse_config('host=localhost
port=5432
invalid_line
user=admin')
print(config)

assert read_file('nonexistent.txt') is None
assert parse_config('key=value') == {'key': 'value'}
assert parse_config('invalid') == {}
print('All tests passed!')
