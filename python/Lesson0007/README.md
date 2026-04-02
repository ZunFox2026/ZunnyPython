# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu cách đọc và ghi dữ liệu vào tệp trong Python. Việc này cho phép chúng ta lưu trữ dữ liệu lâu dài và đọc lại khi cần thiết.

## Lý thuyết
Để làm việc với tệp trong Python, chúng ta cần sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp, cho phép chúng ta thực hiện các thao tác như đọc, ghi, thêm vào tệp.

- `open('tên_tệp', 'chế_độ')`: Mở tệp với chế độ cụ thể.
  - `'r'`: Mở tệp để đọc.
  - `'w'`: Mở tệp để ghi, nếu tệp đã tồn tại thì nội dung sẽ bị xóa.
  - `'a'`: Mở tệp để thêm vào cuối tệp.
  - `'x'`: Tạo tệp mới để ghi, nếu tệp đã tồn tại thì sẽ trả về lỗi.

Ví dụ về mở tệp để đọc:
```python
f = open('example.txt', 'r')
noidung = f.read()
print(noidung)
f.close()
```

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với tệp:

- Đọc nội dung tệp:
  ```python
  f = open('example.txt', 'r')
  content = f.read()
  print(content)
  f.close()
  ```
- Ghi dữ liệu vào tệp:
  ```python
  f = open('example.txt', 'w')
  f.write('Xin chào thế giới!')
  f.close()
  ```
- Thêm dữ liệu vào cuối tệp:
  ```python
  f = open('example.txt', 'a')
  f.write('\nThế giới lập trình!')
  f.close()
  ```

## Bài tập
Để thực hành kỹ năng làm việc với tệp, bạn có thể thực hiện các bài tập sau:

1. Tạo một tệp văn bản mới và ghi vào đó một đoạn văn ngắn.
2. Đọc nội dung của tệp vừa tạo và in ra màn hình.
3. Thêm một đoạn văn mới vào cuối tệp.
4. Đọc lại nội dung của tệp và so sánh với nội dung trước khi thêm.

Bài tập này sẽ giúp bạn nắm vững cách sử dụng hàm `open()` và các chế độ mở tệp khác nhau trong Python. Hãy bắt đầu thực hành để trở thành chuyên gia trong việc làm việc với tệp!