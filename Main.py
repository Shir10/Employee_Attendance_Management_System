from Manager import *
from Common import *
from tkinter import *
from tkinter import messagebox


def launch(option, manager):
    if option == 1:
        manager.add_emp_manually()

    elif option == 2:
        manager.add_emps_from_file()

    elif option == 3:
        manager.delete_emp_manually()

    elif option == 4:
        manager.delete_emps_from_file()

    elif option == 5:
        manager.mark_attendance()

    elif option == 6:
        manager.generate_employee_report()

    elif option == 7:
        print_month_report()

    elif option == 8:
        print_late_emps_report()

    else:
        messagebox.showerror("Error!", "Invalid option!")


def main():
    manager = Manager()

    root = Tk()
    root.title("Employee Attendance Management System")
    root.geometry("500x330")

    title = Label(root, text="Choose an option:")
    title.pack()

    options = [
        "1. Add employee manually",
        "2. Add employees from file",
        "3. Delete employee manually",
        "4. Delete employees from file",
        "5. Mark attendance",
        "6. Generate attendance report of an employee",
        "7. Print a report for current month for all employees",
        "8. Print an attendance report for all employees who were late (came after 9:30am)",
    ]

    r = IntVar()
    r.set(0)

    i = 1
    for option in options:
        Radiobutton(root, text=option, variable=r, value=i, padx=10, pady=5).pack(anchor=W)
        i += 1

    btn = Button(root, text="Launch", padx=20, pady=5, command=lambda: launch(r.get(), manager))
    btn.pack()

    root.mainloop()


if __name__ == "__main__":
    main()





