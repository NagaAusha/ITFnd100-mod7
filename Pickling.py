# -------------------------------------- #
# Title :example for Python Pickling
# Change Log : who, when, what
# Naga Anusha, 2/26/2022
# -------------------------------------- #
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


data_list = []  # A list


def add_data():
    task = str(input("enter task:"))
    priority = str(input("enter priority:"))
    row = {"task": task, "priority": priority}
    print(row)
    data_list.append(row)


def store_data():
    objfile = open("file_name", "wb")
    pickle.dump(data_list, objfile)    # Storing the data with pickle.dump method
    objfile.close()


def load_data():
    obj_file = open("file_name", "rb")
    objfiledata = pickle.load(obj_file)    # Loads the data
    obj_file.close()
    print(objfiledata)


while True:
    menu_task()
    user_input = str(input("enter option:"))

    if user_input == '1':  # Add a data
        add_data()
        continue  # to show the menu

    elif user_input == '2':  # storing the data
        store_data()
        print("Data stored")
        continue

    elif user_input == '3':  # load Data from File
        load_data()
        print("Data loaded!")
        continue  # to show the menu

    elif user_input == '4':  # Exit Program
        print("Goodbye!")
        break  # exiting loop
