import json
name = input("Enter a name")
score = int(input("Enter marks"))

student = {
    "name":name,
    "score":score
}

print(json.dumps(student))