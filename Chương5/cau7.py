

def toi_uu_chuoi(ho_ten):
    # 1. Xóa khoảng trắng đầu và cuối
    ho_ten = ho_ten.strip()

    # 2. Tách các từ theo khoảng trắng
    tu = ho_ten.split()

    # 3. Viết hoa chữ cái đầu mỗi từ, các chữ còn lại viết thường
    tu = [t.capitalize() for t in tu]

    # 4. Ghép lại bằng 1 khoảng trắng
    ho_ten_chuan = " ".join(tu)

    return ho_ten_chuan


# ------------------------------
# Chương trình chính
# ------------------------------
def main():
    s = input("Nhập chuỗi họ tên cần tối ưu: ")
    ket_qua = toi_uu_chuoi(s)
    print("✅ Chuỗi tối ưu là:", ket_qua)


# Gọi hàm
if __name__ == "__main__":
    main()
