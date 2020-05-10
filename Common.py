from Employee import Employee
from Attendance import Attendance
from tkinter import *
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


# 7
def print_month_report():
    # Create new window
    top = Toplevel()
    top.title("Month Report")

    try:
        with open("attendance_log.csv", "r") as file:
            fieldnames = ["id", "date", "time"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)

            # Create label
            id_label = Label(top, text="Id")
            id_label.grid(row=0, column=0, padx=5, pady=10, sticky="W")

            date_label = Label(top, text="Date")
            date_label.grid(row=0, column=1, padx=5, pady=10, sticky="W")

            time_label = Label(top, text="Time")
            time_label.grid(row=0, column=2, padx=5, pady=10, sticky="W")

            curr_month = datetime.now().strftime("%m")

            row_num = 1
            for line in csv_reader:
                date = line["date"]
                if date[3:5] == curr_month:
                    Label(top, text=line["id"]).grid(row=row_num, column=0, padx=5, pady=10, sticky="W")
                    Label(top, text=line["date"]).grid(row=row_num, column=1, padx=5, pady=10, sticky="W")
                    Label(top, text=line["time"]).grid(row=row_num, column=2, padx=5, pady=10, sticky="W")
                row_num += 1

    except FileNotFoundError:
        # Create invalid message label
        empty_file_label = Label(top, text="Attendance log file is empty!", fg="red")
        empty_file_label.pack(padx=10, pady=10)


# 8
def print_late_emps_report():
    # Create new window
    top = Toplevel()
    top.title("Employees Who Were Late Report")

    try:
        with open("attendance_log.csv", "r") as file:
            fieldnames = ["id", "date", "time"]
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)

            # Create label
            id_label = Label(top, text="Id")
            id_label.grid(row=0, column=0, padx=5, pady=10, sticky="W")

            date_label = Label(top, text="Date")
            date_label.grid(row=0, column=1, padx=5, pady=10, sticky="W")

            time_label = Label(top, text="Time")
            time_label.grid(row=0, column=2, padx=5, pady=10, sticky="W")

            row_num = 1
            for line in csv_reader:
                if line["time"] > "09:30:00":
                    Label(top, text=line["id"]).grid(row=row_num, column=0, padx=5, pady=10, sticky="W")
                    Label(top, text=line["date"]).grid(row=row_num, column=1, padx=5, pady=10, sticky="W")
                    Label(top, text=line["time"]).grid(row=row_num, column=2, padx=5, pady=10, sticky="W")
                row_num += 1

    except FileNotFoundError:
        # Create invalid message label
        empty_file_label = Label(top, text="Attendance log file is empty!", fg="red")
        empty_file_label.pack(padx=10, pady=10)

