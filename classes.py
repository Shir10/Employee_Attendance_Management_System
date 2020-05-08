
class Employee:
    def __init__(self, emp_id, name, age, phone):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.phone = phone
        self.attendance = []

class Attendance:
    def __init__(self, emp_id, date, time):
        self.emp_id = emp_id
        self.date = date
        self.time = time
