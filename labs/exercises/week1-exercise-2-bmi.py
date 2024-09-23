# Exercise 2: BMI calculator
# Write a Python script that calculates the body-mass index. 

# --Solution --
# Prompt user to enter their name and assign that value to "name" variable. It will be a string object by default
name = input("Please enter your name: ")

# Prompt user to enter their weight and assign that value to "weight" variable. Define the input value as an integer
weight = int(input("Please enter your weight (Kgs): "))

# Prompt user to enter their height and assign that value to "height" variable. Define the input value as an integer
height = int(input("Please enter your height (cm): "))


# Calculate Body Mass Index(BMI), the weight in kilograms divided by the square of the height in meters,
# we divide by 100 to convert cm to metres
# Resultant value is a float. We round that to two decimal places using the round function for more user friendly value. 
# Assign that value to the variable "bmi"
bmi = str(round(weight/((height/100)**2), 2))

# printing name variable and calculated bmi value with template string converting the name variable to upper case
print("Thank You" +  " " + name.upper() + ":" + "Your Body Mass Index (bmi) is" + " " + str(bmi))
