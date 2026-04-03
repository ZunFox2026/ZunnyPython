# Bài học số 27: Xử lý ngoại lệ (Exception Handling) trong Python

## Mục tiêu bài học
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Biết cách sử dụng khối `try-except` để bắt và xử lý lỗi.
- Sử dụng các khối `else` và `finally` một cách hợp lý.
- Áp dụng xử lý ngoại lệ trong các tình huống thực tế như đọc file, nhập liệu người dùng.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như chia cho 0, truy cập chỉ số vượt ngoài mảng, hoặc mở một file không tồn tại. Những lỗi này được gọi là **ngoại lệ** (exception).

Python cung cấp cơ chế **xử lý ngoại lệ** bằng câu lệnh `try-except`, giúp chương trình không bị dừng đột ngột khi có lỗi xảy ra.

### Cú pháp cơ bản:

```python
try:
    # Các lệnh có thể gây lỗi
    pass
except TênLỗi:
    # Xử lý lỗi nếu xảy ra
    pass
```

### Các khối bổ sung:
- `else`: Thực thi nếu không có ngoại lệ xảy ra.
- `finally`: Luôn thực thi, dù có lỗi hay không.

### Một số ngoại lệ phổ biến:
- `ZeroDivisionError`: Chia cho 0.
- `ValueError`: Giá trị không hợp lệ (ví dụ: chuyển chuỗi chữ sang số).
- `FileNotFoundError`: Không tìm thấy file.
- `IndexError`: Truy cập chỉ số ngoài danh sách.

### Ví dụ đơn giản:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
```

## Ví dụ minh họa

### Ví dụ 1: Xử lý nhập số từ người dùng

Người dùng có thể nhập sai định dạng, dẫn đến lỗi khi chuyển đổi sang số.

### Ví dụ 2: Đọc file an toàn

Khi mở file, có thể file không tồn tại. Cần xử lý lỗi để chương trình không crash.

### Ví dụ 3: Xử lý nhiều loại ngoại lệ

Sử dụng nhiều khối `except` để xử lý các lỗi khác nhau một cách riêng biệt.

## Bài tập thực hành

1. Viết hàm chia hai số, xử lý trường hợp chia cho 0.
2. Nhập danh sách số từ người dùng, xử lý khi nhập sai định dạng.
3. Đọc một file văn bản, in nội dung. Nếu file không tồn tại, in thông báo.
4. Viết chương trình tính căn bậc hai, xử lý khi số âm.
5. Xử lý lỗi khi truy cập phần tử trong danh sách.

## Tổng kết

Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình của bạn **ổn định** và **dễ bảo trì** hơn. Việc sử dụng `try-except-else-finally` hợp lý sẽ giúp bạn kiểm soát được các tình huống lỗi, cải thiện trải nghiệm người dùng và tránh crash chương trình.

Luôn nhớ:
- Không nên bỏ trống khối `except`.
- Cố gắng bắt các lỗi cụ thể thay vì dùng `except:` chung chung.
- Dùng `finally` để dọn dẹp tài nguyên (như đóng file, kết nối mạng...).
