# Bài học Python số 20: Xử lý lỗi và ngoại lệ (Exception Handling)

## Mục tiêu bài học
- Hiểu được khái niệm lỗi và ngoại lệ trong Python.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để xử lý lỗi một cách an toàn.
- Áp dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, nhập liệu người dùng, chia số.
- Phát triển thói quen viết code an toàn, tránh crash chương trình.

## Lý thuyết chi tiết
Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như: chia cho 0, truy cập chỉ số ngoài danh sách, mở file không tồn tại, v.v. Những lỗi này được gọi là **ngoại lệ (exception)**.

Python cung cấp cơ chế **xử lý ngoại lệ** bằng các khối lệnh:

- `try`: Chứa đoạn code có thể gây lỗi.
- `except`: Xử lý lỗi nếu xảy ra.
- `else`: Chạy nếu không có lỗi.
- `finally`: Luôn chạy, dù có lỗi hay không.

### Cú pháp cơ bản
```python
try:
    # Code có thể gây lỗi
    pass
except LoaiLoi:
    # Xử lý lỗi cụ thể
    pass
except:
    # Xử lý mọi lỗi còn lại
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy
    pass
```

### Ví dụ xử lý lỗi chia cho 0
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
```

## Ví dụ minh họa
Dưới đây là 3 ví dụ thực tế giúp bạn hiểu rõ cách áp dụng xử lý ngoại lệ.

### Ví dụ 1: Đọc file an toàn
```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Không tìm thấy file!")
except PermissionError:
    print("Không có quyền truy cập file!")
```

### Ví dụ 2: Nhập số từ người dùng
```python
while True:
    try:
        age = int(input("Nhập tuổi của bạn: "))
        if age < 0:
            raise ValueError("Tuổi không thể âm!")
        print(f"Tuổi của bạn là {age}")
        break
    except ValueError as e:
        print(f"Lỗi: {e}. Vui lòng nhập số nguyên dương.")
```

### Ví dụ 3: Tính trung bình cộng an toàn
```python
def tinh_trung_binh(numbers):
    try:
        avg = sum(numbers) / len(numbers)
        return avg
    except ZeroDivisionError:
        return None
    except TypeError:
        print("Dữ liệu đầu vào không hợp lệ (phải là danh sách số).")
        return None

print(tinh_trung_binh([1, 2, 3, 4]))  # 2.5
print(tinh_trung_binh([]))           # None
print(tinh_trung_binh("abc"))        # Lỗi, trả về None
```

## Bài tập thực hành
1. Viết hàm `chia_hai_so(a, b)` nhận hai số và trả về kết quả a/b. Xử lý các lỗi có thể xảy ra.
2. Viết chương trình đọc một file số, mỗi dòng một số, tính tổng các số. Xử lý lỗi nếu file không tồn tại hoặc có dòng không phải số.
3. Viết hàm `dang_nhap(username, password)` kiểm tra username và password. Nếu sai định dạng (username rỗng, password < 6 ký tự), ném ra `ValueError`. Xử lý lỗi khi gọi hàm.
4. Viết chương trình cho phép người dùng nhập 5 số. Nếu nhập sai, yêu cầu nhập lại. Sử dụng vòng lặp và try-except.
5. Viết hàm `mo_file_va_doc_dong_dau(file_path)` mở file và trả về dòng đầu tiên. Dùng `finally` để đảm bảo thông báo đã hoàn tất thao tác.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình của bạn **ổn định và thân thiện với người dùng**. Thay vì để chương trình sập khi có lỗi, bạn nên dự đoán và xử lý các trường hợp bất thường. Luôn nhớ:
- Dùng `try-except` cho các đoạn code dễ gây lỗi (I/O, chuyển kiểu, chia số...).
- Bắt lỗi cụ thể thay vì dùng `except` chung chung.
- Dùng `finally` để dọn dẹp tài nguyên (đóng file, kết nối DB...).
- Có thể ném lỗi bằng `raise` khi cần thiết.

Thực hành thường xuyên để thành thạo kỹ năng này!