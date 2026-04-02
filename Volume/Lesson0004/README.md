# Làm quen với thư viện Matplotlib
## Giới thiệu
Thư viện Matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh từ dữ liệu. Với Matplotlib, bạn có thể tạo ra nhiều loại biểu đồ khác nhau, từ biểu đồ đơn giản như biểu đồ đường, biểu đồ cột, đến các biểu đồ phức tạp hơn như biểu đồ 3D, biểu đồ phân tán. Trong bài viết này, chúng ta sẽ tìm hiểu cách làm quen với thư viện Matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Trước khi bắt đầu sử dụng Matplotlib, bạn cần hiểu một số khái niệm cơ bản về thư viện này. Matplotlib cung cấp hai loại biểu đồ chính: biểu đồ 2D và biểu đồ 3D. Biểu đồ 2D được sử dụng để thể hiện dữ liệu trên một mặt phẳng, trong khi biểu đồ 3D được sử dụng để thể hiện dữ liệu trong không gian ba chiều. Ngoài ra, Matplotlib cũng cung cấp nhiều loại biểu đồ khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, biểu đồ phân tán, v.v. Để sử dụng Matplotlib, bạn cần nhập thư viện này vào chương trình Python của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`.

## Ví dụ
Để minh họa cách sử dụng Matplotlib, hãy xem xét ví dụ sau:
Giả sử chúng ta muốn tạo ra một biểu đồ đường thể hiện sự thay đổi của nhiệt độ trong một ngày. Chúng ta có thể sử dụng dữ liệu sau:
- 8h: 20 độ
- 12h: 25 độ
- 16h: 28 độ
- 20h: 22 độ
Chúng ta có thể sử dụng Matplotlib để tạo ra biểu đồ đường như sau:
```python
import matplotlib.pyplot as plt

# Dữ liệu
gio = [8, 12, 16, 20]
nhiet_do = [20, 25, 28, 22]

# Tạo biểu đồ
plt.plot(gio, nhiet_do)
plt.xlabel('Giờ')
plt.ylabel('Nhiệt độ (độ)')
plt.title('Biểu đồ nhiệt độ')
plt.show()
```
Khi chạy chương trình này, chúng ta sẽ thấy một biểu đồ đường thể hiện sự thay đổi của nhiệt độ trong một ngày.

## Bài tập
Để练习 sử dụng Matplotlib, bạn có thể thực hiện các bài tập sau:
- Tạo ra một biểu đồ cột thể hiện số lượng sản phẩm bán được trong một tuần.
- Tạo ra một biểu đồ tròn thể hiện tỷ lệ doanh thu của các sản phẩm khác nhau.
- Tạo ra một biểu đồ phân tán thể hiện mối quan hệ giữa giá cả và chất lượng của các sản phẩm.
Với những bài tập này, bạn sẽ có thể nắm vững cách sử dụng Matplotlib để tạo ra các biểu đồ khác nhau và áp dụng nó vào các dự án thực tế.