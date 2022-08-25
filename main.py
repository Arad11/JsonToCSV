import json
import csv

def main():
    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        keys = getJsonKeysAsList(jsonObject)
        objects = getJsonAsList(jsonObject)
        jsonFile.close()
        
    name = keys[0]
    contact = keys[1]
    email = keys[2]
    hobbies = keys[3]

 
def getJsonKeysAsList(jsonObject):
    return list(jsonObject[0].keys())

def getJsonAsList(jsonObject):
    objects = []
    for object in jsonObject:
        objects.append(object)
    return objects




































main()