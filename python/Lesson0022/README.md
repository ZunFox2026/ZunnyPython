# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ tệp. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp trong Python, bao gồm cả việc đọc và viết tệp.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp bằng cách sử dụng các hàm như `open()`, `read()`, `write()` và `close()`. Hàm `open()` được sử dụng để mở tệp, hàm `read()` được sử dụng để đọc nội dung của tệp, hàm `write()` được sử dụng để viết dữ liệu vào tệp và hàm `close()` được sử dụng để đóng tệp.

Có nhiều chế độ mở tệp khác nhau, bao gồm:
- `r`: Mở tệp để đọc
- `w`: Mở tệp để viết, nếu tệp đã tồn tại thì sẽ bị xóa
- `a`: Mở tệp để thêm nội dung vào cuối tệp
- `r+`: Mở tệp để đọc và viết

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với tệp:
- Đọc tệp:
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```
- Viết tệp:
```python
file = open("example.txt", "w")
file.write("Xin chào!")
file.close()
```
- Thêm nội dung vào tệp:
```python
file = open("example.txt", "a")
file.write(" Đây là nội dung thêm vào!")
file.close()
```
Lưu ý rằng sau khi xong việc với tệp, chúng ta nên đóng tệp bằng hàm `close()` để giải phóng tài nguyên.

## Bài tập
Để rèn luyện kỹ năng làm việc với tệp, bạn có thể thực hiện các bài tập sau:
- Tạo một tệp mới và viết nội dung vào tệp đó
- Đọc nội dung của tệp và in ra màn hình
- Thêm nội dung vào tệp đã có
- Tạo một chương trình cho phép người dùng nhập nội dung và lưu vào tệp

Hy vọng qua bài này, bạn đã hiểu được cách làm việc với tệp trong Python và có thể áp dụng vào các dự án thực tế.