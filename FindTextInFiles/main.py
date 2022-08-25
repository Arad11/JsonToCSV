import os
from os.path import isfile, join

#directoryPath = sys[1]
directoryPath = "D:\\"
stringToComperWith = "arad"
filesWithSameString = []

def main():
    filesInDir = getTxtFilesFromDir(directoryPath)
    
    filesWithSameString = getTxtFilesFromDir(directoryPath,"arad")
            
    arad = "arad"
    print(f"{arad}\\\\a")

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
            if text.__contains__(sen):
                newFiles.append(file)
            newFile.close()


    return files

main()