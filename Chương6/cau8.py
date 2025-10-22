def nhap_day_so():
    n = int(input("Nhập số phần tử của dãy: "))
    M = []
    for i in range(n):
        x = float(input(f"Nhập M[{i}]: "))
        M.append(x)
    return M

def sap_xep_giam(M):
    M.sort(reverse=True)
    return M

# Chương trình chính
M = nhap_day_so()
print("\nDãy số ban đầu:")
print(M)

M = sap_xep_giam(M)
print("\nDãy số sau khi sắp xếp giảm dần:")
print(M)
