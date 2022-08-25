import json

def main():
    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    name = jsonObject[0]['Name']
    Contact = jsonObject[0]['Contact']
    Email = jsonObject[0]['Email']
    Hobbies = jsonObject[0]['Hobbies']

 







































main()