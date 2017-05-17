"""
This script tries to accomplish task 5.
"""

from CeltoFah import C_F # Imported conversion function for the exercise.

# Initialize the temperatures list
temperatures = [10, -20, -289, 100]

# Create a text file.
exercise4 = open("exercise5.txt",'w')
exercise4.close()

# For loop to go through each element and perform conversion.
for i in temperatures:
    if i < -273.15:
        print("This temperature is not possible")
    else:
        Fahrenheit = C_F(i)
        files = open("exercise5.txt",'r+')
        files.seek(0)
        content = files.read()
        files.write(str(Fahrenheit)+"\n")
