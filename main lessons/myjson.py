import json

# Python dict
data = {"name": "jadi", "sen": 47, "fun": "bicycle", "coolness": 6}
print(data)
print(type(data))

# Convert dict to JSON string
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# Correct JSON string
d = '{"name": "jadi", "sen": 47, "fun": "bicycle", "coolness": 6}'

# Convert JSON string to Python dict
new_data = json.loads(d)
print(new_data)
print(new_data['sen'])
print(type(new_data))

