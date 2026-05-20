info = {
    "name": "shrutika",
    "cgpa": 9.67,
    "subjects": ["maths", "science"],
    3.14: "pie"
}

# keys() - returns all keys
dict_keys = (info.keys())
print(dict_keys)
#  print(info.keys()) we can also write it like this

# values() - returns all values
dict_vals = (info.values())
print(dict_vals)
#  print(info.values()) 

# iteams() - return (key,val) pair
print(info.items())

# get(val) - returns val acc to key
print(info.get("cgpa"))
# we can also write it like print(info["cgpa"])
# but if we give wrong value then error may occur and program can stop so we use get method instead
# get give output as none and contineoue the program

# update(new_iteam) - adds/insert new iteam to dict 
info.update({
    "city": "Nagpur"
})
print(info)