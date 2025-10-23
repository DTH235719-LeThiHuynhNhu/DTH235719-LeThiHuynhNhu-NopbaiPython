from xml.dom.minidom import parse
import xml.dom.minidom

# Mở và phân tích file XML
try:
    DOMTree = xml.dom.minidom.parse("employees.xml")
except FileNotFoundError:
    print("❌ Không tìm thấy file employees.xml — hãy chắc chắn file nằm cùng thư mục với chương trình.")
    exit()

# Lấy phần tử gốc
collection = DOMTree.documentElement

# Lấy tất cả các tag <employee>
employees = collection.getElementsByTagName("employee")

# Duyệt vòng lặp để lấy dữ liệu
print("Danh sách nhân viên:")
for employee in employees:
    # Kiểm tra tồn tại thẻ <id> và <name>
    tag_id = employee.getElementsByTagName('id')
    tag_name = employee.getElementsByTagName('name')

    if tag_id and tag_id[0].childNodes:
        id = tag_id[0].childNodes[0].data.strip()
    else:
        id = "Không có ID"

    if tag_name and tag_name[0].childNodes:
        name = tag_name[0].childNodes[0].data.strip()
    else:
        name = "Không có tên"

    print(id, '\t', name)
