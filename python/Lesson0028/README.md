# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, giúp bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm việc mở, đọc, viết và đóng tệp tin.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp tin, cho phép bạn thực hiện các hoạt động như đọc, viết và đóng tệp tin. Cú pháp của hàm `open()` như sau:
```python
tệp_tin = open('tên_tệp_tin', 'chế_độ')
```
Trong đó, `'tên_tệp_tin'` là tên của tệp tin bạn muốn mở, và `'chế_độ'` là chế độ mở tệp tin. Có các chế độ sau:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để viết. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa.
- `a`: Mở tệp tin để viết tiếp. Nếu tệp tin đã tồn tại, nội dung mới sẽ được thêm vào cuối tệp tin.
- `x`: Mở tệp tin để tạo mới. Nếu tệp tin đã tồn tại, sẽ发生 lỗi.

Sau khi mở tệp tin, bạn có thể sử dụng các phương thức như `read()`, `write()`, `close()` để đọc, viết và đóng tệp tin.

## Ví dụ
Ví dụ sau minh họa cách mở, viết và đóng tệp tin:
```python
# Mở tệp tin để viết
tệp_tin = open('example.txt', 'w')

# Viết nội dung vào tệp tin
tệp_tin.write('Xin chào, thế giới!')

# Đóng tệp tin
tệp_tin.close()
```
Ví dụ sau minh họa cách mở, đọc và đóng tệp tin:
```python
# Mở tệp tin để đọc
tệp_tin = open('example.txt', 'r')

# Đọc nội dung từ tệp tin
nội_dung = tệp_tin.read()

# In nội dung
print(nội_dung)

# Đóng tệp tin
tệp_tin.close()
```
## Bài tập
Bài tập sau yêu cầu bạn thực hiện các hoạt động sau:
- Tạo một tệp tin mới có tên `my_file.txt`.
- Viết nội dung `Xin chào, thế giới!` vào tệp tin.
- Đọc nội dung từ tệp tin và in ra màn hình.
- Đóng tệp tin.

Hãy thử thực hiện bài tập trên và xem kết quả!