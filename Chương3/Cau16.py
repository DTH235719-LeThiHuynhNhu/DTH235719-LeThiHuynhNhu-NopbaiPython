print("=== CHƯƠNG TRÌNH ĐẾM DẤU * IN RA MÀN HÌNH ===")

count = 0  # Biến đếm số dấu *

for a in range(20, 100, 5):
    print('*', end='')  # In dấu *
    count += 1          # Tăng biến đếm

print()  # Xuống dòng sau khi in xong
print("Tổng số dấu * được in ra là:", count)
