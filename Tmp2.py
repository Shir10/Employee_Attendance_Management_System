import csv
from tkinter import *


def is_valid_option(option):
    if option.isdigit() and (int(option) in range(1, 10)):
        return True
    return False


def is_valid_id(emp_id):
    if emp_id.isdigit() and len(emp_id) == 9:
        return True
    return False


def is_valid_name(name):
    if len(name) > 0 and name.isalpha():
        return True
    return False


def is_valid_age(age):
    if age.isdigit() and (int(age) in range(1, 100)):
        return True
    return False


def is_valid_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    return False


def is_exist_id(emps_dict, emp_id):
    if emp_id in emps_dict:
        return True
    return False


def is_valid_add_file(file_name, emps_dict, top):
    # Create invalid message labels
    invalid_fields_label = Label(top, text="The file contains invalid fields!", fg="red")
    invalid_dup_label = Label(top, text="Error! One of the IDs is already exist!", fg="red")
    invalid_file_name_label = Label(top, text="No such file!", fg="red")

    try:
        with open(file_name, "r") as file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)

            for line in csv_reader:
                if not (len(line) == 4 and is_valid_id(line["id"]) and is_valid_name(line["name"]) and is_valid_age(line["age"]) and is_valid_phone(line["phone"])):
                    invalid_fields_label.grid(row=0, column=2, sticky="W")
                    return False
                else:
                    invalid_fields_label.grid_remove()

                if line["id"] in emps_dict:
                    invalid_dup_label.grid(row=0, column=2, sticky="W")
                    return False
                else:
                    invalid_dup_label.grid_remove()
        return True

    except FileNotFoundError:
        invalid_file_name_label.grid(row=0, column=2, sticky="W")
        return False


def is_valid_delete_file(file_name, emps_dict, top):
    # Create invalid message labels
    invalid_fields_label = Label(top, text="The file contains invalid fields!", fg="red")
    missing_data_label = Label(top, text="Not all the data of all the employees to delete is supplied!", fg="red")
    not_exist_label = Label(top, text="Some of the employees to delete do not exist in the system!", fg="red")
    invalid_file_name_label = Label(top, text="No such file!", fg="red")

    try:
        with open(file_name, "r") as file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)

            for line in csv_reader:
                if not (len(line) == 4 and is_valid_id(line["id"]) and is_valid_name(line["name"]) and is_valid_age(line["age"]) and is_valid_phone(line["phone"])):
                    invalid_fields_label.grid(row=0, column=2, sticky="W")
                    return False

                found = False
                correct_data = False
                for key, emp in emps_dict.items():
                    if emp.emp_id == line["id"]:
                        found = True
                        if emp.name == line["name"] and emp.age == line["age"] and emp.phone == line["phone"]:
                            correct_data = True
                            break

                if found and not correct_data:
                    missing_data_label.grid(row=0, column=2, sticky="W")
                    return False

                if not found:
                    not_exist_label.grid(row=0, column=2, sticky="W")
                    return False
        return True

    except FileNotFoundError:
        invalid_file_name_label.grid(row=0, column=2, sticky="W")
        return False
