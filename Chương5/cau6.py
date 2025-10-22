
import re

def NegativeNumberInString(s):
    so_am = re.findall(r'-\d+', s)  # tìm tất cả số âm
    return [int(x) for x in so_am]

def main():
    s = input("Nhập chuỗi: ")
    ds_am = NegativeNumberInString(s)
    if ds_am:
        print("✅ Các số nguyên âm trong chuỗi là:", ds_am)
    else:
        print("❌ Không có số âm nào trong chuỗi!")

# Gọi hàm
main()
