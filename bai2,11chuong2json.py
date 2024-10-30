import json

# Đọc dữ liệu JSON từ file
with open("company_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Lấy thông tin công ty và các đơn vị
company_info = data["company"]
company_name = company_info["name"]
company_address = company_info["address"]
departments = company_info["departments"]

# Tính tổng số nhân viên
total_employees = sum(len(dept["employees"]) for dept in departments)

# In thông tin công ty
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {company_address}")
print(f"Tổng số nhân viên: {total_employees}\n")

# Thống kê nhân viên theo từng đơn vị và in kết quả
print("- Thống kê nhân viên theo đơn vị\n")
for idx, dept in enumerate(departments, start=1):
    department_name = dept["name"]
    employee_count = len(dept["employees"])
    employee_percentage = (employee_count / total_employees) * 100
    print(f"{idx}. Tên đơn vị: {department_name}")
    print(f"- Số nhân viên: {employee_count}")
    print(f"- Tỷ lệ: {employee_percentage:.2f} %\n")
