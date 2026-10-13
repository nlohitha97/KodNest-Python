import json
name = input("Enter name")
score = int(input("Enter marks"))

print(name,type(name))
print(score,type(score))

student = {
    "name":name,
    "score":score
}
print(student, type(student))

strObj = json.dumps(student)
print(strObj, type(strObj))

with open('data.json','w') as file:
    file.write(strObj)

#Json.load() --> JSON string obj to python data
python_data = json.loads(strObj)
print(python_data,python_data["name"],python_data["score"])

#Json.load() --> JSON file to python data
with open('data.json',"r") as file:
    python_data = json.load(file)
    print(python_data,type(python_data))

#json.dump()

studnet = {
    "name":"Lohitha",
    "age":21,
    "course":"Pyhton",
    "Mobile":1234567890

}

with open("studet.json",'w') as file:
    json.dump(student,file)