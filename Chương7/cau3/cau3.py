from xml.dom.minidom import parse
import xml.dom.minidom
import os

# Tên file XML
path = "employees.xml"

# Kiểm tra file có tồn tại không
if not os.path.exists(path):
    print("❌ Không tìm thấy file employees.xml — hãy chắc chắn file nằm cùng thư mục với chương trình.")
    exit()

# Đọc file XML
DOMTree = xml.dom.minidom.parse(path)
collection = DOMTree.documentElement

# Lấy tất cả thẻ <employee>
employees = collection.getElementsByTagName("employee")

print("Danh sách nhân viên:")
for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    id = tag_id.childNodes[0].data.strip()

    tag_name = employee.getElementsByTagName('name')[0]
    name = tag_name.childNodes[0].data.strip()

    print(id, '\t', name)
