# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và ghi dữ liệu.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp tin, cho phép bạn thực hiện các hoạt động như đọc, ghi, và đóng tệp tin. Có hai chế độ chính khi làm việc với tệp tin: chế độ đọc (`'r'`) và chế độ ghi (`'w'`). Ngoài ra, bạn cũng có thể sử dụng chế độ đọc và ghi (`'r+'`), hoặc chế độ追加 (`'a'`).

Khi mở một tệp tin, bạn cần chỉ định đường dẫn đến tệp tin và chế độ mở. Ví dụ:
```python
file = open('example.txt', 'r')
```
Sau khi mở tệp tin, bạn có thể sử dụng các phương thức như `read()`, `write()`, và `close()` để thực hiện các hoạt động trên tệp tin.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi dữ liệu vào một tệp tin:
```python
# Mở tệp tin ở chế độ đọc
file = open('example.txt', 'r')
# Đọc nội dung của tệp tin
content = file.read()
print(content)
# Đóng tệp tin
file.close()

# Mở tệp tin ở chế độ ghi
file = open('example.txt', 'w')
# Ghi dữ liệu vào tệp tin
file.write('Xin chào, thế giới!')
# Đóng tệp tin
file.close()
```
Trong ví dụ trên, chúng ta mở tệp tin `example.txt` ở chế độ đọc, đọc nội dung của tệp tin, và in ra màn hình. Sau đó, chúng ta mở lại tệp tin ở chế độ ghi, ghi dữ liệu vào tệp tin, và đóng tệp tin.

## Bài tập
Bài tập 1: Tạo một tệp tin mới có tên `hello.txt` và ghi nội dung "Xin chào, thế giới!" vào tệp tin đó.
Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.
Bài tập 3: Tạo một tệp tin mới có tên `numbers.txt` và ghi các số từ 1 đến 10 vào tệp tin đó, mỗi số trên một dòng.
Bài tập 4: Đọc nội dung của tệp tin `numbers.txt` và tính tổng của các số trong tệp tin.