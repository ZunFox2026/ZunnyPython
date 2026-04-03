# Bài học Python số 37 - Cấp độ Trung cấp

## Chủ đề: **Xử lý ngoại lệ (Exception Handling) nâng cao và tạo ngoại lệ tùy chỉnh**

Trong bài học này, chúng ta sẽ đi sâu vào cách xử lý các lỗi (exception) trong Python một cách chuyên nghiệp hơn. Bạn sẽ học cách bắt nhiều loại ngoại lệ, sử dụng khối `else` và `finally`, cũng như tự tạo các loại ngoại lệ riêng phù hợp với ứng dụng của mình.

### ✅ Mục tiêu bài học
- Hiểu rõ cách xử lý nhiều loại ngoại lệ khác nhau.
- Biết sử dụng các khối `else` và `finally` trong câu lệnh `try-except`.
- Tự tạo và sử dụng các lớp ngoại lệ tùy chỉnh.
- Ứng dụng xử lý ngoại lệ trong các tình huống thực tế như đọc file, tính toán, và nhập liệu người dùng.

### 📘 Lý thuyết chi tiết

#### 1. Câu lệnh `try-except` nâng cao

Cú pháp cơ bản:
```python
try:
    # Đoạn mã có thể gây lỗi
    pass
except LoaiException as bien:
    # Xử lý lỗi cụ thể
    pass
except Exception as e:
    # Xử lý các lỗi còn lại
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

- `except` có thể bắt nhiều loại ngoại lệ.
- `else`: chỉ chạy khi **không có ngoại lệ nào xảy ra**.
- `finally`: luôn chạy, thường dùng để dọn dẹp tài nguyên (đóng file, kết nối mạng, v.v.).

#### 2. Tạo ngoại lệ tùy chỉnh

Bạn có thể tạo lớp ngoại lệ riêng bằng cách kế thừa từ `Exception`:
```python
class MyCustomError(Exception):
    def __init__(self, message="Lỗi tùy chỉnh"):
        self.message = message
        super().__init__(self.message)
```

Sau đó dùng `raise MyCustomError("Chi tiết lỗi")` để phát sinh lỗi.

### 🖼️ Ví dụ minh họa

**Ví dụ 1: Đọc file và xử lý các lỗi có thể xảy ra**
- Xử lý `FileNotFoundError`, `PermissionError`, và lỗi chung.

**Ví dụ 2: Tính chia hai số với kiểm tra đầu vào và ngoại lệ tùy chỉnh**
- Tạo `InvalidInputError` nếu người dùng nhập sai.

**Ví dụ 3: Quản lý tài khoản ngân hàng với ngoại lệ tùy chỉnh**
- Tạo `InsufficientFundsError` khi rút tiền vượt số dư.

### 📝 Bài tập thực hành
1. Viết hàm chia hai số với xử lý đầy đủ ngoại lệ và thông báo chi tiết.
2. Viết chương trình đọc danh sách số từ file, xử lý lỗi định dạng.
3. Tạo lớp `Student` với phương thức thêm điểm, ném ngoại lệ nếu điểm không hợp lệ.
4. Viết hàm mở file và đảm bảo luôn đóng file bằng `finally`.
5. Tạo ngoại lệ `AgeLimitError` và kiểm tra độ tuổi đăng ký.

### 🧠 Tổng kết
Xử lý ngoại lệ là kỹ năng cần thiết để viết chương trình ổn định và dễ bảo trì. Việc sử dụng `try-except-else-finally` hợp lý giúp kiểm soát luồng chương trình tốt hơn. Tạo ngoại lệ tùy chỉnh giúp mã nguồn rõ ràng, chuyên nghiệp và dễ gỡ lỗi khi có sự cố.

> ✅ Hãy thực hành nhiều để thành thạo kỹ năng này!
