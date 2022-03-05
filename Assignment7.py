# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <Naga Anusha.Perali>,<2.26.2022>,Created Script
# ------------------------------------------------- #
# This imports code from another code file!


import pickle


def menu_task():
    print('''
    menu of options
    1) enter task and priority
    2) store data to file
    3) load data 
    4)exit
    ''')
    print()


data_list = []


def add_data():
    task = str(input("enter task:"))
    priority = str(input("enter priority:"))
    row = {"task": task, "priority": priority}
    print(row)
    data_list.append(row)


def store_data():
    objfile = open("file_name", "ab")
    pickle.dump(data_list, objfile)      # Stores the data with pickle.dump
    objfile.close()


def load_data():
    obj_file = open("file_name", "rb")
    objfiledata = pickle.load(obj_file)  # loads the data with pickle.load method
    obj_file.close()
    print(objfiledata)


while True:
    menu_task()

    try:
        user_input = input("enter option:")
        if not user_input.isnumeric():
            raise ValueError()

        print(user_input)
        if int(user_input) == 1:  # Add a data
            add_data()
            continue  # to show the menu

        elif int(user_input) == 2:  # storing the data
            store_data()
            print("Data stored")
            continue

        elif int(user_input) == 3:  # load Data from File
            load_data()
            print("Data loaded!")
            continue  # to show the menu

        elif int(user_input) == 4:  # Exit Program
            print("Goodbye!")
            break  # exiting loop
    except ValueError as ex:
        print("user_input should be integer 1-4")
        print(ex, type(ex), sep='\n')
