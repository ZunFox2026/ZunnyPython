# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong lĩnh vực khoa học dữ liệu và phân tích dữ liệu bằng ngôn ngữ lập trình Python. Matplotlib cung cấp các công cụ để tạo ra các biểu đồ và đồ thị chất lượng cao, giúp chúng ta có thể trực quan hóa dữ liệu và đưa ra các quyết định dựa trên dữ liệu một cách dễ dàng hơn.

Matplotlib hỗ trợ nhiều loại biểu đồ và đồ thị khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, biểu đồ phân tán và nhiều loại khác. Thư viện này cũng cung cấp nhiều tùy chọn để tùy chỉnh biểu đồ, chẳng hạn như thay đổi màu sắc, kích thước, font chữ và nhiều thứ khác.

## Lý thuyết
Để sử dụng matplotlib, trước tiên bạn cần phải cài đặt thư viện này vào môi trường Python của mình. Điều này có thể được thực hiện bằng cách chạy lệnh `pip install matplotlib` trong terminal hoặc command prompt.

Sau khi cài đặt, bạn có thể nhập thư viện matplotlib vào chương trình Python của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`. Từ đó, bạn có thể sử dụng các hàm và phương thức của matplotlib để tạo ra các biểu đồ và đồ thị.

Một số hàm và phương thức cơ bản của matplotlib bao gồm:
- `plt.plot()`: Tạo ra một biểu đồ đường.
- `plt.bar()`: Tạo ra một biểu đồ cột.
- `plt.pie()`: Tạo ra một biểu đồ tròn.
- `plt.scatter()`: Tạo ra một biểu đồ phân tán.
- `plt.show()`: Hiển thị biểu đồ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt

# Dữ liệu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ
plt.plot(x, y)

# Hiển thị biểu đồ
plt.show()
```
Kết quả sẽ là một biểu đồ đường với dữ liệu được chỉ định.

## Bài tập
Bài tập cho bạn:
- Tạo ra một biểu đồ cột với dữ liệu sau: `x = [1, 2, 3, 4, 5]`, `y = [2, 4, 6, 8, 10]`.
- Tạo ra một biểu đồ tròn với dữ liệu sau: `labels = ['A', 'B', 'C', 'D']`, `sizes = [15, 30, 45, 10]`.
- Thử nghiệm với các tùy chọn khác nhau của matplotlib để tùy chỉnh biểu đồ.