# Bài học Python Nâng cao - Bài 48: Thiết kế và sử dụng Context Manager (Quản lý ngữ cảnh)

## Mục tiêu bài học
- Hiểu rõ khái niệm **Context Manager** trong Python.
- Biết cách sử dụng `with` để quản lý tài nguyên một cách an toàn.
- Tự tạo Context Manager bằng cách sử dụng **class** và **decorator `@contextmanager`**.
- Ứng dụng Context Manager trong xử lý file, kết nối cơ sở dữ liệu, và các tình huống cần dọn dẹp tài nguyên.

## Lý thuyết chi tiết

### 1. Context Manager là gì?

Context Manager (Quản lý ngữ cảnh) là một cơ chế trong Python cho phép bạn phân bổ và giải phóng tài nguyên một cách chính xác. Cú pháp phổ biến nhất là dùng với lệnh `with`.

Ví dụ:
```python
with open('file.txt', 'r') as f:
    data = f.read()
# Tệp tự động đóng sau khi ra khỏi khối `with`
```

Lợi ích:
- Đảm bảo tài nguyên luôn được giải phóng (ngay cả khi có lỗi xảy ra).
- Code sạch hơn, dễ đọc hơn.

### 2. Cấu trúc của Context Manager

Một Context Manager cần định nghĩa hai phương thức:
- `__enter__`: được gọi khi vào khối `with`, trả về tài nguyên.
- `__exit__`: được gọi khi thoát khỏi khối `with`, dù có lỗi hay không. Dùng để dọn dẹp.

### 3. Tạo Context Manager bằng class

```python
class MyContext:
    def __enter__(self):
        print("Bắt đầu ngữ cảnh")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Kết thúc ngữ cảnh")
        if exc_type:
            print(f"Lỗi: {exc_value}")
        return False  # Không xử lý lỗi, để lỗi nổi lên
```

### 4. Tạo Context Manager bằng decorator `@contextmanager`

Sử dụng từ module `contextlib`:

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Bắt đầu")
    try:
        yield "dữ liệu"
    finally:
        print("Kết thúc")
```

## Ví dụ minh họa

### Ví dụ 1: Quản lý tệp tin

Tự tạo Context Manager để đọc và ghi file an toàn.

### Ví dụ 2: Đo thời gian thực thi

Tạo Context Manager để đo thời gian chạy của một đoạn code.

### Ví dụ 3: Quản lý kết nối cơ sở dữ liệu giả lập

Tạo Context Manager mô phỏng việc kết nối và đóng kết nối DB.

## Bài tập thực hành

1. Viết Context Manager để tạm thời thay đổi thư mục làm việc.
2. Viết Context Manager để đếm số lần gọi một hàm trong một khối code.
3. Viết Context Manager để tắt/bật logging trong một khối code.
4. Viết Context Manager dùng `@contextmanager` để tạo file tạm và tự xóa sau khi dùng xong.
5. Viết Context Manager để giới hạn thời gian thực thi một khối code (timeout giả lập).

## Tổng kết

- Context Manager giúp quản lý tài nguyên hiệu quả và an toàn.
- Có thể tạo bằng class hoặc dùng `@contextmanager`.
- Rất hữu ích trong xử lý file, DB, đo hiệu năng, và các tác vụ cần dọn dẹp.
- Nên sử dụng `with` thay vì tự động `open/close`, `connect/disconnect` để tránh rò rỉ tài nguyên.
