# Làm quen với thư viện Matplotlib
## Giới thiệu
Matplotlib là một thư viện đồ họa nổi tiếng của Python, được sử dụng rộng rãi trong việc tạo ra các loại biểu đồ, từ đơn giản đến phức tạp. Thư viện này cung cấp rất nhiều công cụ và tính năng giúp người dùng dễ dàng tạo ra các biểu đồ đẹp và chuyên nghiệp. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện Matplotlib để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Trước khi bắt đầu tạo ra các biểu đồ, chúng ta cần hiểu về một số khái niệm cơ bản của Matplotlib. Thư viện này cung cấp hai loại biểu đồ chính: biểu đồ 2D và biểu đồ 3D. Biểu đồ 2D được sử dụng để thể hiện dữ liệu trên hai trục (x và y), trong khi biểu đồ 3D được sử dụng để thể hiện dữ liệu trên ba trục (x, y và z). Để tạo ra một biểu đồ, chúng ta cần import thư viện Matplotlib, sau đó sử dụng các hàm và phương thức của nó để tạo ra biểu đồ.

Một số hàm và phương thức quan trọng của Matplotlib bao gồm:
- `plot()`: Tạo ra một biểu đồ 2D đơn giản.
- `scatter()`: Tạo ra một biểu đồ phân tán.
- `bar()`: Tạo ra một biểu đồ cột.
- `hist()`: Tạo ra một biểu đồ histogram.
- `title()`: Thêm tiêu đề cho biểu đồ.
- `xlabel()` và `ylabel()`: Thêm nhãn cho trục x và y.

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng Matplotlib để tạo ra một biểu đồ 2D đơn giản:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ 2D đơn giản')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.show()
```
Kết quả của ví dụ này sẽ là một biểu đồ 2D đơn giản với tiêu đề, nhãn cho trục x và y.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ cột so sánh số lượng sinh viên của ba trường đại học. Dữ liệu như sau:
- Trường Đại học A: 1000 sinh viên
- Trường Đại học B: 1200 sinh viên
- Trường Đại học C: 1500 sinh viên

Hãy sử dụng Matplotlib để tạo ra một biểu đồ cột thể hiện số lượng sinh viên của từng trường. Thêm tiêu đề, nhãn cho trục x và y vào biểu đồ.