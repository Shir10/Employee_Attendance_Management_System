from classes import *
from functionality import *
import csv
from datetime import datetime


def main():
    emps_dict = get_employees()
    
    while True:
        option = input("""Choose an option:
1. Add employee manually
2. Add employees from file
3. Delete employee manually
4. Delete employees from file
5. Mark attendance
6. Generate attendance report of an employee
7. Print a report for current month for all employees
8. Print an attendance report for all employees who were late (came after 9:30am)
9. Leave
""")
        if not is_valid_option(option):
            print("Invalid option!\n")
            continue
        else:
            option = int(option)

        if option == 1:
            add_emp_manually(emps_dict)
            
        elif option == 2:
            add_emps_from_file(emps_dict)
            
        elif option == 3:
            emps_dict = delete_emp_manually(emps_dict)
            
        elif option == 4:
            emps_dict = delete_emps_from_file(emps_dict)
            
        elif option == 5:
            mark_attendance(emps_dict)
            
        elif option == 6:
            generate_employee_report(emps_dict)
            
        elif option == 7:
            print_month_report()
        
        elif option == 8:
            print_late_emps_report()

        else:
            break


if __name__ == "__main__":
    main()




                
