# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện matplotlib để tạo ra các biểu đồ cơ bản.

Matplotlib cung cấp nhiều tính năng như tạo biểu đồ 2D, 3D, histogram, scatter plot, v.v. Ngoài ra, thư viện này cũng hỗ trợ nhiều định dạng hình ảnh khác nhau như PNG, PDF, EPS, v.v.

## Lý thuyết
Để bắt đầu sử dụng matplotlib, chúng ta cần import thư viện này vào chương trình Python của mình. Chúng ta có thể làm điều này bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`.

Sau khi import, chúng ta có thể sử dụng các hàm trong matplotlib để tạo ra các biểu đồ. Ví dụ, để tạo ra một biểu đồ đường thẳng, chúng ta có thể sử dụng hàm `plt.plot()`. Hàm này nhận vào hai tham số là danh sách các giá trị x và danh sách các giá trị y.

Ngoài ra, chúng ta cũng có thể tùy chỉnh các thuộc tính của biểu đồ như màu sắc, kích thước, tiêu đề, v.v. bằng cách sử dụng các hàm như `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường thẳng:
```plain
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường thẳng')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
Khi chạy chương trình này, chúng ta sẽ thấy một biểu đồ đường thẳng với tiêu đề "Biểu đồ đường thẳng" và các nhãn x, y.

## Bài tập
Bài tập 1: Tạo ra một biểu đồ histogram để thể hiện phân bố của các giá trị trong danh sách `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]`.

Bài tập 2: Tạo ra một biểu đồ scatter plot để thể hiện mối quan hệ giữa hai danh sách `[1, 2, 3, 4, 5]` và `[2, 4, 6, 8, 10]`.

Bài tập 3: Tạo ra một biểu đồ đường thẳng để thể hiện sự thay đổi của giá trị y theo giá trị x trong phương trình y = 2x + 1.