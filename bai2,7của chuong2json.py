import json

# JSON data
json_data = '''
{
    "name": "Nguyen Van A",
    "age": 30,
    "city": "Hanoi",
    "skills": ["Python", "JavaScript", "Machine Learning"]
}
'''

# Chuyển đổi JSON thành đối tượng Python
python_object = json.loads(json_data)

# In ra đối tượng Python
print(python_object)
print(type(python_object))  # Kiểm tra kiểu dữ liệu

