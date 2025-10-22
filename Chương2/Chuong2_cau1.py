import math  # Dùng để lấy giá trị số pi

# Nhập bán kính từ bàn phím
r = float(input("Nhập bán kính đường tròn r: "))

# Tính chu vi và diện tích
chu_vi = 2 * math.pi * r
dien_tich = math.pi * r * r

# In kết quả
print("Chu vi đường tròn là:", chu_vi)
print("Diện tích đường tròn là:", dien_tich)

 