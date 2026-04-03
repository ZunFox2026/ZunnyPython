# Bài học Python nâng cao số 81: Context Managers và Quản lý Tài nguyên

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của context managers trong Python.
- Biết cách sử dụng `with` để quản lý tài nguyên một cách an toàn.
- Tự tạo context manager bằng class và decorator `@contextmanager`.
- Ứng dụng context managers trong các tình huống thực tế như xử lý file, kết nối cơ sở dữ liệu, đo thời gian thực thi.

## Lý thuyết chi tiết

### 1. Context Manager là gì?
Context manager là một đối tượng định nghĩa cách chiếm hữu và giải phóng tài nguyên. Nó giúp đảm bảo rằng tài nguyên (như file, kết nối mạng, khóa…) được sử dụng và giải phóng đúng cách, kể cả khi xảy ra lỗi.

Cú pháp phổ biến là dùng với từ khóa `with`:
```python
with context_manager:
    # Làm việc với tài nguyên
```

Khi khối `with` kết thúc (bất kể có exception hay không), context manager sẽ tự động giải phóng tài nguyên.

### 2. Giao diện Context Manager
Một context manager phải triển khai hai phương thức:
- `__enter__(self)`: Được gọi khi bắt đầu khối `with`. Trả về tài nguyên cần sử dụng.
- `__exit__(self, exc_type, exc_value, traceback)`: Được gọi khi khối `with` kết thúc. Dùng để dọn dẹp tài nguyên, và có thể xử lý exception nếu cần.

### 3. Tạo Context Manager bằng Class
Bạn có thể tạo context manager bằng cách định nghĩa class với hai phương thức trên.

### 4. Tạo Context Manager bằng @contextmanager
Từ module `contextlib`, decorator `@contextmanager` cho phép bạn tạo context manager từ một hàm generator. Câu lệnh trước `yield` tương đương `__enter__`, sau `yield` tương đương `__exit__`.

### 5. Ví dụ cơ bản: Mở file
```python
with open('file.txt', 'r') as f:
    data = f.read()
# File tự động đóng dù có lỗi hay không
```

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi
Tạo context manager để đo thời gian thực hiện một khối lệnh.

### Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
Tạo context manager mô phỏng việc mở và đóng kết nối CSDL.

### Ví dụ 3: Tạm thời thay đổi thư mục làm việc
Tạo context manager để tạm thời chuyển thư mục, sau đó quay lại.

## Bài tập thực hành
1. Viết context manager `SuppressErrors` để bỏ qua các exception nhất định.
2. Tạo context manager `Timer` để ghi log thời gian thực thi vào file.
3. Xây dựng context manager `ReadOnlyFile` để mở file chỉ đọc và đảm bảo không bị ghi đè.
4. Viết context manager `ChangeDir` để thay đổi thư mục làm việc an toàn.
5. Tạo context manager dùng `@contextmanager` để in ra thông báo khi bắt đầu và kết thúc khối lệnh.

## Tổng kết
Context managers là công cụ mạnh mẽ giúp quản lý tài nguyên một cách sạch sẽ, an toàn và dễ đọc. Việc sử dụng `with` không chỉ ngăn lỗi rò rỉ tài nguyên mà còn giúp code rõ ràng hơn. Ở cấp độ nâng cao, việc tự định nghĩa context manager cho các tình huống cụ thể là kỹ năng quan trọng trong xây dựng thư viện và ứng dụng lớn.
