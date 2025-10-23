import tkinter as tk

def convert_temp():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        label_result.config(text=f"{c:.2f} °C")
    except:
        label_result.config(text="Nhập sai định dạng!")

root = tk.Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("300x150")
root.configure(bg="lightyellow")

tk.Label(root, text="Nhập độ F:", bg="lightyellow").pack(pady=5)
entry_f = tk.Entry(root)
entry_f.pack()

tk.Button(root, text="Chuyển", command=convert_temp, bg="lightblue").pack(pady=5)
label_result = tk.Label(root, text="", bg="lightyellow", font=("Arial", 10, "bold"))
label_result.pack(pady=5)

root.mainloop()
