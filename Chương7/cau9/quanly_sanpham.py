import os

# ============ HÀM XỬ LÝ FILE ============

def LuuFile(path, data):
    """Ghi 1 dòng dữ liệu vào file"""
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data + "\n")


def GhiDeFile(path, list_data):
    """Ghi đè toàn bộ danh sách vào file"""
    with open(path, 'w', encoding='utf-8') as f:
        for line in list_data:
            f.write(line + "\n")


def DocFile(path):
    """Đọc dữ liệu từ file -> trả về list sản phẩm"""
    ds = []
    if not os.path.exists(path):
        return ds
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            data = line.strip()
            if data != "":
                arr = data.split(';')
                ds.append(arr)
    return ds

# ============ HÀM XỬ LÝ NGHIỆP VỤ ============

def XuatDanhSach(ds):
    print("\n{:<6}{:<15}{:<10}{:<15}{:<10}".format("MaDM", "TenDM", "MaSP", "TenSP", "DonGia"))
    print("-"*60)
    for sp in ds:
        print("{:<6}{:<15}{:<10}{:<15}{:<10}".format(sp[0], sp[1], sp[2], sp[3], sp[4]))


def ThemSanPham(ds):
    maDM = input("Nhập mã danh mục: ")
    tenDM = input("Nhập tên danh mục: ")
    maSP = input("Nhập mã sản phẩm: ")
    tenSP = input("Nhập tên sản phẩm: ")
    donGia = input("Nhập đơn giá: ")
    sp = [maDM, tenDM, maSP, tenSP, donGia]
    ds.append(sp)
    print("✅ Đã thêm sản phẩm mới!")


def SuaSanPham(ds):
    maSP = input("Nhập mã sản phẩm cần sửa: ")
    for sp in ds:
        if sp[2] == maSP:
            print("Tìm thấy:", sp)
            sp[3] = input("Tên mới: ")
            sp[4] = input("Đơn giá mới: ")
            print("✅ Đã cập nhật!")
            return
    print("❌ Không tìm thấy sản phẩm.")


def XoaSanPham(ds):
    maSP = input("Nhập mã sản phẩm cần xóa: ")
    for sp in ds:
        if sp[2] == maSP:
            ds.remove(sp)
            print("✅ Đã xóa sản phẩm!")
            return
    print("❌ Không tìm thấy sản phẩm.")


def TimKiem(ds):
    keyword = input("Nhập tên sản phẩm cần tìm: ").lower()
    kq = [sp for sp in ds if keyword in sp[3].lower()]
    if kq:
        XuatDanhSach(kq)
    else:
        print("❌ Không tìm thấy sản phẩm nào!")


def SapXep(ds):
    ds.sort(key=lambda x: x[3])  # sắp xếp theo tên sản phẩm
    print("✅ Đã sắp xếp theo tên sản phẩm.")

# ============ CHƯƠNG TRÌNH CHÍNH ============

def main():
    path = "sanpham.txt"
    dsSanPham = DocFile(path)

    while True:
        print("""
========== QUẢN LÝ SẢN PHẨM ==========
1. Xem danh sách
2. Thêm sản phẩm
3. Sửa sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Sắp xếp sản phẩm theo tên
7. Lưu file
8. Thoát
======================================
""")
        chon = input("Chọn chức năng (1-8): ")

        if chon == '1':
            XuatDanhSach(dsSanPham)
        elif chon == '2':
            ThemSanPham(dsSanPham)
        elif chon == '3':
            SuaSanPham(dsSanPham)
        elif chon == '4':
            XoaSanPham(dsSanPham)
        elif chon == '5':
            TimKiem(dsSanPham)
        elif chon == '6':
            SapXep(dsSanPham)
        elif chon == '7':
            # Ghi lại toàn bộ danh sách vào file
            data_lines = [';'.join(sp) for sp in dsSanPham]
            GhiDeFile(path, data_lines)
            print("💾 Đã lưu dữ liệu vào file sanpham.txt")
        elif chon == '8':
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
