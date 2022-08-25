import json
import csv
import sys

jsonFilePath = sys[1] #example: D:\\projects\\JsonToCSV\\test.json
csvFilePath = sys[2] #example: D:\\projects\\JsonToCSV\\copyToFile.csv

def main():
    with open(jsonFilePath) as jsonFile:
        jsonObject = json.load(jsonFile)
        keys = getJsonKeysAsList(jsonObject)
        objects = getJsonAsList(jsonObject)
        jsonFile.close()
        
    with open(csvFilePath, 'w', encoding="UTF8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(objects)
    
def getJsonKeysAsList(jsonObject):
    return list(jsonObject[0].keys())

def getJsonAsList(jsonObject):
    objects = []
    for object in jsonObject:
        objects.append(object)
    return objects



main()