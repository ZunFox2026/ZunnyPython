# Làm quen với thư viện Matplotlib
## Giới thiệu
Thư viện Matplotlib là một trong những thư viện phổ biến nhất của Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Nó cung cấp một giao diện người dùng đơn giản và linh hoạt, giúp người dùng dễ dàng tạo ra các biểu đồ phức tạp. Trong bài viết này, chúng ta sẽ tìm hiểu cách làm quen với thư viện Matplotlib và sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, v.v. Để tạo ra một biểu đồ, bạn cần nhập thư viện Matplotlib vào chương trình của mình bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm như `plt.plot()`, `plt.bar()`, `plt.pie()` để tạo ra các biểu đồ khác nhau. Thư viện Matplotlib cũng cung cấp nhiều tùy chọn để tùy chỉnh biểu đồ, như thay đổi màu sắc, kích thước, v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng Matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
Khi chạy chương trình này, bạn sẽ thấy một biểu đồ đường với tiêu đề "Biểu đồ đường" và các nhãn X, Y. Biểu đồ này thể hiện mối quan hệ giữa các giá trị X và Y.

## Bài tập
Để thực hành sử dụng Matplotlib, hãy thử tạo ra các biểu đồ sau:
- Biểu đồ cột thể hiện số lượng sinh viên ở các lớp khác nhau.
- Biểu đồ tròn thể hiện tỷ lệ giữa các loại thực phẩm khác nhau trong một bữa ăn.
- Biểu đồ đường thể hiện sự thay đổi của nhiệt độ trong một ngày.
Hãy sử dụng các hàm và tùy chọn của Matplotlib để tạo ra các biểu đồ chất lượng cao và đẹp mắt.