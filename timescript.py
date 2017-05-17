import datetime

r"""
This script creates an empty file with the date and time of creation.
"""
# Variable for the current time and date
filename = datetime.datetime.now()

# Create the emptyfile
def CreateFile():
    """ This function creates the empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("") # Writing empty string()

CreateFile()
