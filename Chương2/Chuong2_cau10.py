# Khởi tạo giá trị ban đầu
x = 10
y = 5
ncc = 3
number_of_closed_cases = 8

print("Giá trị ban đầu:")
print(f"x = {x}, y = {y}, ncc = {ncc}, number_of_closed_cases = {number_of_closed_cases}")
print("-" * 40)

# (a) x = x + 1
x += 1
print("(a) x += 1  --> x =", x)

# (b) x = x / 2
x /= 2
print("(b) x /= 2  --> x =", x)

# (c) x = x - 1
x -= 1
print("(c) x -= 1  --> x =", x)

# (d) x = x + y
x += y
print("(d) x += y  --> x =", x)

# (e) x = x - (y + 7)
x -= (y + 7)
print("(e) x -= (y + 7)  --> x =", x)

# (f) x = 2 * x
x *= 2
print("(f) x *= 2  --> x =", x)

# (g) number_of_closed_cases = number_of_closed_cases + 2 * ncc
number_of_closed_cases += 2 * ncc
print("(g) number_of_closed_cases += 2 * ncc  --> number_of_closed_cases =", number_of_closed_cases)
