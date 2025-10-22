# --- CÂU 10: XỬ LÝ MA TRẬN ---
from random import randint

def nhap_ma_tran(m, n, ten):
    print(f"\nNhập ma trận {ten}:")
    mat = []
    for i in range(m):
        hang = []
        for j in range(n):
            x = int(input(f"{ten}[{i}][{j}] = "))
            hang.append(x)
        mat.append(hang)
    return mat

def in_ma_tran(M, ten):
    print(f"\nMa trận {ten}:")
    for hang in M:
        for x in hang:
            print(f"{x:5}", end="")
        print()

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        hang = []
        for j in range(n):
            hang.append(A[i][j] + B[i][j])
        C.append(hang)
    return C

def hoan_vi(M):
    m = len(M)
    n = len(M[0])
    HT = []
    for j in range(n):
        hang = []
        for i in range(m):
            hang.append(M[i][j])
        HT.append(hang)
    return HT

# --- CHƯƠNG TRÌNH CHÍNH ---
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = nhap_ma_tran(m, n, "A")
B = nhap_ma_tran(m, n, "B")

in_ma_tran(A, "A")
in_ma_tran(B, "B")

C = cong_ma_tran(A, B)
in_ma_tran(C, "C = A + B")

A_T = hoan_vi(A)
B_T = hoan_vi(B)

in_ma_tran(A_T, "A chuyển vị")
in_ma_tran(B_T, "B chuyển vị")
