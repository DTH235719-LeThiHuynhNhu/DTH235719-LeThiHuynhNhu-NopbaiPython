# --- CÂU 9: XỬ LÝ MẢNG ---

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập mảng
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Dòng 1: số lẻ
le = [x for x in M if x % 2 != 0]
print("Các số lẻ:", le)
print("Tổng cộng có", len(le), "số lẻ.\n")

# Dòng 2: số chẵn
chan = [x for x in M if x % 2 == 0]
print("Các số chẵn:", chan)
print("Tổng cộng có", len(chan), "số chẵn.\n")

# Dòng 3: số nguyên tố
nto = [x for x in M if la_nguyen_to(x)]
print("Các số nguyên tố:", nto)

# Dòng 4: không phải số nguyên tố
ko_nto = [x for x in M if not la_nguyen_to(x)]
print("Các số không phải nguyên tố:", ko_nto)
