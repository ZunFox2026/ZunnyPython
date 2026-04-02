# Nhập thư viện Matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.plot(x, y)

# Thêm tiêu đề
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và y
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị nhiều đường
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]

plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x + 1')

plt.title('Đồ thị hàm số')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Tạo đồ thị hình tròn
plt.pie([25, 30, 45], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title('Đồ thị hình tròn')
plt.show()

# Tạo đồ thị cột
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]
plt.bar(x, y)
plt.title('Đồ thị cột')
plt.xlabel('x')
plt.ylabel('y')
plt.show()