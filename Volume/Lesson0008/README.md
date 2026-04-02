# Làm việc với tệp
Bài này sẽ hướng dẫn bạn cách làm việc với tệp trong Python, bao gồm đọc, ghi, và xử lý tệp.

## Giới thiệu
Trong chương trình Python, bạn thường cần đọc và ghi dữ liệu từ tệp. Tệp có thể là tệp văn bản, tệp hình ảnh, tệp âm thanh, v.v. Python cung cấp nhiều hàm và phương thức để làm việc với tệp, giúp bạn dễ dàng đọc, ghi, và xử lý dữ liệu.

## Lý thuyết
Để làm việc với tệp, bạn cần mở tệp trước. Hàm `open()` được sử dụng để mở tệp. Hàm này trả về một đối tượng tệp, mà bạn có thể sử dụng để đọc và ghi dữ liệu.

Có nhiều chế độ mở tệp, bao gồm:
- `r`: Mở tệp để đọc.
- `w`: Mở tệp để ghi. Nếu tệp đã tồn tại, nội dung sẽ bị xóa.
- `a`: Mở tệp để thêm dữ liệu vào cuối tệp.
- `r+`: Mở tệp để đọc và ghi.
- `w+`: Mở tệp để đọc và ghi. Nếu tệp đã tồn tại, nội dung sẽ bị xóa.

Khi bạn mở tệp, bạn cần nhớ đóng tệp lại sau khi sử dụng xong. Hàm `close()` được sử dụng để đóng tệp.

## Ví dụ
Ví dụ sau minh họa cách mở tệp, đọc dữ liệu, và ghi dữ liệu:
```python
# Mở tệp để đọc
f = open('test.txt', 'r')
# Đọc nội dung tệp
content = f.read()
print(content)
# Đóng tệp
f.close()

# Mở tệp để ghi
f = open('test.txt', 'w')
# Ghi nội dung vào tệp
f.write('Xin chào, thế giới!')
# Đóng tệp
f.close()

# Mở tệp để đọc và ghi
f = open('test.txt', 'r+')
# Đọc nội dung tệp
content = f.read()
print(content)
# Ghi nội dung vào tệp
f.write(' Đây là nội dung mới.')
# Đóng tệp
f.close()
```
## Bài tập
Bài tập sau sẽ giúp bạn thực hành làm việc với tệp:
- Tạo một tệp văn bản mới và ghi nội dung vào tệp.
- Đọc nội dung từ tệp và in ra màn hình.
- Thêm nội dung vào cuối tệp.
- Đọc và ghi dữ liệu vào tệp bằng chế độ `r+`.
- Tìm hiểu và sử dụng các hàm khác như `readline()`, `readlines()`, `write()`, `writelines()`.