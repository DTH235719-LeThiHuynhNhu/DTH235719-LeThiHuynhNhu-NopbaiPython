from datetime import date, timedelta

print("Chương trình tìm ngày kế tiếp")

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    d = date(nam, thang, ngay)          # Tạo đối tượng ngày
    ngay_sau = d + timedelta(days=1)    # Cộng thêm 1 ngày
    print("Ngày kế tiếp là: {}/{}/{}".format(ngay_sau.day, ngay_sau.month, ngay_sau.year))
except ValueError:
    print("Ngày tháng năm không hợp lệ!")
