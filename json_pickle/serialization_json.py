import json #Major drawback over pickles, can not use custom data types from python

#For example if this dictionary is changed to type tuple we can not serialize it with JSON
friends1 = {"Dan": (20, "London", 3234342), "Maria": (25, "Madrid", 25252525)}
#friends1 = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 25252525]}

with open('friends.json', 'w') as f:
    json.dump(friends1, f, indent=4)

json_string = json.dumps(friends1, indent=4)
print(json_string)

with open('friends.json') as file:
    print(type(file))
    obj = json.load(file)
    print(type(obj))

#json multiline string (multiline is """ text """) and loads
jsonString = """{
    "Dan": [
        20,
        "London",
        3234342
    ],
    "Maria": [
        25,
        "Madrid",
        25252525
    ]
} """

object1 = json.loads(jsonString)
print(object1)

#Python data types become in  JSON 
# dict []                 object
#list, tuples ()          array
#set {}                   set can not be serialized    --- convert first to list
#str                      string
#int,float                number
#True                     true
#False                    false
#None                     null