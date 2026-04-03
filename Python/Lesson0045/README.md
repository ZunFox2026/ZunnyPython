# Python 45 Cấp Cơ Bản – Bài 45

## Giới thiệu

Bài học thứ 45 trong chuỗi "Python 45 Cấp Cơ Bản" tiếp tục củng cố kiến thức lập trình Python với chủ đề **Xử lý ngoại lệ (Exception Handling)**. Trong thực tế, chương trình có thể gặp lỗi do nhiều nguyên nhân như nhập liệu sai, file không tồn tại, chia cho 0,... Xử lý ngoại lệ giúp chương trình không bị sập và có thể phản hồi hợp lý khi gặp lỗi.

Python cung cấp cơ chế `try-except` để bắt và xử lý các lỗi phát sinh, từ đó tăng tính ổn định và thân thiện với người dùng.

## Lý thuyết

Trong Python, ta dùng khối lệnh `try-except` để xử lý ngoại lệ:

```python
try:
    # Các câu lệnh có thể gây lỗi
    pass
except TênLỗi:
    # Xử lý khi xảy ra lỗi cụ thể
    pass
```

- `try`: Chứa đoạn mã có thể gây lỗi.
- `except`: Xử lý lỗi nếu xảy ra. Có thể bắt lỗi cụ thể (ví dụ: `ValueError`, `ZeroDivisionError`) hoặc dùng `except Exception` để bắt mọi lỗi chung.
- Có thể dùng `else` (thực thi nếu không có lỗi) và `finally` (luôn thực thi, dù có lỗi hay không).

## Ví dụ

Dưới đây là ví dụ xử lý lỗi khi người dùng nhập không phải số hoặc chia cho 0:

```python
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    ket_qua = a / b
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
else:
    print(f"Kết quả: {ket_qua}")
finally:
    print("Chương trình kết thúc.")
```

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập tuổi. Nếu nhập không phải số, in thông báo lỗi và yêu cầu nhập lại.
2. Mở một file tên `data.txt` và đọc nội dung. Nếu file không tồn tại, in thông báo "File không tìm thấy".
3. Viết hàm `tinh_can_bac_hai(x)` tính căn bậc hai của `x`. Xử lý ngoại lệ khi `x < 0`.

> Gợi ý: Dùng `import math` và `math.sqrt()`, bắt lỗi bằng `ValueError` khi `x` âm.