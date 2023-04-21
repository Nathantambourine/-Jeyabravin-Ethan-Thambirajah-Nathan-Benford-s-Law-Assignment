import os
print(os.getcwd())
def printMenu():
    print('''
          Customer and Sales System\n
          1. Load sales data\n
          2. Create Chart\n
          Enter menu option (1-2)
          ''')

# Put your code on line 13 

userInput = ""
saledata = "1"
createchart = "2"
exitCondition = "3"

salesData = []
with open(fileName, 'r') as file:
    lines = file.readlines()[1:] # skip header row
for line in lines:
    salesData.append(int(line.strip().split(',')[1]))

digit_counts = [0] * 9
for num in sales_data:
    first_digit = int(str(num)[0])
digit_counts[first_digit-1] += 1

digit_percentages = []
for count in digit_counts:
    percentage = count/len(sales_data)*100
digit_percentages.append(percentage)

fraud_threshold = (29, 32)
if fraud_threshold[0] <= digit_percentages[0] <= fraud_threshold[1]:
    print("The data indicates that fraud likely did not occur.")
else:
    print("The data indicates that fraud may have occurred.")  


while userInput != exitCondition:
    printMenu()               
    userInput = input();   

    if userInput == saledata:        
        folder = os.getcwd()
        fileName = folder + "\\sales.csv"
        file = open(fileName, "r")
        print(file.read())
        file.close()

    if userInput == createchart: 
        
        folder = os.getcwd()
        fileName = folder + "\\results.csv"
        file = open(fileName, "w")
        print(file.read())
        file.close()
        

    else:
        print("Please type in a valid option (A number from 1-3)")


print("Program Terminated")


