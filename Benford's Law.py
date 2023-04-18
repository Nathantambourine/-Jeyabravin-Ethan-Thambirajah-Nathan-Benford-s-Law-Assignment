import os
print(os.getcwd())
def printMenu():
    print('''
          Customer and Sales System\n
          1. Load sales data\n
          2. Create Chart\n
          3. Exit 
          Enter menu option (1-3)
          ''')
    
userInput = ""
saledata = "1"
createchart = "2"
exitCondition = "3"


while userInput != exitCondition:
    printMenu()               
    userInput = input();   

    if userInput == saledata:        
        folder = os.getcwd()
        fileName = folder + "\\sales.csv"
        file = open(fileName, "r")
        print(file.read())
        file.close()

    elif userInput == createchart: 
        
        createchart()

    else:
        print("Please type in a valid option (A number from 1-3)")


print("Program Terminated")
