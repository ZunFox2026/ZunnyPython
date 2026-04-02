# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện nổi tiếng và được sử dụng rộng rãi trong lĩnh vực phân tích dữ liệu và tạo biểu đồ trong Python. Với matplotlib, bạn có thể tạo ra các biểu đồ 2D và 3D với nhiều tính năng tùy chỉnh khác nhau. Bài viết này sẽ giới thiệu về cách sử dụng thư viện matplotlib để tạo biểu đồ và phân tích dữ liệu.

## Lý thuyết
Thư viện matplotlib cung cấp nhiều tính năng để tạo biểu đồ, bao gồm:
- Biểu đồ đường (line plot)
- Biểu đồ cột (bar plot)
- Biểu đồ tròn (pie chart)
- Biểu đồ phân tán (scatter plot)
- Biểu đồ 3D

Để sử dụng matplotlib, bạn cần nhập thư viện vào chương trình Python của mình bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm trong thư viện để tạo biểu đồ.

## Ví dụ
Ví dụ dưới đây sẽ tạo một biểu đồ đường đơn giản:
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
Kết quả sẽ là một biểu đồ đường với tiêu đề "Biểu đồ đường" và hai trục x, y.

## Bài tập
Bài tập dưới đây sẽ giúp bạn làm quen với thư viện matplotlib:
- Tạo một biểu đồ cột với 5 cột, mỗi cột đại diện cho một ngày trong tuần (thứ 2, thứ 3, thứ 4, thứ 5, thứ 6).
- Tạo một biểu đồ tròn với 4 phần, mỗi phần đại diện cho một mùa trong năm (mùa xuân, mùa hạ, mùa thu, mùa đông).
- Tạo một biểu đồ phân tán với 10 điểm, mỗi điểm đại diện cho một thành phố trên bản đồ.

Hãy thử nghiệm với các hàm và tính năng khác nhau của thư viện matplotlib để tạo ra các biểu đồ khác nhau và phân tích dữ liệu của mình.