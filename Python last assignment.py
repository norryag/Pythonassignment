import os
import pathlib


def main():
    os.system('cls')

    def GetState():
        state=input("What is the name of the state?  ")
        
        return state;

    def FormatState(state):
        if len(state) < 8:
            newState = state.ljust(8, '*')
            return newState
        else:
            return state;
 
    print("1. Get information and display to screen")
    print("2. Call user created functions")
    print("3. Write List of files to file")
    print("4. Read specified file")

    task = input("Enter number of task to do:")
    
    if task == "1":
        companyName="Dunwoody College"
        programName="Computer Networking"
        uName=os.environ['UserName']
        classFirst=input("Provide the name of your first class:")
        classSecond=input("Provide the name of your second class:")

        print("Logged on as " + uName + " at " + companyName + " in department:" + programName)
        print("My first class is " + classFirst + " and my second class is " + classSecond)

    elif task == "2":
        state=GetState()
        newState=FormatState(state)
        print("State was " + state + " and now it is " + newState)
        
    elif task == "3":
        fileOfFiles = input("Name of file to hold the files  ")
        fList = []
        for p in pathlib.Path('.').iterdir():
            if p.is_file():
                fList.append(p)
        with open(fileOfFiles, "w") as myFileWrite:
            myFileWrite.write("These are my files:\n")
            for f in fList:
                myFileWrite.write(f.name)
                myFileWrite.write("\n")        

    elif task == "4":
        fileToRead = input("Name of file to read:  ")


        with open(fileToRead, "r+") as myFileRead:
            print(myFileRead.read())
   

main()
    



