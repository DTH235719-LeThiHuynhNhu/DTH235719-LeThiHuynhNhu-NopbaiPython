from tkinter import *

# =========================
# CÁC HÀM XỬ LÝ
# =========================
def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia 0!")
        else:
            stringKQ.set(a / b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

# =========================
# GIAO DIỆN CHÍNH
# =========================
root = Tk()
root.title("Máy tính 4 phép tính")
root.minsize(height=200, width=300)
root.resizable(False, False)

# Biến lưu dữ liệu
stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="CỘNG - TRỪ - NHÂN - CHIA", fg="blue", font=("Tahoma", 16)).grid(row=0, column=0, columnspan=3, pady=10)

# Khung nút
frameButton = Frame(root)
Button(frameButton, text="Cộng", command=congAction, width=8).pack(side=TOP, fill=X, pady=2)
Button(frameButton, text="Trừ", command=truAction, width=8).pack(side=TOP, fill=X, pady=2)
Button(frameButton, text="Nhân", command=nhanAction, width=8).pack(side=TOP, fill=X, pady=2)
Button(frameButton, text="Chia", command=chiaAction, width=8).pack(side=TOP, fill=X, pady=2)
frameButton.grid(row=1, column=0, rowspan=4, padx=10)

# Nhập và xuất dữ liệu
Label(root, text="Số a:").grid(row=1, column=1, sticky=W)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2)

Label(root, text="Số b:").grid(row=2, column=1, sticky=W)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1, sticky=W)
Entry(root, width=15, textvariable=stringKQ).grid(row=3, column=2)

Button(root, text="Thoát", command=root.quit, width=8).grid(row=4, column=2, pady=5)

root.mainloop()
