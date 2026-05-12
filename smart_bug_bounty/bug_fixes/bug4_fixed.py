import json
import os
import tempfile

def read_json_file(filepath):
    with open(filepath, "r", encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON in '{filepath}': {exc}") from exc

def process_records(filepath):
    data = read_json_file(filepath)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array, got {type(data).__name__}")
    return [record for record in data if "id" in record]

if __name__ == "__main__":
    sample = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"name": "No-ID"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(sample, tmp)
        tmp_path = tmp.name
    try:
        records = process_records(tmp_path)
        assert len(records) == 2
        print("Test 1 passed")
    finally:
        os.unlink(tmp_path)
    try:
        process_records("/nonexistent/path/data.json")
        assert False
    except FileNotFoundError:
        print("Test 2 passed")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        tmp.write("{this is not valid json}")
        bad_path = tmp.name
    try:
        process_records(bad_path)
        assert False
    except ValueError as exc:
        print(f"Test 3 passed: {exc}")
    finally:
        os.unlink(bad_path)
    print("All tests passed for bug4_fixed.py")
