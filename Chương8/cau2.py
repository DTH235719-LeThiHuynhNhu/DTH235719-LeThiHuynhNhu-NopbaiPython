from tkinter import *
from math import sqrt

# =========================
# HÀM GIẢI PHƯƠNG TRÌNH
# =========================
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:  # bx + c = 0
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set("x = " + str(x))
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                x = -b / (2 * a)
                stringKQ.set("Nghiệm kép x1 = x2 = " + str(x))
            else:
                x1 = (-b - sqrt(delta)) / (2 * a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                stringKQ.set("x1 = " + str(x1) + "; x2 = " + str(x2))
    except ValueError:
        stringKQ.set("❌ Nhập sai hệ số!")

# =========================
# HÀM TIẾP TỤC
# =========================
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# =========================
# GIAO DIỆN CHÍNH
# =========================
root = Tk()
root.title("Giải phương trình bậc 2")
root.minsize(height=180, width=320)
root.resizable(False, False)

# Khai báo biến
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="Phương Trình Bậc 2", fg="red", font=("Tahoma", 16)).grid(row=0, column=0, columnspan=2, pady=5)

# Nhập hệ số
Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=W)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=W)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=W)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

# Các nút chức năng
frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction, width=8).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp", command=tiepAction, width=8).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", command=root.quit, width=8).pack(side=LEFT, padx=5)
frameButton.grid(row=4, column=0, columnspan=2, pady=5)

# Kết quả
Label(root, text="Kết quả:").grid(row=5, column=0, sticky=W)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()
