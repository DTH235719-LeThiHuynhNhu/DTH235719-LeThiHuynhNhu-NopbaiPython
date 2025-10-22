# Câu 9 (tiếp): Giải thích kết quả tính toán của các biểu thức (k) -> (r)

i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

print("k) d1 + (d2 * d3) =", d1 + (d2 * d3))
print("   Thực hiện: d2 * d3 = 5.0 * -0.5 = -2.5; d1 + (-2.5) = 2.0 - 2.5 = -0.5")

print("l) d1 + d2 * d3 =", d1 + d2 * d3)
print("   Quy tắc ưu tiên: nhân trước, cộng sau -> kết quả giống (k) = -0.5")

print("m) d1 / d2 - d3 =", d1 / d2 - d3)
print("   Thực hiện: d1 / d2 = 2.0 / 5.0 = 0.4; 0.4 - (-0.5) = 0.4 + 0.5 = 0.9")

print("n) d1 / (d2 - d3) =", d1 / (d2 - d3))
print("   Thực hiện: d2 - d3 = 5.0 - (-0.5) = 5.5; 2.0 / 5.5 = 0.363636...")

print("o) d1 + d2 + d3 / 3 =", d1 + d2 + d3 / 3)
print("   Quy tắc ưu tiên: d3 / 3 = -0.5 / 3 = -0.1666...; 2.0 + 5.0 - 0.1666... = 6.8333...")

print("p) (d1 + d2 + d3) / 3 =", (d1 + d2 + d3) / 3)
print("   Thực hiện: d1 + d2 + d3 = 2.0 + 5.0 - 0.5 = 6.5; 6.5 / 3 = 2.1666...")

print("q) d1 + d2 + (d3 / 3) =", d1 + d2 + (d3 / 3))
print("   Thực hiện: d3 / 3 = -0.5 / 3 = -0.1666...; 2.0 + 5.0 - 0.1666... = 6.8333... (giống o)")

print("r) 3 * (d1 + d2) * (d1 - d3) =", 3 * (d1 + d2) * (d1 - d3))
print("   Thực hiện: d1 + d2 = 2.0 + 5.0 = 7.0; d1 - d3 = 2.0 - (-0.5) = 2.5; 3 * 7.0 * 2.5 = 52.5")
