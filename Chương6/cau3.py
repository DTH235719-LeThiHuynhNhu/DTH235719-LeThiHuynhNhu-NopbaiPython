from random import randrange

# ------------------------------
# Hàm tạo ma trận ngẫu nhiên
# ------------------------------
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))  # giá trị ngẫu nhiên từ 0 đến 99
        D.append(row)
    return D


# ------------------------------
# Hàm xuất ma trận
# ------------------------------
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()


# ------------------------------
# Hàm lấy 1 dòng
# ------------------------------
def LayDong(D, r):
    return D[r]


# ------------------------------
# Hàm xuất list 1 chiều
# ------------------------------
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()


# ------------------------------
# Hàm lấy 1 cột
# ------------------------------
def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C


# ------------------------------
# Hàm tìm giá trị lớn nhất trong ma trận
# ------------------------------
def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val


# ------------------------------
# Chương trình chính
# ------------------------------
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)
print("\n=== Ma trận vừa tạo ===")
XuatMaTran(D)

print("\nMời bạn nhập dòng muốn xuất:")
r = int(input())
print("Dòng", r, "là:")
XuatList1Chieu(LayDong(D, r))

print("\nMời bạn nhập cột muốn xuất:")
c = int(input())
print("Cột", c, "là:")
XuatList1Chieu(LayCot(D, c))

max_value = MAX(D)
print("\n✅ Số lớn nhất trong ma trận =", max_value)
