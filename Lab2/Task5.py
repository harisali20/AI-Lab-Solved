sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}

# Keys to extract
keys = ["name", "salary"]

# New dictionary

new_Dict = {}
for key in keys:
    new_Dict[key] = sample_dict[key]
print(new_Dict)