from json import dumps, loads

# serializing a dictionary to JSON
""" users = [
    {"user": "juan", "active": True, "quota": None},
    {"user": "ana", "active": False, "quota": 300},
]
str_json = dumps(users) # operación contraria al loads, de dict a JSON
print(type(str_json), str_json)
print(dumps(users, indent=2)) 
 """
# deserializing a JSON string to a dictionary  
stringJson = '{"name": "John", "age": null, "active": true}'
pythonDict = loads(stringJson) # convierte la string JSON en un diccionario de Python
print(stringJson)
print(pythonDict)

