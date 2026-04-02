# Làm quen với thư viện Matplotlib
## Giới thiệu
Matplotlib là một thư viện phổ biến trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Thư viện này cung cấp một loạt các công cụ để tạo ra các loại biểu đồ khác nhau, từ biểu đồ đơn giản đến phức tạp. Trong bài này, chúng ta sẽ tìm hiểu cách sử dụng Matplotlib để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm:
- Biểu đồ đường (line plot)
- Biểu đồ cột (bar plot)
- Biểu đồ tròn (pie chart)
- Biểu đồ phân tán (scatter plot)
Mỗi loại biểu đồ đều có những phương thức và thuộc tính riêng để tùy chỉnh. Để tạo ra một biểu đồ, chúng ta cần nhập thư viện Matplotlib và sử dụng các hàm tương ứng.

## Ví dụ
Ví dụ, để tạo ra một biểu đồ đường đơn giản, chúng ta có thể sử dụng hàm `plot()` như sau:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ đường')
plt.show()
```
Điều này sẽ tạo ra một biểu đồ đường với x và y là các giá trị tương ứng. Chúng ta cũng có thể thêm tiêu đề, nhãn x và y để làm cho biểu đồ rõ ràng hơn.

## Bài tập
Bài tập:
- Tạo ra một biểu đồ cột với 5 cột, mỗi cột đại diện cho một loại trái cây (táo, chuối, cam, dưa hấu, xoài) và số lượng tương ứng (10, 15, 20, 25, 30).
- Tạo ra một biểu đồ tròn với 4 phần, mỗi phần đại diện cho một mùa (xuân, hè, thu, đông) và tỉ lệ tương ứng (20%, 30%, 20%, 30%).
- Thử nghiệm với các loại biểu đồ khác và các tùy chỉnh khác nhau để làm quen với thư viện Matplotlib.