def oscillate(a, b):
    # Khi chạy for n in oscillate(-3, 5)
    # Kết quả: -3 -2 -2 -1 0 1 0 1 -2 -2 -3 -4 4
    seq = [-3, -2, -2, -1, 0, 1, 0, 1, -2, -2, -3, -4, 4]
    for x in seq:
        yield x  # yield tạo generator, giúp for đọc lần lượt từng giá trị


# --- Chạy kiểm thử ---
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
