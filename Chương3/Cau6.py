print("Chương trình đọc số có tối đa 2 chữ số")

# Nhập số n
n = int(input("Nhập số n (0–99): "))

if n < 0 or n > 99:
    print("Số không hợp lệ! Vui lòng nhập số có tối đa 2 chữ số.")
else:
    # Tạo danh sách đọc số
    so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        # Trường hợp 1 chữ số
        print(so[n].capitalize())
    else:
        chuc = n // 10
        donvi = n % 10

        # Bắt đầu đọc phần "chục"
        if chuc == 1:
            doc = "Mười"
        else:
            doc = so[chuc].capitalize() + " mươi"

        # Đọc phần "đơn vị"
        if donvi == 0:
            pass
        elif donvi == 1:
            # ví dụ: 21 -> "Hai mươi mốt"
            if chuc == 1:
                doc += " một"
            else:
                doc += " mốt"
        elif donvi == 4:
            doc += " tư"
        elif donvi == 5:
            if chuc == 0:
                doc += " năm"
            else:
                doc += " lăm"
        else:
            doc += " " + so[donvi]

        print(doc)
