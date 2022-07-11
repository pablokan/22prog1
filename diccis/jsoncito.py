# stringJson = '{"nombre":"Juan", "salario":null, "empleado":false}'
# 1) Es obligatoria la doble comilla
# 2) El valor nulo se llama null (en lugar de None)
# 3) El valor booleano se llama true o false en vez de True or False

# serializing a Python object to JSON
# lista de diccionarios
from json import dumps, loads

users = [
    {"user": "juan", "active": True, "quota": None},
    {"user": "ana", "active": False, "quota": 300},
]
strJson = dumps(users)
print(strJson)


# deserializing a JSON string to a Python dictionary
stringJson = '{"nombre":"Juan", "salario":null, "empleado":false}'
pythonDict = loads(stringJson)
print(stringJson)
print(pythonDict)
