#! python3
# selectiveCopy.py - Takes a file extension from the user and copies the files from the specified source folder to the specified destination file

from pathlib import Path
import shutil, os
import pyinputplus as pyip

#Prints a dashed-line separator for readability
def printDashLine():
    print('\n----------------------------------------------------------------------------------------------------------------\n')

#Builds a file path starting from a root folder pass by the caller
def buildFilePath(folder, srcDest):
    #Sentinel to designate when the user is done building the folder's file path
    doneWithFilePath = False
    print("Enter the first folder of the " + srcDest.lower() + " folder's file path from the options below.")
    #Build the file path
    while doneWithFilePath == False:
        folderListNumber = 1
        dirList = os.listdir(folder)
        for i in range(len(dirList)):
            if os.path.isdir(Path(folder / dirList[i])):
                print(str(folderListNumber) + ': ', end = '')
                print(dirList[i])
                folderListNumber += 1
        print('\nNext folder: ', end='')
        nextFolder = input()
        folder = folder / nextFolder
        print(srcDest + ' folder: ' + str(folder))
        print()
        print('Done with specifying ' + srcDest.lower() + ' folder?')
        answer = pyip.inputYesNo()
        print()
        if answer == 'yes':
            doneWithFilePath = True
            return(folder)
        else:
            print("Enter the next folder in the " + srcDest.lower() + " folder's file path from the options below")

#Prompt the user to enter the types of files they want to copy from the source folder to the destination folder
print("Which file type would you like to copy? Enter 'jpg', 'png', 'txt', etc.")

fileType = pyip.inputStr('File extension: ')
fileType = '.' + fileType

printDashLine()

#Get to the root directory and initialize the source and destination paths
os.chdir("../../../../..")
srcFolder = Path(os.path.abspath(os.curdir))
destFolder = Path(os.path.abspath(os.curdir))

#Prompt user to begin building the source file path
print('Source folder: ' + str(srcFolder) + '\n')
srcFolder = buildFilePath(srcFolder, 'Source')

printDashLine()

#Prompt user to begin building the destination file path
print('Destination folder: ' + str(destFolder) + '\n')
destFolder = buildFilePath(destFolder, 'Destination')

#Now copy all the files that end in the file extension from the source to the destination folder
srcFolderList = os.listdir(srcFolder)
for i in range(len(srcFolderList)):
    fileName = str(srcFolderList[i])
    if fileName.endswith(fileType):
        shutil.copy(srcFolder / srcFolderList[i], destFolder / srcFolderList[i])
