# Fill in this file with the code from parsing JSON exercise
import json
import yaml
with open('myfile.json','r') as json_file:
     ourjson = json.load (json_file)
print (ourjson)
print ("\n\n---")
print (yaml.dump(ourjson))
