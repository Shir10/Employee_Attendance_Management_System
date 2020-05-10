from Employee import Employee
from Attendance import Attendance
from Common import get_employees
from Validation import *
import csv
from datetime import datetime
from tkinter import *


class Manager:
    def __init__(self):
        self.emps_dict = get_employees()

    # 1
    def add_emp_manually(self):
        # Create new window
        top = Toplevel()
        top.title("Add Employee")

        # Create labels
        id_label = Label(top, text="Id: ")
        id_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        name_label = Label(top, text="Name: ")
        name_label.grid(row=1, column=0, padx=5, pady=10, sticky="E")

        age_label = Label(top, text="Age: ")
        age_label.grid(row=2, column=0, padx=5, pady=10, sticky="E")

        phone_label = Label(top, text="Phone: ")
        phone_label.grid(row=3, column=0, padx=5, pady=10, sticky="E")

        # Create entries
        id_entry = Entry(top, width=30)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        name_entry = Entry(top, width=30)
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        age_entry = Entry(top, width=30)
        age_entry.grid(row=2, column=1, padx=10, pady=10)

        phone_entry = Entry(top, width=30)
        phone_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create invalid message labels
        invalid_id_label = Label(top, text="Invalid id! Id needs to contain only 9 digits!", fg="red")
        invalid_name_label = Label(top, text="Invalid name! Name needs to contain only letters!", fg="red")
        invalid_age_label = Label(top, text="Invalid age! Age needs to be a number between 1 to 99!", fg="red")
        invalid_phone_label = Label(top, text="Invalid phone number! Phone number needs contains only 10 digits!", fg="red")

        def submit(emp_id, name, age, phone, emps_dict):
            valid = True
            if not is_valid_id(emp_id) or is_exist_id(emps_dict, emp_id):
                invalid_id_label.grid(row=0, column=2, sticky="W")
                valid = False
            else:
                invalid_id_label.grid_remove()

            if not is_valid_name(name):
                invalid_name_label.grid(row=1, column=2, sticky="W")
                valid = False
            else:
                invalid_name_label.grid_remove()

            if not is_valid_age(age):
                invalid_age_label.grid(row=2, column=2, sticky="W")
                valid = False
            else:
                invalid_age_label.grid_remove()

            if not is_valid_phone(phone):
                invalid_phone_label.grid(row=3, column=2, sticky="W")
                valid = False
            else:
                invalid_phone_label.grid_remove()

            if valid:
                with open("employees.csv", "a") as employees_file:
                    fieldnames = ["id", "name", "age", "phone"]
                    csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                    csv_writer.writerow({"id": emp_id, "name": name, "age": age, "phone": phone})

                emps_dict[emp_id] = Employee(emp_id, name, age, phone)
                top.destroy()

        # Create button
        btn = Button(top, text="Submit",
                     command=lambda: submit(id_entry.get(), name_entry.get(), age_entry.get(), phone_entry.get(), self.emps_dict))
        btn.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    # 2
    def add_emps_from_file(self):
        # Create new window
        top = Toplevel()
        top.title("Add Employee From File")

        # Create label
        file_name_label = Label(top, text="File Name: ")
        file_name_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        # Create entry
        file_name_entry = Entry(top, width=30)
        file_name_entry.grid(row=0, column=1, padx=10, pady=10)

        def submit(file_name, emps_dict):
            if is_valid_add_file(file_name, emps_dict, top):

                with open(file_name, "r") as other_file:
                    fieldnames = ["id", "name", "age", "phone"]
                    csv_reader = csv.DictReader(other_file, fieldnames=fieldnames)

                    with open("employees.csv", "a") as employees_file:
                        csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                        for line in csv_reader:
                            csv_writer.writerow(line)
                            emps_dict[line["id"]] = Employee(line["id"], line["name"], line["age"], line["phone"])

                top.destroy()

        # Create button
        btn = Button(top, text="Submit", command=lambda: submit(file_name_entry.get(), self.emps_dict))
        btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    # 3
    def delete_emp_manually(self):
        # Create new window
        top = Toplevel()
        top.title("Delete Employee Manually")

        # Create label
        emp_id_label = Label(top, text="Employee ID: ")
        emp_id_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        # Create entry
        emp_id_entry = Entry(top, width=30)
        emp_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create invalid message labels
        invalid_id_label_1 = Label(top, text="Invalid id! Id needs to contain only 9 digits!", fg="red")
        invalid_id_label_2 = Label(top, text="None of the employees have this id!", fg="red")

        def submit(emp_id, emps_dict):
            if not is_valid_id(emp_id):
                invalid_id_label_1.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_1.grid_remove()

            if not is_exist_id(emps_dict, emp_id):
                invalid_id_label_2.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_2.grid_remove()

            del emps_dict[emp_id]

            with open("employees.csv", "w") as employees_file:
                fieldnames = ["id", "name", "age", "phone"]
                csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                for key, emp in emps_dict.items():
                    csv_writer.writerow({"id": emp.emp_id, "name": emp.name, "age": emp.age, "phone": emp.phone})

            top.destroy()

        # Create button
        btn = Button(top, text="Submit", command=lambda: submit(emp_id_entry.get(), self.emps_dict))
        btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    # 4
    def delete_emps_from_file(self):
        # Create new window
        top = Toplevel()
        top.title("Delete Employees From File")

        # Create label
        file_name_label = Label(top, text="File name: ")
        file_name_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        # Create entry
        file_name_entry = Entry(top, width=30)
        file_name_entry.grid(row=0, column=1, padx=10, pady=10)

        def submit(file_name, emps_dict):
            if is_valid_delete_file(file_name, emps_dict, top):

                with open(file_name, "r") as other_file:
                    fieldnames = ["id", "name", "age", "phone"]
                    csv_reader = csv.DictReader(other_file, fieldnames=fieldnames)
                    for line in csv_reader:
                        if line["id"] in emps_dict:
                            del emps_dict[line["id"]]

                    with open("employees.csv", "w") as employees_file:
                        csv_writer = csv.DictWriter(employees_file, fieldnames=fieldnames)
                        for key, emp in emps_dict.items():
                            csv_writer.writerow(
                                {"id": emp.emp_id, "name": emp.name, "age": emp.age, "phone": emp.phone})

                top.destroy()

        # Create button
        btn = Button(top, text="Submit", command=lambda: submit(file_name_entry.get(), self.emps_dict))
        btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    # 5
    def mark_attendance(self):
        # Create new window
        top = Toplevel()
        top.title("Mark Attendance")

        # Create label
        emp_id_label = Label(top, text="Id: ")
        emp_id_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        # Create entry
        emp_id_entry = Entry(top, width=30)
        emp_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create invalid message labels
        invalid_id_label_1 = Label(top, text="Invalid id! Id needs to contain only 9 digits!", fg="red")
        invalid_id_label_2 = Label(top, text="None of the employees have this id!", fg="red")
        dup_attendance_label = Label(top, text="You have already registered yourself today in the attendance log!", fg="red")

        def submit(emp_id, emps_dict):
            if not is_valid_id(emp_id):
                invalid_id_label_1.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_1.grid_remove()

            if not is_exist_id(emps_dict, emp_id):
                invalid_id_label_2.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_2.grid_remove()

            emp = emps_dict[emp_id]
            now = datetime.now()
            now_date_string = now.strftime("%d/%m/%Y")
            now_time_string = now.strftime("%H:%M:%S")
            for record in emp.attendance:
                if record.date == now_date_string:
                    dup_attendance_label.grid(row=0, column=2, sticky="W")
                    return
            dup_attendance_label.grid_remove()

            emp.attendance.append(Attendance(emp_id, now_date_string, now.time()))

            with open("attendance_log.csv", "a") as file:
                fieldnames = ["id", "date", "time"]
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writerow({"id": emp.emp_id, "date": now_date_string, "time": now_time_string})

            top.destroy()

        # Create button
        btn = Button(top, text="Submit", command=lambda: submit(emp_id_entry.get(), self.emps_dict))
        btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    # 6
    def generate_employee_report(self):
        # Create new window
        top = Toplevel()
        top.title("Generate Employee Report")

        # Create label
        emp_id_label = Label(top, text="Id: ")
        emp_id_label.grid(row=0, column=0, padx=5, pady=10, sticky="E")

        # Create entry
        emp_id_entry = Entry(top, width=30)
        emp_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create invalid message labels
        invalid_id_label_1 = Label(top, text="Invalid id! Id needs to contain only 9 digits!", fg="red")
        invalid_id_label_2 = Label(top, text="None of the employees have this id!", fg="red")

        def submit(emp_id, emps_dict):
            if not is_valid_id(emp_id):
                invalid_id_label_1.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_1.grid_remove()

            if not is_exist_id(emps_dict, emp_id):
                invalid_id_label_2.grid(row=0, column=2, sticky="W")
                return
            else:
                invalid_id_label_2.grid_remove()

            emp = emps_dict[emp_id]

            with open(emp_id + ".csv", "w") as file:
                fieldnames = ["date", "time"]
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                for record in emp.attendance:
                    csv_writer.writerow({"date": record.date, "time": record.time})
            top.destroy()

        # Create button
        btn = Button(top, text="Submit", command=lambda: submit(emp_id_entry.get(), self.emps_dict))
        btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
