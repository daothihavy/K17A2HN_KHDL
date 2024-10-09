### Bài 6:
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def count(self):
        return len(self.items)

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.items)

# Ví dụ 
stack = Stack()
stack.push(50)
stack.push(20)
stack.push(90)
stack.print_stack() 
stack.pop()
stack.print_stack()



### Bài 7:
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0
    
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")
    

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1



### Bài 8:
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name  
        self.birth_date = birth_date 
        self.join_date = join_date  

    def display_info(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.join_date.display()
        print("-" * 30)

employees = []  # Danh sách nhân viên
n = int(input("Nhập số lượng nhân viên: "))

for i in range(n):
    print(f"\nNhân viên {i + 1}:")
    name = input("Nhập họ tên: ")

    # Nhập ngày sinh
    day = int(input("Nhập ngày sinh: "))
    month = int(input("Nhập tháng sinh: "))
    year = int(input("Nhập năm sinh: "))
    birth_date = Date(day, month, year)

    # Nhập ngày vào công ty
    day = int(input("Nhập ngày vào công ty: "))
    month = int(input("Nhập tháng vào công ty: "))
    year = int(input("Nhập năm vào công ty: "))
    join_date = Date(day, month, year)

    # Tạo nhân viên và thêm vào danh sách
    employee = Employee(name, birth_date, join_date)
    employees.append(employee)

# Hiển thị thông tin nhân viên
print("\nThông tin nhân viên:")
for emp in employees:
    emp.display_info()
