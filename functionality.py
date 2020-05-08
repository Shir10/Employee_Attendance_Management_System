from classes import *
from validation import *
import csv
from datetime import datetime


def get_employees():
    emps_dict = {}
    try:
        with open("employees.csv", "r") as file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)
            for line in csv_reader:
                emps_dict[line["id"]] = Employee(line["id"], line["name"], line["age"], line["phone"])

        with open("attendance_log.csv", "r") as file:
            fieldnames = ["id", "date", "time"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)
            for line in csv_reader:
                if line["id"] in emps_dict:
                    emps_dict[line["id"]].attendance.append(Attendance(line["id"], line["date"], line["time"]))

    except FileNotFoundError:
        pass
    return emps_dict


#1
def add_emp_manually(emps_dict):
    emp_id = input("Id: ")
    valid = is_valid_id(emp_id)
    exist = is_exist_id(emps_dict, emp_id)
    while not valid or exist:
        if not valid:
            print("Invalid id! Id needs to contain only 9 digits!\n")
        else:
            print("Id already exists\n")
        emp_id = input("Id: ")
        valid = is_valid_id(emp_id)
        exist = is_exist_id(emps_dict, emp_id)
        
    name = input("Name: ")
    while not is_valid_name(name):
        print("Invalid name! Name needs to contain only letters!\n")
        name = input("Name: ")
    
    age = input("Age: ")
    while not is_valid_age(age):
        print("Invalid age! Age needs to be a number between 1 to 99!\n")
        age = input("Age: ")
        
    phone = input("Phone: ")
    while not is_valid_phone(phone):
        print("Invalid phone number! Phone number needs contains only 10 digits!\n")
        phone = input("Phone: ")

    with open("employees.csv", "a") as employees_file:
        fieldnames = ["id", "name", "age", "phone"]
        csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
        csv_writer.writerow({"id": emp_id, "name": name, "age": age, "phone": phone})

    emps_dict[emp_id] = Employee(emp_id, name, age, phone)


#2
def add_emps_from_file(emps_dict):
    file_name = input("File name: ")
    if is_valid_add_file(file_name, emps_dict):
        
        with open(file_name, "r") as other_file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(other_file, fieldnames=fieldnames)

            with open("employees.csv", "a") as employees_file:                
                csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                for line in csv_reader:
                    csv_writer.writerow(line)
                    emps_dict[line["id"]] = Employee(line["id"], line["name"], line["age"], line["phone"])


#3
def delete_emp_manually(emps_dict):
    emp_id = input("Employee id: ")
    if not is_valid_id(emp_id):
        print("Invalid id! Id needs to contain only 9 digits!\n")
        return
    if not is_exist_id(emps_dict, emp_id):
        print("None of the employees have this id!\n")
        return

    emps_dict = {i:emps_dict[i] for i in emps_dict if i != emp_id}    

    with open("employees.csv", "w") as employees_file:
        fieldnames = ["id", "name", "age", "phone"]
        csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
        for key, emp in emps_dict.items():
            csv_writer.writerow({"id": emp.emp_id, "name": emp.name, "age": emp.age, "phone": emp.phone})

    return emps_dict


#4
def delete_emps_from_file(emps_dict):
    file_name = input("File name: ")
    if is_valid_delete_file(file_name, emps_dict):
        
        with open(file_name, "r") as other_file:
            fieldnames = ["id", "name", "age", "phone"]
            csv_reader = csv.DictReader(other_file, fieldnames=fieldnames)
            for line in csv_reader:
                if line["id"] in emps_dict:
                    del emps_dict[line["id"]]

            with open("employees.csv", "w") as employees_file:
                csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                for key, emp in emps_dict.items():
                    csv_writer.writerow({"id": emp.emp_id, "name": emp.name, "age": emp.age, "phone": emp.phone})

    return emps_dict


#5
def mark_attendance(emps_dict):
    emp_id = input("Employee id: ")
    if not is_valid_id(emp_id):
        print("Invalid id! Id needs to contain only 9 digits!\n")
        return
    if not is_exist_id(emps_dict, emp_id):
        print("None of the employees have this id!\n")
        return

    emp = emps_dict[emp_id]
    now = datetime.now()
    now_date_string = now.strftime("%m/%d/%Y")
    for record in emp.attendance:
        if record.date == now_date_string:
            print("You have already registered yourself today in the attendance log!\n")
            return
        
    emp.attendance.append(Attendance(emp_id, now.date(), now.time()))

    with open("attendance_log.csv", "a") as file:
        fieldnames = ["id", "date", "time"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow({"id": emp.emp_id, "date": now.strftime("%m/%d/%Y"), "time": now.strftime("%H:%M:%S")})


#6
def generate_employee_report(emps_dict):
    emp_id = input("Employee id: ")
    if not is_valid_id(emp_id):
        print("Invalid id! Id needs to contain only 9 digits!\n")
        return
    if not is_exist_id(emps_dict, emp_id):
        print("None of the employees have this id\n")
        return

    emp = emps_dict[emp_id]

    with open(emp_id + ".csv", "w") as file:
        fieldnames = ["date", "time"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        for record in emp.attendance:
            csv_writer.writerow({"date": record.date,"time": record.time})


#7
def print_month_report():
    curr_month = datetime.now().strftime("%m")
    
    with open("attendance_log.csv", "r") as file:
        fieldnames = ["id", "date", "time"]
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        for line in csv_reader:
            date = line["date"]
            if date[0:2] == curr_month:
                print(line["id"], line["date"], line["time"])
    print()


#8
def print_late_emps_report():    
    with open("attendance_log.csv", "r") as file:
        fieldnames = ["id", "date", "time"]
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        for line in csv_reader:
            if line["time"] > "09:30:00":
                print(line["id"], line["date"], line["time"])
    print()


