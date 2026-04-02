# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong Python, việc làm việc với tệp được thực hiện thông qua các hàm và phương thức được cung cấp bởi ngôn ngữ. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong Python, bao gồm các loại tệp, cách mở và đọc tệp, cũng như cách viết và lưu trữ dữ liệu vào tệp.

## Lý thuyết
Trong Python, có hai loại tệp chính: tệp văn bản (text file) và tệp nhị phân (binary file). Tệp văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp nhị phân chứa dữ liệu dưới dạng nhị phân. Để làm việc với tệp, bạn cần sử dụng hàm `open()` để mở tệp, sau đó bạn có thể đọc hoặc viết dữ liệu vào tệp bằng cách sử dụng các phương thức như `read()`, `write()`, `readline()` và `writelines()`. Khi hoàn thành, bạn cần sử dụng phương thức `close()` để đóng tệp.

Ví dụ về các chế độ mở tệp:
- `r`: Mở tệp để đọc (read)
- `w`: Mở tệp để viết (write), nếu tệp đã tồn tại thì sẽ bị xóa
- `a`: Mở tệp để thêm (append) vào cuối tệp
- `r+`: Mở tệp để đọc và viết
- `w+`: Mở tệp để đọc và viết, nếu tệp đã tồn tại thì sẽ bị xóa
- `a+`: Mở tệp để đọc và thêm vào cuối tệp

## Ví dụ
Dưới đây là một số ví dụ cơ bản về làm việc với tệp trong Python:
```python
# Mở tệp để đọc
f = open("test.txt", "r")
content = f.read()
print(content)
f.close()

# Mở tệp để viết
f = open("test.txt", "w")
f.write("Xin chào, thế giới!")
f.close()

# Mở tệp để thêm
f = open("test.txt", "a")
f.write(" Đây là một dòng mới.")
f.close()
```
Lưu ý rằng trong Python, bạn có thể sử dụng khối `with` để mở tệp, giúp tự động đóng tệp khi hoàn thành:
```python
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```

## Bài tập
Bài tập này yêu cầu bạn thực hiện các nhiệm vụ sau:
- Tạo một tệp tin mới có tên "gioithieu.txt" và viết vào đó một đoạn văn giới thiệu về bản thân.
- Đọc nội dung của tệp "gioithieu.txt" và in nó ra màn hình.
- Thêm một dòng mới vào cuối tệp "gioithieu.txt" với nội dung "Xin chào, mọi người!".
- Đọc lại nội dung của tệp "gioithieu.txt" và in nó ra màn hình để kiểm tra kết quả.