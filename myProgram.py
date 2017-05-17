def age_foo(age):
    new_age = float(age) + 25
    return new_age # age here is a local variable

# Prompt user for the input
age = input("Enter your age: ") # Global variable
print(age_foo(age))
