# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Sliang,11.15.2022,Homework 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # text file to read
objFile = ""  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    row = row.rstrip('\n')  # remove \n in txt file
    strData = row.split(",")  # Returns a list!
    dicRow = {"Task":strData[0],"Priority":strData[1]}
    lstTable.append(dicRow)
print(lstTable)
# print(lstTable, "<<list with dictionary objects")
# test file
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(row["Task"],":",row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        # TODO: Add Code Here
        strTask = input("Add Task: ")
        strPriority = input("Priority for this Task: ")
        lstTable.append({"Task":strTask,"Priority":strPriority})
        # append a new dictionary to the list
        #print(lstTable)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strTask = input("Task to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("Task: ",strTask, " has been removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        objFile.close()
        # overwrite the old file and start a new file
        objFile = open(strFile, "a")
        for row in lstTable:
            x = str(row["Task"]) + ',' + str(row["Priority"]) + '\n'
            objFile.write(x)
        objFile.close()
        print(" Data has been saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print(" Data was not saved!")
        break  # and Exit the program
