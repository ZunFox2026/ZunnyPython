# Import thư viện Turtle
import turtle

# Tạo một cửa sổ mới với tiêu đề "Làm quen với thư viện Turtle"
window = turtle.Screen()
window.title("Làm quen với thư viện Turtle")

# Tạo một con rùa mới
my_turtle = turtle.Turtle()

# Đặt tốc độ di chuyển của con rùa
my_turtle.speed(2)

# Di chuyển con rùa tới vị trí (100, 100)
my_turtle.penup()
my_turtle.goto(100, 100)
my_turtle.pendown()

# Vẽ một hình vuông
for _ in range(4):
    my_turtle.forward(100)  # Di chuyển con rùa tới phía trước 100 đơn vị
    my_turtle.right(90)     # Quay con rùa sang phải 90 độ

# Viết chữ "Xin chào"
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()
my_turtle.write("Xin chào", font=("Arial", 24, "bold"))

# Giữ cửa sổ mở cho đến khi người dùng đóng nó
window.mainloop()