

import json

#De-serilization: converting json to python obj

with open("sample.json",'r') as fp:
    python_obj=json.load(fp)

print(python_obj)
