import csv
import random

# ========== HÀM 1: GHI FILE CSV ==========

def TaoFileCSV(path):
    """Tạo file CSV gồm 10 dòng, mỗi dòng 10 số ngẫu nhiên"""
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            dong = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(dong)
    print(f"✅ Đã tạo file {path} với dữ liệu ngẫu nhiên.")


# ========== HÀM 2: ĐỌC FILE CSV & TÍNH TỔNG ==========

def DocVaTinhTong(path):
    """Đọc file CSV và in tổng các phần tử trên mỗi dòng"""
    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        print("Tổng giá trị mỗi dòng:")
        dong_thu = 1
        for row in reader:
            # Chuyển từng phần tử từ chuỗi sang số nguyên
            tong = sum(int(x) for x in row if x.strip() != '')
            print(f"Dòng {dong_thu}: {tong}")
            dong_thu += 1


# ========== CHƯƠNG TRÌNH CHÍNH ==========

def main():
    path = "data.csv"
    print("""
========= XỬ LÝ CSV FILE =========
1. Tạo file CSV (10 dòng, 10 số ngẫu nhiên)
2. Đọc file và tính tổng từng dòng
3. Thoát
==================================
""")
    while True:
        chon = input("Chọn chức năng (1-3): ")
        if chon == '1':
            TaoFileCSV(path)
        elif chon == '2':
            DocVaTinhTong(path)
        elif chon == '3':
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
