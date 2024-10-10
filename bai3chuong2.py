from xml.dom import minidom

doc = minidom.parse('sample.xml')

company_name = doc.getElementsByTagName('name')[0].firstChild.nodeValue
print(f"Company Name: {company_name}")


staff_list = doc.getElementsByTagName('staff')

for staff in staff_list:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue
    print(f"Staff ID: {staff_id}, Name: {staff_name}, Salary: {staff_salary}")