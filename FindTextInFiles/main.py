import os
import sys
from os.path import isfile, join

directoryPath = sys[1]
stringToComperWith = sys[2]
filesWithSameString = []

def main():    
    filesWithSameString = getTxtFilesFromDir(directoryPath)
    files = getTxtFilesWithChoosenString(filesWithSameString , stringToComperWith)
    for file in files:
        print(f"{directoryPath}\{file}")

def getTxtFilesFromDir(dirPath):
    files = []
    for file in os.listdir(directoryPath):
        if file.endswith(".txt"):
            files.append(file)

    return files

def getTxtFilesWithChoosenString(files, sen):
    newFiles = []
    for file in files:
        with open(directoryPath + "\\" + file) as newFile:
            text = newFile.read()
            if sen in text:
                newFiles.append(file)
            newFile.close()

    return newFiles

main()