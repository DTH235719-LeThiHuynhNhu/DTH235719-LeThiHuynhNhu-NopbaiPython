from tkinter import *

# =========================
# HÀM XỬ LÝ
# =========================
def nhanPhim(giatri):
    hien_thi.set(hien_thi.get() + str(giatri))

def xoaTatCa():
    hien_thi.set("")

def tinhToan():
    try:
        ketqua = str(eval(hien_thi.get()))
        hien_thi.set(ketqua)
    except:
        hien_thi.set("Lỗi!")

# =========================
# GIAO DIỆN CHÍNH
# =========================
root = Tk()
root.title("Máy tính bỏ túi")
root.resizable(False, False)
root.geometry("260x330")

# Biến hiển thị
hien_thi = StringVar()

# Ô hiển thị kết quả
Entry(root, textvariable=hien_thi, font=("Arial", 20), justify='right', bd=10).grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# =========================
# CÁC NÚT SỐ & PHÉP TOÁN
# =========================
nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in nut:
    if text == '=':
        Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="#4CAF50", fg="white", command=tinhToan).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: nhanPhim(t)).grid(row=row, column=col, padx=5, pady=5)

# Nút xóa toàn bộ
Button(root, text="C", width=22, height=2, font=("Arial", 14), bg="red", fg="white", command=xoaTatCa).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
