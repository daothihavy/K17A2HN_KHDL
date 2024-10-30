import json

# Đối tượng Python (dictionary)
python_object = {
    "name": "Nguyen Van A",
    "age": 30,
    "city": "Hanoi",
    "skills": ["Python", "JavaScript", "Machine Learning"]
}

# Chuyển đổi đối tượng Python sang chuỗi JSON
json_data = json.dumps(python_object, indent=4)

# In ra chuỗi JSON
print("Chuỗi JSON:")
print(json_data)

# In ra tất cả các giá trị
print("\nCác giá trị:")
for key, value in python_object.items():
    print(f"{key}: {value}")
