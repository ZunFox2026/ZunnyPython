# Import thư viện turtle
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

# Vẽ một hình vuông
# Comment: Di chuyển con rùa về phía trước 100 đơn vị
for i in range(4):
    rua.forward(100)  # Di chuyển con rùa về phía trước 100 đơn vị
    rua.right(90)     # Quay con rùa 90 độ về phía bên phải

# Vẽ một hình tròn
# Comment: Di chuyển con rùa đến vị trí (-200, 0)
rua.penup()
rua.goto(-200, 0)
rua.pendown()

# Comment: Vẽ một hình tròn với bán kính 50 đơn vị
rua.circle(50)

# Vẽ một hình tam giác
# Comment: Di chuyển con rùa đến vị trí (200, 0)
rua.penup()
rua.goto(200, 0)
rua.pendown()

# Comment: Vẽ một hình tam giác
for i in range(3):
    rua.forward(100)  # Di chuyển con rùa về phía trước 100 đơn vị
    rua.left(120)     # Quay con rùa 120 độ về phía bên trái

# Giữ màn hình mở cho đến khi người dùng đóng lại
turtle.done()