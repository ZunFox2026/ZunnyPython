# Làm quen với thư viện Matplotlib
## Giới thiệu
Matplotlib là một thư viện đồ họa Python phổ biến, được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học, kỹ thuật, kinh tế,... Thư viện này cung cấp các công cụ để tạo ra nhiều loại biểu đồ khác nhau, từ biểu đồ đơn giản đến phức tạp. Trong bài học này, chúng ta sẽ tìm hiểu cách sử dụng Matplotlib để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm:
- Biểu đồ đường (line plot)
- Biểu đồ cột (bar plot)
- Biểu đồ tròn (pie chart)
- Biểu đồ phân tán (scatter plot)
Để sử dụng Matplotlib, bạn cần nhập thư viện này vào chương trình Python của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm như `plt.plot()`, `plt.bar()`, `plt.pie()`, `plt.scatter()` để tạo ra các biểu đồ.

## Ví dụ
Ví dụ sau đây sẽ tạo ra một biểu đồ đường đơn giản:
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
Ví dụ này sẽ tạo ra một biểu đồ đường với các giá trị x và y tương ứng. Chúng ta cũng có thể thêm tiêu đề, nhãn x và nhãn y cho biểu đồ.

## Bài tập
Bài tập sau đây sẽ giúp bạn rèn luyện kỹ năng sử dụng Matplotlib:
- Tạo một biểu đồ cột với các giá trị x = [1, 2, 3, 4, 5] và y = [2, 4, 6, 8, 10]
- Tạo một biểu đồ tròn với các giá trị [25, 25, 50]
- Tạo một biểu đồ phân tán với các giá trị x = [1, 2, 3, 4, 5] và y = [2, 4, 6, 8, 10]
Hãy thử nghiệm với các loại biểu đồ khác nhau và tùy chỉnh các tham số để tạo ra các biểu đồ độc đáo.