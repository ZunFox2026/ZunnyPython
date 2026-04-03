# main.py
# Bài học 1: Biến, kiểu dữ liệu, nhập xuất cơ bản

# --- Ví dụ 1: Chào hỏi người dùng ---
print("=== Ví dụ 1: Chào hỏi ===")
ten = input("Tên của bạn là gì? ")
print("Xin chào,", ten, "! Rất vui được gặp bạn.")

# --- Ví dụ 2: Tính tổng hai số ---
print("\n=== Ví dụ 2: Tính tổng hai số ===")
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
tong = so1 + so2
print("Tổng của", so1, "và", so2, "là:", tong)

# --- Ví dụ 3: Chuyển đổi nhiệt độ C sang F ---
print("\n=== Ví dụ 3: Chuyển đổi nhiệt độ ===")
celsius = float(input("Nhập nhiệt độ theo độ C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} độ C tương đương với {fahrenheit} độ F.")

# Kiểm tra kiểu dữ liệu (minh họa)
print("\n--- Kiểm tra kiểu dữ liệu ---")
x = 5
y = 3.14
z = "Hello"
b = True
print("Kiểu của x (5):", type(x))
print("Kiểu của y (3.14):", type(y))
print("Kiểu của z (\"Hello\"):", type(z))
print("Kiểu của b (True):", type(b))