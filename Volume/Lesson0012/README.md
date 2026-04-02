# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu cách đọc, ghi và xử lý tệp tin trong Python. Đây là một chủ đề cơ bản nhưng rất quan trọng, vì nó cho phép chúng ta lưu trữ và xử lý dữ liệu một cách hiệu quả.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng các hàm như `open()`, `read()`, `write()`, và `close()`. Hàm `open()` được sử dụng để mở một tệp tin, và nó trả về một đối tượng tệp tin. Chúng ta có thể sử dụng đối tượng này để đọc hoặc ghi dữ liệu vào tệp tin.

Có nhiều chế độ mở tệp tin khác nhau, bao gồm:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nó sẽ bị xóa và thay thế bằng một tệp tin mới.
- `a`: Mở tệp tin để thêm dữ liệu vào cuối tệp tin.
- `r+`: Mở tệp tin để đọc và ghi.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi tệp tin trong Python:
```python
# Mở tệp tin để ghi
f = open("example.txt", "w")
# Ghi dữ liệu vào tệp tin
f.write("Xin chào, thế giới!")
# Đóng tệp tin
f.close()

# Mở tệp tin để đọc
f = open("example.txt", "r")
# Đọc dữ liệu từ tệp tin
data = f.read()
# In dữ liệu
print(data)
# Đóng tệp tin
f.close()
```
Trong ví dụ này, chúng ta mở một tệp tin tên là `example.txt` để ghi, sau đó ghi dữ liệu vào tệp tin. Sau đó, chúng ta mở lại tệp tin để đọc và in dữ liệu.

## Bài tập
Để thực hành làm việc với tệp tin, bạn có thể thực hiện các bài tập sau:
- Tạo một tệp tin tên là `hello.txt` và ghi dữ liệu "Xin chào, thế giới!" vào tệp tin.
- Đọc dữ liệu từ tệp tin `hello.txt` và in nó ra màn hình.
- Tạo một tệp tin tên là `numbers.txt` và ghi các số từ 1 đến 10 vào tệp tin.
- Đọc dữ liệu từ tệp tin `numbers.txt` và tính tổng của các số trong tệp tin.

Bằng cách thực hành các bài tập này, bạn sẽ có thể hiểu rõ hơn về cách làm việc với tệp tin trong Python và áp dụng kỹ năng này vào các dự án thực tế.