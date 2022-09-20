import json
# from unicodedata import name
person = {"name":"Josh",
"age":"15",
"mail":"joshmail",
"hobbies":[
    'reading',
    'sport',
    'videogames'
]}
# convert the dictionary into a JSON filesort_keys sort the keys alphabetically (DECODE)
personJSON = json.dumps(person, indent=4,sort_keys=True)
print(personJSON)

# create a new json document with our element
with open ('person.json','w') as file:
    json.dump(person,file, indent = 4)

# convert to a json to a dictionary (ENCODE)
# person = json.loads(personJSON)

# classes in python
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User("Mark",8)
