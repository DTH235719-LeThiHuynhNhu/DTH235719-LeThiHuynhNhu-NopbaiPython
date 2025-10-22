print("=== CHƯƠNG TRÌNH KIỂM TRA SỐ NGUYÊN TỐ ===")

def la_so_nguyen_to(n):
    """Hàm kiểm tra số nguyên tố"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chạy chương trình lặp cho đến khi người dùng muốn thoát
while True:
    n = int(input("Nhập vào một số nguyên dương: "))

    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố.")

    tieptuc = input("Bạn có muốn kiểm tra tiếp không? (c/k): ").lower()
    if tieptuc != 'c':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
