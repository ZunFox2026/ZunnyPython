# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp trong Python, bao gồm cả việc đọc và viết tệp.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp bằng cách sử dụng hàm `open()`. Hàm này sẽ mở một tệp và trả về một đối tượng tệp. Bạn có thể sử dụng đối tượng này để đọc hoặc viết dữ liệu vào tệp. Có nhiều chế độ mở tệp khác nhau, bao gồm:
- `r`: Mở tệp để đọc
- `w`: Mở tệp để viết, nếu tệp đã tồn tại thì sẽ bị xóa
- `a`: Mở tệp để thêm dữ liệu vào cuối tệp
- `r+`: Mở tệp để đọc và viết
- `w+`: Mở tệp để đọc và viết, nếu tệp đã tồn tại thì sẽ bị xóa
- `a+`: Mở tệp để đọc và thêm dữ liệu vào cuối tệp

Khi bạn mở một tệp, bạn cần đảm bảo rằng tệp đó đã được đóng lại khi bạn xong việc với nó. Bạn có thể sử dụng hàm `close()` để đóng tệp.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và viết tệp:
```python
# Mở tệp để viết
f = open("test.txt", "w")
f.write("Xin chào, thế giới!")
f.close()

# Mở tệp để đọc
f = open("test.txt", "r")
print(f.read())
f.close()
```
Trong ví dụ này, chúng ta mở tệp `test.txt` để viết, sau đó viết chuỗi "Xin chào, thế giới!" vào tệp. Sau đó, chúng ta mở lại tệp để đọc và in nội dung của tệp.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python để tạo một tệp tin mới, sau đó viết một số dữ liệu vào tệp đó. Sau đó, hãy đọc lại dữ liệu từ tệp và in nó ra màn hình.
- Tạo một tệp tin mới có tên là `data.txt`
- Viết các số từ 1 đến 10 vào tệp `data.txt`
- Đọc lại nội dung của tệp `data.txt` và in nó ra màn hình
- Đóng tệp lại khi xong việc

Hãy thử viết chương trình này và chạy nó để xem kết quả!