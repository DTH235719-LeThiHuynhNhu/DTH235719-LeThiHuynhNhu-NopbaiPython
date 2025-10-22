import tkinter as tk
from tkinter import ttk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Quản Lý Cửa Hàng Tivi")
root.geometry("800x500")

# Tạo 2 frame: Tivi và Nhân viên
tivi_frame = tk.Frame(root)
nhanvien_frame = tk.Frame(root)

for frame in (tivi_frame, nhanvien_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# ======== Menu chuyển đổi =========
menu_frame = tk.Frame(root)
menu_frame.grid(row=1, column=0, sticky='ew')
tk.Button(menu_frame, text="Quản lý Tivi", command=lambda: show_frame(tivi_frame)).pack(side='left', padx=10, pady=5)
tk.Button(menu_frame, text="Quản lý Nhân viên", command=lambda: show_frame(nhanvien_frame)).pack(side='left', padx=10)

# ========= Giao diện Quản lý Tivi =========
tk.Label(tivi_frame, text="QUẢN LÝ TIVI", font=("Arial", 18)).pack(pady=10)

tivi_table = ttk.Treeview(tivi_frame, columns=("Ma", "Ten", "Hang", "Loai", "Size", "Gia", "SL"), show="headings")
for col in tivi_table["columns"]:
    tivi_table.heading(col, text=col)
tivi_table.pack(expand=True, fill='both', padx=20, pady=10)

# Dữ liệu mẫu
sample_tivi = [
    ("TV001", "LG Smart 43 inch", "LG", "Smart TV", "43", "7,990,000", "10"),
    ("TV002", "Samsung QLED 55", "Samsung", "QLED", "55", "14,500,000", "5"),
]
for item in sample_tivi:
    tivi_table.insert("", "end", values=item)

# ========= Giao diện Quản lý Nhân viên =========
tk.Label(nhanvien_frame, text="QUẢN LÝ NHÂN VIÊN", font=("Arial", 18)).pack(pady=10)

nv_table = ttk.Treeview(nhanvien_frame, columns=("Ma", "HoTen", "GioiTinh", "NgaySinh", "ChucVu"), show="headings")
for col in nv_table["columns"]:
    nv_table.heading(col, text=col)
nv_table.pack(expand=True, fill='both', padx=20, pady=10)

# Dữ liệu mẫu
sample_nv = [
    ("NV001", "Nguyễn Phước Minh", "Nam", "04/19/1975", "Trưởng phòng"),
    ("NV002", "Lý Văn Sang", "Nam", "12/12/1970", "Nhân viên chuyên trách"),
]
for item in sample_nv:
    nv_table.insert("", "end", values=item)

# Mặc định hiện frame quản lý Tivi
show_frame(tivi_frame)

root.mainloop()
