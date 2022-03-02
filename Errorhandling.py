# ---------------------------------- #
# Title : Exception Handling
# Description : A simple example on Exception Handling
# ChangeLog : Who, When, What
# Naga Anusha, 2/26/2022
# --------------------------------- #

try:
    file_name = input("enter the name of the file:")
    if file_name.isnumeric():
        raise ValueError()
    file = open(file_name, "r+")
    print("file_name")

except FileNotFoundError as e:
    print("Text file must exist before running this script!")
    print("built-in python error info:")
    print(e, type(e), sep='\n')
except ValueError as f:
    print("file name should be string")
    print(f, type(f), sep='\n')
