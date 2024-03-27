# import requests
# import json

# response = requests.get("http://api.open-notify.org/astros.json")  # specially  it is http don't have s in it 
# print(response.status_code)
# print(response.json())


import json

# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

# convert a Python object to JSON:
x = {"name":"John", "age":30, "city":"New York"}

# convert x to JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)