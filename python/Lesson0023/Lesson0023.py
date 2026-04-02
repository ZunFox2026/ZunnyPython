# Khởi tạo màn hình
import turtle

# Tạo một màn hình mới
man_hinh = turtle.Screen()

# Đặt tiêu đề cho màn hình
man_hinh.title("Làm quen với thư viện Turtle")

# Tạo một con rùa mới
rua = turtle.Turtle()

# Di chuyển con rùa đến vị trí (0, 0)
rua.penup()
rua.goto(0, 0)
rua.pendown()

# Vẽ hình vuông
# Comment: Dưới đây là đoạn code để vẽ hình vuông
for _ in range(4):
    rua.forward(100)  # Di chuyển con rùa 100 bước về phía trước
    rua.right(90)      # Quay con rùa 90 độ về phía phải

# Vẽ hình tròn
# Comment: Dưới đây là đoạn code để vẽ hình tròn
rua.penup()
rua.goto(-150, 0)
rua.pendown()
rua.circle(50)       # Vẽ hình tròn với bán kính 50

# Vẽ hình tam giác
# Comment: Dưới đây là đoạn code để vẽ hình tam giác
rua.penup()
rua.goto(150, 0)
rua.pendown()
for _ in range(3):
    rua.forward(100)  # Di chuyển con rùa 100 bước về phía trước
    rua.left(120)      # Quay con rùa 120 độ về phía trái

# Giữ màn hình mở
turtle.done()