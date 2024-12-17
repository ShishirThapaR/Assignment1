"""
write a python script that print your name , course name , and the python version you are using
"""
# importing the sys module
import sys
# This line assigns the string value "Pulkit Pandey" to the variable my_name
my_name = "Arpita Panigrahi" 
# This line assigns the string value "python programming" to the variable course_name
course_name = "python programming"
#nting Name:,Course:   using the f-string
print(f"Name: {my_name}")
print(f"Course: {course_name}")
# printing the sys.version tell about the current version of python you are using
print(sys.version)


""""
write  a python program with briefly explained comments that takes a users first and 
last name as input and prints them in reverse order with a space between them.
"""
# Take the user's first name as input
first_name = input("Enter your first name: ")

# Take the user's last name as input
last_name = input("Enter your last name: ")

# Print the last name first, then the first name with a space in between
print(last_name + " " + first_name)


# This line assigns the string value "How are you." to the variable input_string
input_string = "Python is easy language to code in ."

# 1. String Method: upper(). It Converts all characters in the string to uppercase.
uppercase_string = input_string.upper()

# 2. String Method: replace(). It allows us to replace a specific substring with a different one.
modified_string = input_string.replace(".", "?")

# Print the results using the f-string method
print("Original string:", input_string)
print("Uppercase string:", uppercase_string)
print("Modified string:", modified_string)

"""
write a python program that takes an input number from the user, converts it to diffent numeric data types (integer, float, nad complex), 
and displays the converted values.
"""
# Takes an input number from the user using variable input_num
input_num = input("Enter the number here: ")

try:
    # Convert the input to an integer by typecasting using int method.
    # An integer is a whole number without a fractional part.
    # Examples: -3, 0, 42, 1001
    
    int_num = int(input_num)
    
    # Convert the input to a float by typecasting using float method.
    # A floating-point number (or float) represents a real number with a decimal point.
    # Examples: 3.14, -0.001, 2.71828
    
    float_num = float(input_num)
    
    # Convert the input to a complex number by typecasting using complex method.
    # A complex number consists of a real part and an imaginary part.
    # Written in the form a + bj, where a is the real part and b is the imaginary part.
    # Example: 3 + 2j (where 3 is the real part and 2j represents the imaginary part).
    
    complex_num = complex(input_num)
    
    # Display the converted values using the f-string method
    print(f"Integer value: {int_num}")
    print(f"Float value: {float_num}")
    print(f"Complex value: {complex_num}")
    
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")

"""
create a python script that calculates the sum the area of a rectangle . 
the script should ask user to enter the length and width of the rectangle .
Calculate the area.
Display the result using print function.
"""

# takes the lenght as input from user
length = float(input("Enter the length of the rectangle: "))
# takes the width as input from user
width = float(input("Enter the width of the rectangle: "))

# Calculate the area (length * width)
area = length * width

# Display the result using the f-string method
print(f"The area of the rectangle is: {area}")

"""
modify the rectangle area program to format the output so that it display the area with two decimal places.
"""

# takes the lenght as input from user
length = float(input("Enter the length of the rectangle: "))
# takes the width as input from user
width = float(input("Enter the width of the rectangle: "))

# Calculate the area (length * width)
area = length * width

# Display the area of rectangle upto two decimal places 
print(f"The area of the rectangle is: {area:.2f}")
"""
write a python script that takes three jumbers as input and prints their average using the % method for string  formating.
Also, use the print functions to display a message that states , "the average of the three numbers is: [calculated average]".
"""
#Taking three numbers as input from the user
num1 = input("Enter the first number here: ")
num2 = input("Enter the second number here: ")
num3 = input("Enter the third number here: ")

try:
    #convering input to float
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    
    # Calculating the average
    average = (num1 + num2 + num3) / 3

    # Printing the average using % formatting
    print("The average of the three numbers is: %.2f" % average)

except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
"""
write a pythin program that asks the user for a number and determines whether it is positive , negative or zero. 
Implement a loop that continues to ask the user for a number until they enter 'exit'  
Use break to exit the loop and continue to prompt for a new number if the input is not 'exit'.
"""

# Initializing a loop
while True:
    # takes the user input
    input_num = input("Enter a number here (or 'exit' to quit): ")

    # Check if the user wants to exit
    if input_num.lower() == 'exit':
        print("Exiting the program.")
        
        break

    try:
        # Convert input_num to a floating-point number
        number = float(input_num)
        
        # finding the number is positive, negative, or zero
        if number > 0:
            print("Positive number")
        elif number < 0:
            print("Negative number")
        else:
            print("Zero")
    except ValueError:
        # Handle invalid input (non-numeric or empty input)
        print("Invalid input. Please enter a valid number or 'exit'.")

"""
create a python script that takes two numbers as input and prints whether both numbers are even, 
odd or one of each using relational and logical operators.
"""

# Takes two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if both numbers are even, both are odd, or one of each
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")

