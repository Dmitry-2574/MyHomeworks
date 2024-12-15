
from files_utils import *

# JSON
data_json = {"name": "John Doe", "age": 30, "city": "New York"}
write_json(data_json, "test.json")
read_data_json = read_json("test.json")
print(f"JSON read: {read_data_json}")

append_json([{"name": "Jane Doe", "age": 25, "city": "London"}], "test.json")
read_data_json_append = read_json("test.json")
print(f"JSON appended: {read_data_json_append}")

# CSV
data_csv = [["Name", "Age", "City"], ["John Doe", "30", "New York"]]
write_csv(data_csv, "test.csv")
read_data_csv = read_csv("test.csv")
print(f"CSV read: {read_data_csv}")

append_csv([["Jane Doe", "25", "London"]], "test.csv")
read_data_csv_append = read_csv("test.csv")
print(f"CSV appended: {read_data_csv_append}")

