import json

with open("Data.json","r")as file:
    data = json.load(file)

print("Name: ", data["name"])
print("Age: ", data["age"])
print("course: ", data["course"])
print("Skills: ", data["Skills"])
