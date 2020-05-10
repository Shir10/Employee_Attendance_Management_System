import csv


def is_valid_option(option):
    if (option.isdigit() and (int(option) in range(1, 10))):
        return True
    return False


def is_valid_id(emp_id):
    if (emp_id.isdigit() and len(emp_id) == 9):
        return True
    return False


def is_valid_name(name):
    if (len(name) > 0 and name.isalpha()):
        return True
    return False


def is_valid_age(age):
    if (age.isdigit() and (int(age) in range(1, 100))):
        return True
    return False


def is_valid_phone(phone):
    if (phone.isdigit() and len(phone) == 10):
        return True
    return False


def is_exist_id(emps_dict, emp_id):
    if (emp_id in emps_dict):
        return True
    return False


def is_valid_add_file(file_name, emps_dict):
    try:
        with open(file_name, "r") as file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)
            for line in csv_reader:
                if (not (len(line) == 4 and is_valid_id(line["id"]) and is_valid_name(line["name"]) and is_valid_age(
                        line["age"]) and is_valid_phone(line["phone"]))):
                    print("Invalid file!\n")
                    return False

                if (line["id"] in emps_dict):
                    print("Error! One of the IDs is already exist!\n")
                    return False
        return True
    except FileNotFoundError:
        print("No such file!\n")
        return False


def is_valid_delete_file(file_name, emps_dict):
    try:
        with open(file_name, "r") as file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)
            for line in csv_reader:
                if (not (len(line) == 4 and is_valid_id(line["id"]) and is_valid_name(line["name"]) and is_valid_age(
                        line["age"]) and is_valid_phone(line["phone"]))):
                    print("Invalid file!\n")
                    return False
                found = False
                for key, emp in emps_dict.items():
                    if (emp.emp_id == line["id"] and emp.name == line["name"] and emp.age == line["age"] and emp.phone == line["phone"]):
                        found = True
                        break
                if (not found):
                    print("Not all the data of the employees to delete is supplied!")
                    return False
        return True
    except FileNotFoundError:
        print("No such file!\n")
        return False
