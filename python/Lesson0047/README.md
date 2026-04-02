# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về các cách thức làm việc với tệp tin trong Python, bao gồm việc đọc, viết và chỉnh sửa tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ mở tệp tin và trả về một đối tượng tệp tin, cho phép bạn thực hiện các операции như đọc, viết và chỉnh sửa tệp tin.

Có ba chế độ mở tệp tin chính:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để viết, nếu tệp tin đã tồn tại thì sẽ bị xóa và tạo mới.
- `a`: Mở tệp tin để thêm nội dung vào cuối tệp tin.

Khi làm việc với tệp tin, bạn cần phải đóng tệp tin sau khi sử dụng xong bằng cách gọi phương thức `close()`.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với tệp tin trong Python:

- Đọc tệp tin:
```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

- Viết tệp tin:
```python
file = open('example.txt', 'w')
file.write('Xin chào thế giới!')
file.close()
```

- Thêm nội dung vào tệp tin:
```python
file = open('example.txt', 'a')
file.write('\nĐây là dòng thứ hai.')
file.close()
```

## Bài tập
Bài tập này sẽ giúp bạn thực hành làm việc với tệp tin trong Python. Hãy thực hiện các bước sau:

- Tạo một tệp tin mới có tên `bai_tap.txt`.
- Viết nội dung "Xin chào thế giới!" vào tệp tin `bai_tap.txt`.
- Đọc nội dung của tệp tin `bai_tap.txt` và in ra màn hình.
- Thêm nội dung "Đây là dòng thứ hai." vào cuối tệp tin `bai_tap.txt`.
- Đọc lại nội dung của tệp tin `bai_tap.txt` và in ra màn hình.

Hãy thử thực hiện các bước trên và xem kết quả. Nếu bạn gặp khó khăn, hãy tham khảo các ví dụ trong phần Lý thuyết và Ví dụ.