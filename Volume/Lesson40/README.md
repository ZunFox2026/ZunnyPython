# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng khi lập trình. Trong bài học này, chúng ta sẽ tìm hiểu cách đọc và ghi tệp tin trong Python. Đây là một chủ đề cơ bản nhưng rất quan trọng, vì nó cho phép chúng ta lưu trữ và tải dữ liệu từ tệp tin.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp tin, mà chúng ta có thể sử dụng để đọc và ghi dữ liệu. Có ba chế độ mở tệp tin:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nội dung của nó sẽ bị xóa.
- `a`: Mở tệp tin để ghi thêm. Nếu tệp tin đã tồn tại, dữ liệu mới sẽ được thêm vào cuối tệp tin.

Chúng ta cũng có thể sử dụng các phương thức của đối tượng tệp tin để đọc và ghi dữ liệu, chẳng hạn như `read()`, `write()`, `readline()`, `writelines()`.

## Ví dụ
Ví dụ sau đây minh họa cách mở và đọc một tệp tin:
```python
# Mở tệp tin để đọc
file = open("example.txt", "r")

# Đọc nội dung của tệp tin
content = file.read()

# In nội dung của tệp tin
print(content)

# Đóng tệp tin
file.close()
```
Ví dụ sau đây minh họa cách mở và ghi một tệp tin:
```python
# Mở tệp tin để ghi
file = open("example.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()
```
## Bài tập
Bài tập sau đây yêu cầu bạn thực hiện các bước sau:
- Tạo một tệp tin mới có tên là `demo.txt`.
- Ghi nội dung `"Xin chào, thế giới!"` vào tệp tin `demo.txt`.
- Đọc nội dung của tệp tin `demo.txt` và in nó ra màn hình.
- Thêm nội dung `"Đây là một tệp tin demo."` vào cuối tệp tin `demo.txt`.
- Đọc lại nội dung của tệp tin `demo.txt` và in nó ra màn hình.

Hãy cố gắng giải quyết bài tập này bằng cách sử dụng các kỹ năng bạn đã học được trong bài học này. Nếu bạn gặp khó khăn, hãy tham khảo các ví dụ trên để có thêm minh họa.