import os

folderToSearch = str(input("Selecione uma pasta: "))
foldersList = []
removeUseless = ["$RECYCLE.BIN","System Volume Information"]

def listDirectories(path):
    global foldersToTest
    foldersToTest = []
    folderToSearch = path
    actualFolder = os.scandir(path)
    
    for entry in actualFolder:
        if entry.is_dir():
            foldersToTest.append(entry.name)
    
    for val in removeUseless:
        if val in foldersToTest:
            foldersToTest.remove(val)
    foldersList.clear()
    
    for folder in foldersToTest:
        foldersList.append(folder)
    foldersList = foldersToTest

listDirectories(path=folderToSearch)
print(foldersList)
print(foldersToTest)