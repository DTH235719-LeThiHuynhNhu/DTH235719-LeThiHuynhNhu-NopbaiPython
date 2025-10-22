print("Chương trình xác định quý trong năm")
a = float(input("Nhập số a: "))
# Nhập tháng
thang = int(input("Nhập vào số tháng (1–12): "))

# Kiểm tra và xuất quý
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
elif thang in (1, 2, 3):
    print("Tháng", thang, "thuộc quý I (Quý 1)")
elif thang in (4, 5, 6):
    print("Tháng", thang, "thuộc quý II (Quý 2)")
elif thang in (7, 8, 9):
    print("Tháng", thang, "thuộc quý III (Quý 3)")
else:
    print("Tháng", thang, "thuộc quý IV (Quý 4)")
