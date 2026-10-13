import json

data = input()
py_data = json.loads(data)
print(py_data["name"])
print(sum(py_data["scores"]))
    
