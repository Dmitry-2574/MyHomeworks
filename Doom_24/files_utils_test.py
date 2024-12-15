
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

# TXT
data_txt = "Hello, world!"
write_txt(data_txt, "test.txt")
read_data_txt = read_txt("test.txt")
print(f"TXT read: {read_data_txt}")

append_txt("\nThis is an appended line.", "test.txt")
read_data_txt_append = read_txt("test.txt")
print(f"TXT appended: {read_data_txt_append}")

# YAML
data_yaml = {"name": "John Doe", "age": 30, "city": "New York"}
with open('test.yaml', 'w') as file:
    yaml.dump(data_yaml, file)

read_data_yaml = read_yaml("test.yaml")
print(f"YAML read: {read_data_yaml}")