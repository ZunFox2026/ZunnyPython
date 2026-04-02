# Làm quen với thư viện Turtle
## Giới thiệu
Thư viện Turtle là một công cụ tuyệt vời trong Python giúp bạn tạo ra các hình ảnh và hình dạng khác nhau bằng cách sử dụng các chức năng đơn giản. Thư viện này thường được sử dụng để giới thiệu lập trình cho người mới bắt đầu, đặc biệt là trẻ em. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện Turtle để tạo ra các hình dạng cơ bản.

## Lý thuyết
Thư viện Turtle cung cấp một số chức năng cơ bản để tạo ra các hình dạng, bao gồm:
- `forward()`: Di chuyển con trỏ về phía trước một khoảng cách nhất định.
- `backward()`: Di chuyển con trỏ về phía sau một khoảng cách nhất định.
- `left()`: Quay con trỏ sang trái một góc nhất định.
- `right()`: Quay con trỏ sang phải một góc nhất định.
- `penup()`: Nâng bút lên, không vẽ khi di chuyển.
- `pendown()`: Đặt bút xuống, vẽ khi di chuyển.
- `color()`: Thay đổi màu vẽ.
- `begin_fill()`: Bắt đầu tô màu.
- `end_fill()`: Kết thúc tô màu.

Chúng ta có thể sử dụng các chức năng này để tạo ra các hình dạng khác nhau, từ đơn giản đến phức tạp.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng thư viện Turtle để vẽ một hình vuông:
```python
import turtle

# Tạo một con trỏ
t = turtle.Turtle()

# Vẽ một hình vuông
for i in range(4):
    t.forward(100)  # Di chuyển về phía trước 100 đơn vị
    t.right(90)  # Quay sang phải 90 độ

# Kết thúc
turtle.done()
```
Trong ví dụ này, chúng ta đã sử dụng vòng lặp `for` để lặp lại 4 lần, mỗi lần di chuyển về phía trước 100 đơn vị và quay sang phải 90 độ. Kết quả là một hình vuông với mỗi cạnh dài 100 đơn vị.

## Bài tập
Bài tập này yêu cầu bạn sử dụng thư viện Turtle để vẽ một hình tam giác. Bạn có thể sử dụng các chức năng đã được giới thiệu trong bài này để tạo ra hình dạng mong muốn. Hãy thử nghiệm với các giá trị khác nhau để tạo ra các hình tam giác khác nhau.

Một số gợi ý:
- Sử dụng `forward()` và `left()` để di chuyển và quay con trỏ.
- Thử nghiệm với các giá trị khác nhau cho khoảng cách di chuyển và góc quay.
- Sử dụng `color()` để thay đổi màu vẽ.
- Sử dụng `begin_fill()` và `end_fill()` để tô màu cho hình tam giác.

Hãy chia sẻ kết quả của bạn và xem xét các cách khác nhau để giải quyết bài tập này!