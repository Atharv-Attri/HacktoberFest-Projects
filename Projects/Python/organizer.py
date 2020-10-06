from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

import os
import shutil
import csv
import json


# Simple GUI in Tkinter
# Used to get the directory name from the user
root = Tk()

root.geometry("400x400")
root.minsize(400, 400)
root.maxsize(400, 400)

root.title("File Origanizer")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

root.geometry(f'+{positionRight}+{positionDown}')

# Top frame ---------
topFrame = Frame(root, width=400, height=50, bg="#34495e")
topFrame.pack()
Label(topFrame,text="File Organizer", bg="#34495e", fg="#ecf0f1", font=("Courier", 25)).place(x=200, y=20, anchor="center")

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# Middle Frame

middleFrame = Frame(root,width=400,height=300,bg="#c0392b")
middleFrame.pack()

# gets the directory name when browse button clicked
def browse():
    global browseFolderVar
    global filename
    filename = filedialog.askdirectory()
    browseFolderVar.set(f'Selected Folder: {filename}')


browseFolderVar = StringVar()
browseFolderVar.set("WELCOME")
browseFolderBtn = Button(middleFrame, text="BROWSE",width=10,bg="#2980b9",fg="#ecf0f1",command=browse)
browseFolderBtn.place(x=38,y=270,anchor="w")


def howTo():
    messagebox.showinfo("How To Use", " Step1: Browse the folder \n Step2: Enter the name of the folders you need to create \n Step3: Enter the file extensions you want to organize \n Step4: Click 'Organize'")

howToBtn = Button(middleFrame,text="How To", bg="#8e44ad", fg="#ecf0f1", command=howTo)
howToBtn.place(x=365,y=270,anchor="e")

nameLabel = Label(middleFrame,text="Folder Name",bg="#c0392b",fg="#ecf0f1",font=("Courier", 15))
nameLabel.place(x=100,y=50,anchor="center")

# validation for folder names entered by user
def nameValidation(inp):
    if len(inp) <=11 and not(" " in inp) and not('"' in inp) and not("'" in inp) and not('.' in inp) and not(',' in inp):
        return True
    else:
        return False


# validation for extension names entered by user
def extValidation(inp):
    if len(inp) <= 5 and not("." in inp) and not(" " in inp) and not('"' in inp) and not("'" in inp) and not("," in inp):
        return True
    else:
        return False

# detects for incorrect extensions 
def extDetection(ext):
    valid = True
    correct = 0
    for l in range(len(ext)):
        if (ext[l]>="a" and ext[l]<="z") or (ext[l]>="1" and ext[l]<="9"):
            correct +=1
    if correct == len(ext):
        valid = True
    else:
        valid = False
    
    return valid

nameReg = root.register(nameValidation)
extReg = root.register(extValidation)

# folder and extensions input fields -----------------------------------------------------------
nameOneVar = StringVar()
nameOneVar.set("")
nameOne = Entry(middleFrame,textvariable=nameOneVar)
nameOne.place(x=100,y=100,anchor="center")
nameOne.config(validate="key",validatecommand=(nameReg,"%P"))

extOneVar = StringVar()
extOneVar.set("")
extOne = Entry(middleFrame, textvariable=extOneVar)
extOne.place(x=300,y=100,anchor="center")
extOne.config(validate="key",validatecommand=(extReg,"%P"))

nameTwoVar = StringVar()
nameTwoVar.set("")
nameTwo = Entry(middleFrame,textvariable=nameTwoVar)
nameTwo.place(x=100,y=150,anchor="center")
nameTwo.config(validate="key",validatecommand=(nameReg,"%P"))


extTwoVar = StringVar()
extTwoVar.set("")
extTwo = Entry(middleFrame, textvariable=extTwoVar)
extTwo.place(x=300,y=150,anchor="center")
extTwo.config(validate="key",validatecommand=(extReg,"%P"))

nameThreeVar = StringVar()
nameThreeVar.set("")
nameThree = Entry(middleFrame,textvariable=nameThreeVar)
nameThree.place(x=100,y=200,anchor="center")
nameThree.config(validate="key",validatecommand=(nameReg,"%P"))


