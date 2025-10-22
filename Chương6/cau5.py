# ==============================
# Câu 5: Xác định kết quả khi thực thi list
# ==============================

# Khởi tạo list
lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("List =", lst)
print("----------------------------")

# Các biểu thức kiểm tra
print("(a) lst =", lst)
print("(b) lst[0:3] =", lst[0:3])       # Lấy phần tử từ vị trí 0 đến 2
print("(c) lst[4:8] =", lst[4:8])       # Lấy phần tử từ 4 đến 7
print("(d) lst[4:33] =", lst[4:33])     # Nếu vượt quá, chỉ lấy đến cuối list
print("(e) lst[-5:-3] =", lst[-5:-3])   # Dùng chỉ số âm
print("(f) lst[-22:3] =", lst[-22:3])   # Bắt đầu nhỏ hơn phạm vi => từ đầu tới 2
print("(g) lst[4:] =", lst[4:])         # Từ phần tử thứ 4 đến hết
print("(h) lst[:] =", lst[:])           # Sao chép toàn bộ list
print("(i) lst[:4] =", lst[:4])         # Từ đầu đến phần tử thứ 3
print("(j) lst[1:5] =", lst[1:5])       # Từ phần tử thứ 1 đến 4
print("(k) -34 in lst =", (-34 in lst)) # Kiểm tra -34 có trong list?
print("(l) -34 not in lst =", (-34 not in lst))  # Ngược lại
print("(m) len(lst) =", len(lst))       # Độ dài của list
