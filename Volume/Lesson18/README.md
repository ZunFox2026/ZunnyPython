# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, giúp bạn lưu trữ và truy xuất dữ liệu một cách hiệu quả. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm việc đọc, viết, và chỉnh sửa tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng các hàm built-in như `open()`, `read()`, `write()`, và `close()`. Hàm `open()` được sử dụng để mở tệp tin, trong khi hàm `read()` và `write()` được sử dụng để đọc và viết nội dung vào tệp tin. Khi bạn đã hoàn thành việc làm việc với tệp tin, bạn nên đóng tệp tin bằng hàm `close()` để giải phóng tài nguyên hệ thống.

Có ba chế độ mở tệp tin trong Python:

*   `r`: Mở tệp tin để đọc.
*   `w`: Mở tệp tin để viết. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa.
*   `a`: Mở tệp tin để追加 (thêm nội dung vào cuối tệp tin).

## Ví dụ
Dưới đây là một ví dụ minh họa cách làm việc với tệp tin trong Python:

```python
# Mở tệp tin để viết
f = open("example.txt", "w")

# Viết nội dung vào tệp tin
f.write("Xin chào, thế giới!")

# Đóng tệp tin
f.close()

# Mở tệp tin để đọc
f = open("example.txt", "r")

# Đọc nội dung từ tệp tin
content = f.read()

# In nội dung
print(content)

# Đóng tệp tin
f.close()
```

## Bài tập
Bài tập 1: Tạo một tệp tin có tên là `hello.txt` và viết nội dung "Xin chào, thế giới!" vào tệp tin đó.

Bài tập 2: Đọc nội dung từ tệp tin `hello.txt` và in nội dung ra màn hình.

Bài tập 3: Tạo một tệp tin có tên là `numbers.txt` và viết các số từ 1 đến 10 vào tệp tin đó, mỗi số trên một dòng.

Bài tập 4: Đọc nội dung từ tệp tin `numbers.txt` và tính tổng của các số trong tệp tin đó.

Bài tập 5: Tạo một tệp tin có tên là `students.txt` và viết thông tin của các sinh viên vào tệp tin đó, bao gồm tên, tuổi, và điểm trung bình. Sau đó, đọc nội dung từ tệp tin `students.txt` và in thông tin của các sinh viên ra màn hình.