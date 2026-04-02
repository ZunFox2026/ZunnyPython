# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ, đồ thị và hình ảnh. Với matplotlib, bạn có thể tạo ra các biểu đồ từ đơn giản đến phức tạp, từ biểu đồ đường đến biểu đồ 3D. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Trước khi bắt đầu, bạn cần hiểu một số khái niệm cơ bản về matplotlib. Matplotlib cung cấp hai phương thức chính để tạo biểu đồ: phương thức procedural và phương thức hướng đối tượng. Phương thức procedural cho phép bạn tạo biểu đồ bằng cách gọi các hàm, trong khi phương thức hướng đối tượng cho phép bạn tạo biểu đồ bằng cách tạo ra các đối tượng. 
Một số hàm quan trọng trong matplotlib bao gồm:
- `plot()`: Tạo biểu đồ đường.
- `bar()`: Tạo biểu đồ cột.
- `hist()`: Tạo biểu đồ histogram.
- `scatter()`: Tạo biểu đồ phân tán.
- `show()`: Hiển thị biểu đồ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo biểu đồ đường:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()
```
Ví dụ này sẽ tạo ra một biểu đồ đường với các giá trị x và y tương ứng. Bạn cũng có thể thêm tiêu đề, nhãn và lưới vào biểu đồ bằng cách sử dụng các hàm như `title()`, `xlabel()`, `ylabel()` và `grid()`.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ cột so sánh số lượng sinh viên nam và nữ trong một lớp học. Giả sử số lượng sinh viên nam là 20 và số lượng sinh viên nữ là 25.
- Tạo danh sách các nhãn và giá trị tương ứng.
- Sử dụng hàm `bar()` để tạo biểu đồ cột.
- Thêm tiêu đề, nhãn và lưới vào biểu đồ.
- Hiển thị biểu đồ bằng hàm `show()`.
Khi hoàn thành bài tập này, bạn sẽ hiểu rõ hơn về cách sử dụng matplotlib để tạo ra các biểu đồ cơ bản và có thể áp dụng kiến thức này vào các dự án thực tế.