# ==============================
# Câu 8: Tách lấy tên bài hát từ đường dẫn
# ==============================

import os  # thư viện xử lý đường dẫn

def lay_ten_file(duong_dan):
    """
    Hàm lấy ra tên file (bao gồm phần mở rộng)
    Ví dụ: d:\\music\\muabui.mp3 -> muabui.mp3
    """
    return os.path.basename(duong_dan)


def lay_ten_bai_hat(duong_dan):
    """
    Hàm lấy ra tên bài hát (không gồm phần mở rộng)
    Ví dụ: d:\\music\\muabui.mp3 -> muabui
    """
    ten_file = os.path.basename(duong_dan)
    ten_bai_hat, _ = os.path.splitext(ten_file)
    return ten_bai_hat


# ------------------------------
# Chương trình chính
# ------------------------------
def main():
    duong_dan = input("Nhập đường dẫn bài hát: ")

    ten_file = lay_ten_file(duong_dan)
    ten_bai_hat = lay_ten_bai_hat(duong_dan)

    print("✅ Tên file:", ten_file)
    print("✅ Tên bài hát:", ten_bai_hat)


# Gọi hàm
if __name__ == "__main__":
    main()

