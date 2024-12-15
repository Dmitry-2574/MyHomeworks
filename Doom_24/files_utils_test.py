
from files_utils import *

# JSON
data_json = {"name": "John Doe", "age": 30, "city": "New York"}
write_json(data_json, "test.json")
read_data_json = read_json("test.json")
print(f"JSON read: {read_data_json}")

append_json([{"name": "Jane Doe", "age": 25, "city": "London"}], "test.json")
read_data_json_append = read_json("test.json")
print(f"JSON appended: {read_data_json_append}")

