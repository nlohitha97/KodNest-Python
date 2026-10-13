import json

json_text = input()
python_data = json.loads(json_text)
print(python_data["name"])
print(python_data["price"])
