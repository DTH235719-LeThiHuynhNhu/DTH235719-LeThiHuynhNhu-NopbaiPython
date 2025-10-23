import tkinter as tk
from tkinter import messagebox

def change_password():
    old_pwd = entry_old.get()
    new_pwd = entry_new.get()
    confirm_pwd = entry_confirm.get()

    # Giả lập mật khẩu cũ hiện tại (ví dụ: "123456")
    current_password = "123456"

    if old_pwd != current_password:
        messagebox.showerror("Error", "Old password is incorrect!")
    elif new_pwd == "":
        messagebox.showwarning("Warning", "New password cannot be empty!")
    elif new_pwd != confirm_pwd:
        messagebox.showerror("Error", "New passwords do not match!")
    else:
        # Thay mật khẩu thành công
        messagebox.showinfo("Success", "Password changed successfully!")
        entry_old.delete(0, tk.END)
        entry_new.delete(0, tk.END)
        entry_confirm.delete(0, tk.END)

def cancel_action():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Enter New Password")
root.geometry("300x180")
root.resizable(False, False)

# Giao diện nhãn và ô nhập
tk.Label(root, text="Old Password:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="New Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_old = tk.Entry(root, show="*")
entry_new = tk.Entry(root, show="*")
entry_confirm = tk.Entry(root, show="*")

entry_old.grid(row=0, column=1, padx=10, pady=5)
entry_new.grid(row=1, column=1, padx=10, pady=5)
entry_confirm.grid(row=2, column=1, padx=10, pady=5)

# Nút OK và Cancel
tk.Button(root, text="OK", width=10, command=change_password).grid(row=3, column=0, pady=15)
tk.Button(root, text="Cancel", width=10, command=cancel_action).grid(row=3, column=1, pady=15)

root.mainloop()
