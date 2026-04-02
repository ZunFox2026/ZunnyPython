# Làm quen với thư viện Turtle
## Giới thiệu
Thư viện Turtle là một công cụ tuyệt vời trong Python, giúp bạn dễ dàng tạo ra các hình vẽ và hình ảnh động. Thư viện này được thiết kế để giúp người mới bắt đầu làm quen với lập trình và tạo ra các dự án thú vị. Trong bài này, chúng ta sẽ tìm hiểu cách sử dụng thư viện Turtle và tạo ra các hình vẽ cơ bản.

## Lý thuyết
Thư viện Turtle cung cấp một số hàm và phương thức để tạo ra các hình vẽ. Bạn có thể di chuyển con trỏ đến một vị trí cụ thể, vẽ một đường thẳng, vẽ một hình tròn, và nhiều hơn nữa. Để bắt đầu, bạn cần nhập thư viện Turtle vào chương trình của mình bằng câu lệnh `import turtle`. Sau đó, bạn có thể tạo ra một đối tượng Turtle bằng cách gọi hàm `turtle.Turtle()`. Đối tượng này sẽ là con trỏ mà bạn sẽ sử dụng để tạo ra các hình vẽ.

Một số phương thức phổ biến trong thư viện Turtle bao gồm:
- `forward(distance)`: Di chuyển con trỏ đến một vị trí cụ thể
- `backward(distance)`: Di chuyển con trỏ về phía sau
- `left(angle)`: Xoay con trỏ sang trái
- `right(angle)`: Xoay con trỏ sang phải
- `circle(radius)`: Vẽ một hình tròn

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện Turtle:
```python
import turtle

# Tạo ra một đối tượng Turtle
t = turtle.Turtle()

# Vẽ một hình vuông
for i in range(4):
    t.forward(100)  # Di chuyển con trỏ đến một vị trí cụ thể
    t.right(90)      # Xoay con trỏ sang phải

# Vẽ một hình tròn
t.circle(50)

# Đóng cửa sổ Turtle
turtle.done()
```
Đây là một ví dụ cơ bản về cách sử dụng thư viện Turtle. Bạn có thể thử nghiệm với các phương thức và hàm khác nhau để tạo ra các hình vẽ phức tạp hơn.

## Bài tập
Để củng cố kiến thức của mình, hãy thử hoàn thành các bài tập sau:
- Vẽ một hình tam giác
- Vẽ một hình chữ nhật
- Vẽ một hình ngôi sao
- Tạo ra một hình ảnh động bằng cách di chuyển con trỏ đến các vị trí khác nhau

Hãy nhớ rằng, thư viện Turtle cung cấp nhiều công cụ và phương thức để giúp bạn tạo ra các hình vẽ và hình ảnh động. Hãy thử nghiệm và khám phá các khả năng của thư viện này!