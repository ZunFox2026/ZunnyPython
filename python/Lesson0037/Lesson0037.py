# Nhập thư viện Matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ đường
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu khác
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]

# Tạo biểu đồ đường với nhiều đường
plt.plot(x, y1, label='Đường 1')
plt.plot(x, y2, label='Đường 2')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường với nhiều đường')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu khác
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu khác
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]

# Tạo biểu đồ cột với nhiều cột
x = [1, 2, 3, 4, 5]
bar_width = 0.4
plt.bar([i - bar_width/2 for i in x], y1, bar_width, label='Cột 1')
plt.bar([i + bar_width/2 for i in x], y2, bar_width, label='Cột 2')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột với nhiều cột')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()