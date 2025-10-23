import xml.dom.minidom

# ===============================
# Hàm đọc nhóm thiết bị
# ===============================
def DocNhomThietBi(path):
    try:
        DOMTree = xml.dom.minidom.parse(path)
        collection = DOMTree.documentElement
        nhoms = collection.getElementsByTagName("nhom")

        print("📁 DANH SÁCH NHÓM THIẾT BỊ:")
        ds_nhom = {}
        for nhom in nhoms:
            ma = nhom.getElementsByTagName('ma')[0].childNodes[0].data
            ten = nhom.getElementsByTagName('ten')[0].childNodes[0].data
            ds_nhom[ma] = ten
            print(f"  {ma} - {ten}")
        return ds_nhom

    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {path}")
        return {}

# ===============================
# Hàm đọc danh sách thiết bị
# ===============================
def DocThietBi(path, ds_nhom):
    try:
        DOMTree = xml.dom.minidom.parse(path)
        collection = DOMTree.documentElement
        thietbis = collection.getElementsByTagName("thietbi")

        print("\n💡 DANH SÁCH THIẾT BỊ:")
        for tb in thietbis:
            manhom = tb.getAttribute("manhom")
            ma = tb.getElementsByTagName('ma')[0].childNodes[0].data
            ten = tb.getElementsByTagName('ten')[0].childNodes[0].data
            ten_nhom = ds_nhom.get(manhom, "Không xác định")
            print(f"  {ma} - {ten} (Thuộc nhóm: {ten_nhom})")

    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {path}")

# ===============================
# Chương trình chính
# ===============================
def main():
    print("=== CHƯƠNG TRÌNH QUẢN LÝ THIẾT BỊ (XML) ===")

    ds_nhom = DocNhomThietBi("nhomthietbi.xml")
    if ds_nhom:
        DocThietBi("thietbi.xml", ds_nhom)

if __name__ == "__main__":
    main()
