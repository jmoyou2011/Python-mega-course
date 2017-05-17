# Create a Celsius to Fahrenheit degree coversion fucntion
def C_F(celsius):
    #RapidTables is the source of the equation.
    Fahrenheit = (float(celsius) * (9/5)) + 32.0
    return Fahrenheit

# Create a Fahrenheit to Celsius conversion function.
def F_C(Fahrenheit):
    #RapidTables is the source of the equation
    Celsius = (float(Fahrenheit) - 32.0 ) * (5/9)
    return Celsius
