# JSON (JavaScript Object Notation) is a lightweight, text-based format used for storing and exchanging data in key-value pairs.

import json

# json.loads() - if we wanna comvert json to py
json_str = '{"name": "Jeon Jungkook", "isTeacher": true}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)



#   json.dumps - (if we wanna comvert py to json
py_obj = {
    "name": "Jeon Jungkook",
    "isTeacher": True
}

json_str = json.dumps(py_obj)

print(type(json_str), json_str)



#  json.load() - if we wanna read a file
with  open("PythonFundamentals5/JSON_file/data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)



#  json.dump() - if we wanna write a file.new data file me overwrite karega
data = {
   "name" : "Kim Teahyung",
   "age" : 30,
   "isTeacher" : True
   }
with  open("PythonFundamentals5/JSON_file/data.json", "w") as f:
  json.dump(data, f, indent=4, sort_keys=True)#indent - adds space at the begining, sort_keys= accending order(alphabetical here) 
  print(py_obj)