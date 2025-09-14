# Câu 8: Các loại lỗi khi lập trình và cách bắt lỗi trong Python

print("=== 1. Các loại lỗi khi lập trình ===")

# a) Lỗi cú pháp (SyntaxError): 
# -> Xảy ra khi viết sai cú pháp, ví dụ: if True print("Hi")
print("- Lỗi cú pháp (SyntaxError): Sai quy tắc ngôn ngữ, chương trình không chạy được.")

# b) Lỗi thời gian chạy (Runtime Error / Exception):
print("- Lỗi runtime (Exception): Chương trình chạy nhưng dừng đột ngột do tình huống bất hợp lệ.")
try:
    x = 5 / 0   # gây lỗi ZeroDivisionError
except ZeroDivisionError:
    print("Ví dụ: chia cho 0 sẽ gây ra ZeroDivisionError.")

# c) Lỗi logic (Logic Error):
print("- Lỗi logic: Cú pháp đúng, chạy được nhưng kết quả sai mong muốn.")
n = 5
s = 0
for i in range(1, n):  # lỗi logic: thiếu n+1
    s += i
print("Ví dụ: tổng 1..5 bị tính sai =", s)

print("\n=== 2. Cách bắt lỗi trong Python (try-except) ===")

try:
    x = int(input("Nhập một số nguyên: "))
    print("10 chia cho x =", 10 / x)
except ZeroDivisionError:
    print("Không thể chia cho 0 (ZeroDivisionError).")
except ValueError:
    print("Nhập sai kiểu dữ liệu (ValueError).")
else:
    print("Không có lỗi, chương trình chạy bình thường.")
finally:
    print("Khối finally: Luôn được thực hiện, kết thúc chương trình.")
