
from XuLyFile import *

# Đọc dữ liệu từ file
arrSo = DocFile("csdl_so.txt")
print("Dữ liệu đọc được từ file:")
print(arrSo)

# Hàm xuất các số âm trên mỗi dòng
def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:          # row là 1 dòng dữ liệu (list các chuỗi)
        for element in row:    # element là từng số dạng chuỗi
            number = int(element)
            if number < 0:
                print(number, end='\t')  # in số âm, cách nhau bằng tab
        print()  # xuống dòng sau mỗi hàng

print("\nCác số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)
