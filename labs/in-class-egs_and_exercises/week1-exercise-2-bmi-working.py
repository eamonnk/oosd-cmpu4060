# Exercise 2: BMI calculator
# Write a Python script that calculates the body-mass index. 

# --Solution --
# Prompt user to enter their name and assign that value to "name" object. It will be a string object
name = input("Please enter your name: ")
print(type(name))
# print(name)
# Prompt  user to enter their weight and assign that value to "weight" object. Define the input value as an integer
weight = int(input("Please enter your weight (Kgs): "))
print(type(weight))
print(weight)
# Prompt user to enter their height and assign that value to "height" object. Define the input value as an integer
height = int(input("Please enter your height (cm): "))
print (height)
print(type(height))

# Calculate Body Mass Index(BMI), the weight in kilograms divided by the square of the height in meters,
# we divide by 100 to convert cm to metres
# the resultant value is a float, so we round that to two decimal places using the round function to give us a more user friendly value 
# We assign that value to the variable "bmi"
bmi = str(round(weight/((height/100)**2), 2))
print(bmi)
print(type(bmi))

# printing
print(name.upper() + ":" + "Your Body Mass Index (bmi) is" + " " + str(bmi))
