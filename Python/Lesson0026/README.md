# Bài học Python số 26 - Cấp độ Trung cấp

## Chủ đề: Xử lý ngoại lệ (Exception Handling) nâng cao và tự tạo ngoại lệ

Trong bài học này, chúng ta sẽ tìm hiểu sâu hơn về cách xử lý lỗi trong Python — không chỉ dừng lại ở việc bắt lỗi thông thường, mà còn học cách tự tạo ra các loại ngoại lệ (exception) riêng để xử lý các tình huống đặc biệt trong chương trình. Đây là một kỹ năng quan trọng khi viết các ứng dụng thực tế, giúp chương trình trở nên ổn định, dễ bảo trì và dễ gỡ lỗi hơn.

### Mục tiêu bài học
- Hiểu được cơ chế xử lý ngoại lệ nâng cao (try, except, else, finally)
- Biết cách bắt nhiều ngoại lệ và xử lý riêng biệt
- Hiểu và tự tạo các lớp ngoại lệ tùy chỉnh (custom exceptions)
- Ứng dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, tính toán, kiểm tra dữ liệu đầu vào

### Yêu cầu trước khi học
- Đã nắm vững kiến thức về hàm, lớp và kế thừa trong Python
- Đã từng sử dụng `try-except` ở mức cơ bản

### Cấu trúc bài học
1. **Lý thuyết chi tiết**
2. **Ví dụ minh họa hoàn chỉnh**
3. **Bài tập thực hành**
4. **Tổng kết**

---

## 1. Lý thuyết chi tiết

### Cấu trúc `try-except-else-finally`

Ngoài `try` và `except`, Python cung cấp thêm hai khối lệnh phụ trợ là `else` và `finally`:

- `else`: chạy khi **không có ngoại lệ nào xảy ra** trong khối `try`
- `finally`: luôn chạy **dù có hay không có ngoại lệ**, thường dùng để giải phóng tài nguyên

```python
try:
    # Code có thể gây lỗi
    pass
except ValueError:
    # Xử lý lỗi ValueError
    pass
except Exception as e:
    # Xử lý các lỗi khác
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy
    pass
```

### Bắt nhiều ngoại lệ riêng biệt
Có thể bắt từng loại lỗi cụ thể để xử lý khác nhau, giúp chương trình linh hoạt hơn.

### Tự tạo ngoại lệ tùy chỉnh
Bạn có thể tạo lớp ngoại lệ riêng bằng cách kế thừa từ `Exception` hoặc một lớp con của nó.

```python
class MyCustomError(Exception):
    """Lớp ngoại lệ tùy chỉnh"""
    pass
```

---

## 2. Ví dụ minh họa

### Ví dụ 1: Xử lý lỗi khi đọc file và tính trung bình

Chương trình đọc file số, tính trung bình, xử lý các lỗi có thể xảy ra: file không tồn tại, file rỗng, dữ liệu không hợp lệ.

### Ví dụ 2: Tạo ngoại lệ tùy chỉnh cho tài khoản ngân hàng

Tạo lớp `BankAccount` với các lỗi riêng: rút tiền quá số dư, nạp tiền âm.

### Ví dụ 3: Xử lý lỗi đầu vào người dùng với `else` và `finally`

Chương trình yêu cầu người dùng nhập số, xử lý lỗi nhập sai, in thông báo thành công nếu thành công, và luôn in lời chào cuối cùng.

---

## 3. Bài tập thực hành

1. Viết hàm chia hai số, xử lý lỗi chia cho 0 và kiểu dữ liệu không hợp lệ.
2. Tạo lớp `AgeError` để xử lý tuổi không hợp lệ (dưới 0 hoặc trên 150).
3. Viết chương trình đọc danh sách tên từ file, xử lý lỗi file và định dạng.
4. Viết hàm đăng nhập, ném ngoại lệ nếu tên đăng nhập hoặc mật khẩu sai.
5. Tạo lớp `Temperature` với phương thức đặt nhiệt độ, ném lỗi nếu nhiệt độ dưới -273.15°C.

---

## 4. Tổng kết

- `try-except-else-finally` giúp kiểm soát lỗi toàn diện
- Bắt lỗi cụ thể giúp xử lý chính xác hơn
- Tự tạo ngoại lệ tùy chỉnh giúp code rõ ràng, chuyên nghiệp hơn
- Luôn dùng `finally` để giải phóng tài nguyên (file, kết nối, v.v.)

Việc xử lý lỗi tốt không chỉ giúp chương trình không bị sập, mà còn cung cấp trải nghiệm người dùng tốt và hỗ trợ debug hiệu quả.
