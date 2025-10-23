import json
import os

# ================== HÀM XỬ LÝ FILE ==================

def DocFile(path):
    """Đọc dữ liệu từ file JSON"""
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def LuuFile(path, data):
    """Ghi dữ liệu ra file JSON"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ================== XỬ LÝ NGHIỆP VỤ ==================

def XuatDanhSach(dsLop):
    print("\n========== DANH SÁCH SINH VIÊN ==========")
    for lop in dsLop:
        print(f"\n📘 Lớp: {lop['MaLop']} - {lop['TenLop']}")
        print("{:<10}{:<20}{:<10}".format("Mã SV", "Tên SV", "Năm Sinh"))
        for sv in lop['DanhSachSV']:
            print("{:<10}{:<20}{:<10}".format(sv['MaSV'], sv['TenSV'], sv['NamSinh']))
    print("=========================================\n")


def ThemSinhVien(dsLop):
    maLop = input("Nhập mã lớp: ")
    tenLop = input("Nhập tên lớp: ")

    # Kiểm tra lớp đã có chưa
    lop = next((l for l in dsLop if l['MaLop'] == maLop), None)
    if lop is None:
        lop = {"MaLop": maLop, "TenLop": tenLop, "DanhSachSV": []}
        dsLop.append(lop)

    maSV = input("Nhập mã sinh viên: ")
    tenSV = input("Nhập tên sinh viên: ")
    namSinh = int(input("Nhập năm sinh: "))

    sv = {"MaSV": maSV, "TenSV": tenSV, "NamSinh": namSinh}
    lop['DanhSachSV'].append(sv)
    print("✅ Đã thêm sinh viên vào lớp!")


def SuaSinhVien(dsLop):
    maSV = input("Nhập mã sinh viên cần sửa: ")
    for lop in dsLop:
        for sv in lop['DanhSachSV']:
            if sv['MaSV'] == maSV:
                print(f"Tìm thấy sinh viên {sv['TenSV']} trong lớp {lop['MaLop']}")
                sv['TenSV'] = input("Tên mới: ")
                sv['NamSinh'] = int(input("Năm sinh mới: "))
                print("✅ Đã cập nhật thông tin!")
                return
    print("❌ Không tìm thấy sinh viên.")


def XoaSinhVien(dsLop):
    maSV = input("Nhập mã sinh viên cần xóa: ")
    for lop in dsLop:
        for sv in lop['DanhSachSV']:
            if sv['MaSV'] == maSV:
                lop['DanhSachSV'].remove(sv)
                print(f"✅ Đã xóa sinh viên {sv['TenSV']} trong lớp {lop['MaLop']}")
                return
    print("❌ Không tìm thấy sinh viên.")


def TimKiem(dsLop):
    keyword = input("Nhập tên sinh viên cần tìm: ").lower()
    found = False
    for lop in dsLop:
        for sv in lop['DanhSachSV']:
            if keyword in sv['TenSV'].lower():
                print(f"🔍 {sv['MaSV']} - {sv['TenSV']} ({sv['NamSinh']}) trong lớp {lop['MaLop']}")
                found = True
    if not found:
        print("❌ Không tìm thấy sinh viên nào.")


def SapXep(dsLop):
    for lop in dsLop:
        lop['DanhSachSV'].sort(key=lambda x: x['TenSV'])
    print("✅ Đã sắp xếp danh sách sinh viên theo tên trong từng lớp!")

# ================== MENU CHÍNH ==================

def main():
    path = "sinhvien.json"
    dsLop = DocFile(path)

    while True:
        print("""
========== QUẢN LÝ SINH VIÊN ==========
1. Xem danh sách
2. Thêm sinh viên
3. Sửa sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Sắp xếp sinh viên theo tên
7. Lưu dữ liệu
8. Thoát
=======================================
""")
        chon = input("Chọn chức năng (1-8): ")

        if chon == '1':
            XuatDanhSach(dsLop)
        elif chon == '2':
            ThemSinhVien(dsLop)
        elif chon == '3':
            SuaSinhVien(dsLop)
        elif chon == '4':
            XoaSinhVien(dsLop)
        elif chon == '5':
            TimKiem(dsLop)
        elif chon == '6':
            SapXep(dsLop)
        elif chon == '7':
            LuuFile(path, dsLop)
            print("💾 Dữ liệu đã được lưu vào sinhvien.json")
        elif chon == '8':
            print("👋 Thoát chương trình!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
