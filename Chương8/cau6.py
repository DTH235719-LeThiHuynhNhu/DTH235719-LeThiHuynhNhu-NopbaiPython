import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("frame 2")

# Tạo frame bao quanh
frame = ttk.LabelFrame(root, text="frame 2", padding=10)
frame.pack(padx=10, pady=10)

# Các loại relief (style viền của Button)
reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

# Tạo các hàng button với độ dày viền khác nhau
for border in range(5):  # từ 0 đến 4
    tk.Label(frame, text=f"borderwidth = {border}", width=15).grid(row=border, column=0, padx=5, pady=3)
    for j, relief in enumerate(reliefs):
        tk.Button(
            frame,
            text=relief,
            relief=relief,
            borderwidth=border,
            width=8
        ).grid(row=border, column=j + 1, padx=5, pady=3)

root.mainloop()
