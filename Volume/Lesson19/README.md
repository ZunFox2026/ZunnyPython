# Làm việc với tệp tin
## Giới thiệu
Bài học này sẽ hướng dẫn bạn cách làm việc với tệp tin trong Python. Tệp tin là nơi lưu trữ dữ liệu trên máy tính, và Python cung cấp nhiều cách để đọc và ghi dữ liệu vào tệp tin. Đây là một kỹ năng quan trọng trong lập trình, vì nó cho phép bạn lưu trữ và xử lý dữ liệu một cách hiệu quả.

## Lý thuyết
Để làm việc với tệp tin, bạn cần hiểu về các khái niệm sau:
- **Mở tệp tin**: Trước khi đọc hoặc ghi dữ liệu vào tệp tin, bạn cần mở nó bằng hàm `open()`. Hàm này trả về một đối tượng tệp tin, mà bạn có thể sử dụng để đọc hoặc ghi dữ liệu.
- **Đọc tệp tin**: Bạn có thể đọc dữ liệu từ tệp tin bằng các phương thức như `read()`, `readline()`, hoặc `readlines()`.
- **Ghi tệp tin**: Bạn có thể ghi dữ liệu vào tệp tin bằng các phương thức như `write()` hoặc `writelines()`.
- **Đóng tệp tin**: Sau khi xong việc với tệp tin, bạn nên đóng nó bằng phương thức `close()` để giải phóng tài nguyên hệ thống.

Ví dụ về cách mở và đóng tệp tin:
```python
file = open("example.txt", "r")
# Đọc hoặc ghi dữ liệu vào tệp tin
file.close()
```

## Ví dụ
Dưới đây là một ví dụ cụ thể về cách đọc và ghi dữ liệu vào tệp tin:
```python
# Mở tệp tin để ghi dữ liệu
file = open("example.txt", "w")
file.write("Xin chào, thế giới!")
file.close()

# Mở tệp tin để đọc dữ liệu
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

## Bài tập
Để luyện tập kỹ năng làm việc với tệp tin, bạn có thể thực hiện các bài tập sau:
- Tạo một tệp tin mới và ghi dữ liệu vào đó.
- Đọc dữ liệu từ tệp tin và in ra màn hình.
- Tạo một chương trình cho phép người dùng nhập dữ liệu và lưu trữ vào tệp tin.
- Đọc dữ liệu từ tệp tin và hiển thị ra màn hình theo định dạng cụ thể.

Hãy nhớ luôn đóng tệp tin sau khi xong việc để tránh lãng phí tài nguyên hệ thống. Chúc bạn thành công trong việc làm việc với tệp tin trong Python!