extThreeVar = StringVar()
extThreeVar.set("")
extThree = Entry(middleFrame, textvariable=extThreeVar)
extThree.place(x=300,y=200,anchor="center")
extThree.config(validate="key",validatecommand=(extReg,"%P"))
#  ----------------------------------------------------------------------------------------------------

extLabel = Label(middleFrame,text="Extension",bg="#c0392b",fg="#ecf0f1", font=("Courier", 15))
extLabel.place(x=300,y=50,anchor="center")


filename = "none"

# loading data to the input fields from a file
temp = []
if os.path.isfile('./data.txt'):
    with open('data.txt', "r") as myFile:
        csv_reader = csv.reader(myFile,delimiter=",")
        line_count = 0
        for line in csv_reader:
            if len(line)>0 and line_count==0:
                nameOneVar.set(line[0])
                nameTwoVar.set(line[1])
                nameThreeVar.set(line[2])

                line_count += 1
            elif len(line) > 0:
                extOneVar.set(line[0])
                extTwoVar.set(line[1])
                extThreeVar.set(line[2])
else:
    nameOneVar.set("")
    nameTwoVar.set("")
    nameThreeVar.set("")

    extOneVar.set("")
    extTwoVar.set("")
    extThreeVar.set("")

#  creating directories 
def createDir (folderName, pathName):
    path = pathName+"/"+folderName
    try:
        os.mkdir(path)
        browseFolderVar.set(f'Directory {folderName} created')
    except FileExistsError:
        browseFolderVar.set(f'Directory {folderName} already exists')


#  organizes the files 
def organize():

    name_one = nameOne.get()
    name_two = nameTwo.get()
    name_three = nameThree.get()

    ext_one = extOne.get().lower()
    ext_two = extTwo.get().lower()
    ext_three = extThree.get().lower()

    currentDir = os.getcwd()

    if not(name_one=="" or name_two=="" or name_three=="" or ext_one=="" or ext_two=="" or ext_three==""):
        if extDetection(ext_one) == True and extDetection(ext_two)==True and extDetection(ext_three) == True:
            if filename != "none":
                fNames = []
                for fName in os.listdir(filename):
                    if fName.endswith(ext_one):
                        createDir(name_one,filename)
                        shutil.move(filename+"/"+fName, filename+"/"+name_one)
                        fNames.append(fName)
                    elif fName.endswith(ext_two):
                        createDir(name_two,filename)
                        shutil.move(filename+"/"+fName, filename+"/"+name_two)
                        fNames.append(fName)
                    elif fName.endswith(ext_three):
                        createDir(name_three,filename)
                        shutil.move(filename+"/"+fName, filename+"/"+name_three)
                        fNames.append(fName)

                with open(os.path.join(currentDir, "data.txt"), "w") as myFile:
                    csv_writer = csv.writer(myFile, delimiter=",")
                    csv_writer.writerow([name_one,name_two,name_three])
                    csv_writer.writerow([ext_one,ext_two,ext_three])

                if len(fNames) == 0:
                    browseFolderVar.set("Folder Already Organized")
                else:
                    browseFolderVar.set("Folder Organized")
            else:
                browseFolderVar.set("Please Select A Folder")
        else:
            browseFolderVar.set("Please Fill Valid File Extensions")
    else:
        browseFolderVar.set("Please Fill All The Entries")



organizeBtn = Button(middleFrame,text="ORGANIZE",width=10,bg="#7f8c8d",fg="#ecf0f1", command=organize)
organizeBtn.place(x=190,y=270,anchor="center")

# -----------------------------------------------------------------------------------------------------------------------------


# Bottom Frame
bottomFrame = Frame(root,width=400,height=50,bg="#2c3e50")
bottomFrame.pack()

Label(bottomFrame,textvariable=browseFolderVar,bg="#34495e",fg="#ecf0f1",font=("Courier", 15)).place(x=200,y=20,anchor="center")


root.mainloop()




