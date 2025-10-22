print("Chương trình thực hiện phép toán với hai số a và b")

# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
pheptoan = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if pheptoan == '+':
    kq = a + b
    print("Kết quả:", a, "+", b, "=", kq)

elif pheptoan == '-':
    kq = a - b
    print("Kết quả:", a, "-", b, "=", kq)

elif pheptoan == '*':
    kq = a * b
    print("Kết quả:", a, "*", b, "=", kq)

elif pheptoan == '/':
    if b == 0:
        print("Lỗi: không thể chia cho 0!")
    else:
        kq = a / b
        print("Kết quả:", a, "/", b, "=", kq)

else:
    print("Phép toán không hợp lệ! Vui lòng nhập một trong (+, -, *, /).")
