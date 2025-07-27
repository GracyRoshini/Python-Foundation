
import json

dict={"empid":1, "emp_name":"anish", "salary":20000}

#Serialization json: converting python obj to json
json_obj=json.dumps(dict)

with open("sample.json", 'w') as fp:
    fp.write(json_obj)

