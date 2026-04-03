# Bài học Python số 28 - Cấp độ Trung cấp

## Chủ đề: Xử lý ngoại lệ (Exception Handling) nâng cao

Trong bài học này, chúng ta sẽ tìm hiểu sâu hơn về xử lý ngoại lệ trong Python — một kỹ năng quan trọng giúp chương trình của bạn trở nên **ổn định**, **dễ bảo trì** và **thân thiện với người dùng** hơn. Chúng ta không chỉ dừng ở `try-except` cơ bản, mà sẽ khám phá các khái niệm nâng cao như: `else`, `finally`, tạo ngoại lệ tùy chỉnh, và xử lý nhiều loại ngoại lệ một cách thông minh.

### ✅ Mục tiêu bài học
- Hiểu rõ cấu trúc `try`, `except`, `else`, `finally`.
- Biết cách bắt nhiều ngoại lệ và xử lý chúng riêng biệt.
- Tạo và sử dụng ngoại lệ tùy chỉnh (custom exceptions).
- Ứng dụng thực tế: xử lý lỗi khi làm việc với file và dữ liệu người dùng.

### 📚 Lý thuyết chi tiết

#### 1. Cấu trúc `try-except-else-finally`

```python
try:
    # Đoạn code có thể gây lỗi
    pass
except LoaiException as e:
    # Xử lý lỗi cụ thể
    pass
else:
    # Chạy nếu KHÔNG có lỗi
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

- `except`: Bắt và xử lý lỗi.
- `else`: Thực thi khi không có ngoại lệ.
- `finally`: Luôn được thực thi — lý tưởng để dọn dẹp tài nguyên (đóng file, kết nối DB...).

#### 2. Bắt nhiều ngoại lệ

Bạn có thể bắt nhiều loại ngoại lệ riêng biệt:

```python
except ValueError:
    print("Lỗi định dạng dữ liệu")
except FileNotFoundError:
    print("Không tìm thấy file")
```

#### 3. Tạo ngoại lệ tùy chỉnh

Tạo class kế thừa từ `Exception`:

```python
class MyCustomError(Exception):
    pass
```

### 🧪 Ví dụ minh họa

Xem file `main.py` để chạy các ví dụ sau:

1. **Đọc file an toàn** với `try-except-finally`.
2. **Chuyển đổi dữ liệu người dùng** với xử lý `ValueError`.
3. **Sử dụng ngoại lệ tùy chỉnh** khi kiểm tra tuổi.

### 📝 Bài tập thực hành

Xem file `exercises.py`. Hãy hoàn thành các hàm sau:

1. `chia_hai_so(a, b)` - xử lý chia cho 0 và đầu vào không hợp lệ.
2. `doc_danh_sach_tu_file(filename)` - đọc file, xử lý lỗi nếu file không tồn tại hoặc nội dung không hợp lệ.
3. `kiem_tra_mat_khau(password)` - ném ngoại lệ tùy chỉnh nếu mật khẩu yếu.

Gợi ý: Sử dụng `try-except`, `isinstance`, và tạo class lỗi riêng.

### 🔚 Tổng kết

Xử lý ngoại lệ không chỉ giúp tránh crash chương trình, mà còn làm cho code **rõ ràng** và **dễ kiểm soát lỗi**. Ở cấp độ trung cấp, bạn nên:
- Luôn xử lý ngoại lệ khi làm việc với file, nhập liệu, mạng.
- Sử dụng `finally` để giải phóng tài nguyên.
- Tạo ngoại lệ tùy chỉnh để phản ánh logic nghiệp vụ.

Hãy luyện tập thường xuyên để viết code **chuyên nghiệp** và **chống lỗi tốt** hơn!
