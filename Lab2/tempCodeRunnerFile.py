sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}

# Keys to extract
keys = ["name", "salary"]

# New dictionary

new_Dict = {key: sample_dict[key] for key in keys}
# for i in keys:
#     if i in sample_dict:
#         new_Dict[sample_dict[i]]
print(new_Dict)