# Main script
from CeltoFah import C_F, F_C

# Prompt a user input
temperature_C = input("Enter a Celsius temperature for conversion: ")
temperature_F = input("Enter a Fahrenheit temperature for conversion: ")

# Conditional in temperature_C is less than -273.15^o C
if float(temperature_C) < -273.15 or float(temperature_F) < -459.67:
    print("This is not physically possible and you have destroyed the universe. Goodbye")
    quit()
else:
    print(C_F(temperature_C))
    print(F_C(temperature_F))
