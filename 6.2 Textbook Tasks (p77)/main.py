# ----------------------------
# Title: Textbook Tasks - p77
# Date:
# ----------------------------

'''# 1.
name = input("Enter your name: ")         # prompt user to enter name

file = open("name.txt", "w")              # create a file called name
file.write(name)                          # store value of name in name.txt
file.close()

# 1.2
file = open("myName.txt" , "w")                  # create a file called name  
file.write(input("Please enter your name: "))    # store value of name in name.txt
file.close()


# 2.
file = open("password.txt", "w")         # create a file called password
file.write(input("Enter Password: "))    # prompt user to enter password, store it in password.txt 
file.close()

# 3. 
security = input("Please enter your password: ")    # prompt user to enter the password
file = open("password.txt", "r")                    # read the file password.txt
dataIn = file.read()                                # password assigned to variable 'dataIn'

if security == dataIn:                              # compare password with user entry
    print("Entry successful")
else:
    print("Access denied")
'''

# 4 - Basic no Loop Version
'''
myNums = (input("Please enter 10 numbers separated by commas: "))
file = open("myNumbers.csv", "w")
file.write(myNums)
    
file.close()'''

'''# Using a for Loop

file = open("numbers.csv", "w")  # The "w" argument indicates write
for i in range (10):
    myNums = input("Please enter a number: ")
    file.write((myNums)+",")
    
file.close()'''

# 4 - Version 2

file = open("numbers.csv", "w")   # The "w" argument indicates write

for i in range (10):
  file.write(input("Enter number: "))
  file = open("numbers.csv", "a")  # The "a" argument indicates append
  file.write(",")
file.close()


# 5.
file = open("numbers.csv", "r")

dataIn = file.read()       # assign contents of file to variable "dataIn"
print(dataIn)              # print dataIn to see contents of file
file.close()


numberList = dataIn.split(",")   # separates string into list based on specified delimiter (in this case comma " , ") 
print(numberList)

# This is very important!
numberList.remove(numberList[-1])  # removes the final space ' ' from our list.

# Using list comprehension to convert the data in our list into a float data type.
numberList = [float(item) for item in numberList]  # Uses [ ] to show it is returning a list.
print(numberList)



