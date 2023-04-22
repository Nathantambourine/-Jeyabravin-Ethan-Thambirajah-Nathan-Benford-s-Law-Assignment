import os
print(os.getcwd())
def printMenu():
    print('''
          Customer and Sales System\n   
          1. Load sales data\n
          2. Create Chart\n
          Enter menu option (1-2)  
          ''') # Gives the user two options one to load the sale data and two to create the chart 
    
# Variables 

userInput = ""
saledata = "1"
createchart = "2"


if userInput == saledata:        
    folder = os.getcwd()
    fileName = folder + "\\sales.csv" # Prints the csv file
    file = open(fileName, "r")
    print(file.read())
    file.close()
    
    salesData = []                          #Creates empty list for sales data
with open("sales.csv" , 'r') as file:       #Opens csv file in read mode under the variable file                
    lines = file.readlines()[1:] # read lines and store under lines variable. '[1: ]' skips first row
for line in lines:                          
    salesData.append(int(line.strip().split(',')[1]))         #splits the second column, turns number in to integers, and stores under 'salesData' list      

digit_counts = [0] * 9                                          #Generates 9 number list all starting at 0
for num in sales_data:
    first_digit = int(str(num)[0])                              #Convert first digit of every number into integer using '(str(num0[0])'
digit_counts[first_digit-1] += 1

digit_percentages = []                                          #Empty list for percentages of digit occurences 
for count in digit_counts:
    percentage = count/len(sales_data)*100                      #divide count by total sales and mulitiply by 100
digit_percentages.append(percentage)

fraud_threshold = (29, 32)                                              #Sets range where fraud does not occur using tuple containing min and max integer          
if fraud_threshold[0] <= digit_percentages[0] <= fraud_threshold[1]:
    print("The data indicates that fraud likely did not occur.")
else:
    print("The data indicates that fraud may have occurred.")  


# chart

    if userInput == createchart: 

        import matplotlib as plt

        plt.xlabel("Number")
        plt.ylabel("Percent")
        plt.show()

        folder = os.getcwd()
        fileName = folder + "\\results.csv"         #Creates a new csv file when inputed 
        file = open(fileName, "w")
        print(file.read())
        file.close()

    else:
        print("Please type in a valid option (A number from 1-2)")





