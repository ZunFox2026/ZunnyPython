# Bài 36: Cấp Cơ Bản - Xử lý Ngoại lệ trong Python

## Giới thiệu

Trong quá trình viết chương trình, sẽ có những lúc chương trình gặp lỗi trong lúc thực thi (runtime errors), chẳng hạn như chia cho 0, truy cập chỉ số ngoài danh sách, hoặc mở một tệp không tồn tại. Thay vì để chương trình bị dừng đột ngột, Python cung cấp cơ chế **xử lý ngoại lệ (exception handling)** giúp chương trình có thể bắt lỗi và xử lý một cách mềm dẻo, giữ cho ứng dụng hoạt động ổn định hơn.

## Lý thuyết

Xử lý ngoại lệ trong Python được thực hiện thông qua khối lệnh `try-except`. Cấu trúc cơ bản như sau:

```python
try:
    # Các câu lệnh có thể gây lỗi
    pass
except TênLỗi:
    # Xử lý khi xảy ra lỗi cụ thể
    pass
```

Một số lỗi phổ biến:
- `ZeroDivisionError`: chia cho 0
- `IndexError`: truy cập chỉ số ngoài danh sách
- `ValueError`: giá trị không hợp lệ
- `FileNotFoundError`: không tìm thấy tệp

Bạn cũng có thể dùng `else` (chạy nếu không có lỗi) và `finally` (luôn chạy, dù có lỗi hay không).

## Ví dụ

Dưới đây là ví dụ xử lý lỗi khi người dùng nhập sai kiểu dữ liệu:

```python
try:
    so = int(input("Nhập một số nguyên: "))
    print(f"Bạn đã nhập số: {so}")
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")
else:
    print("Nhập dữ liệu thành công!")
finally:
    print("Kết thúc chương trình.")
```

Nếu người dùng nhập chữ thay vì số, chương trình sẽ không sập mà in ra thông báo lỗi và tiếp tục chạy.

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập hai số, thực hiện phép chia. Xử lý trường hợp chia cho 0.
2. Tạo một danh sách gồm 5 phần tử. Viết chương trình nhập chỉ số từ người dùng và in ra phần tử tại vị trí đó. Xử lý lỗi khi chỉ số vượt quá.
3. Mở một tệp văn bản để đọc. Nếu tệp không tồn tại, in ra thông báo "Tệp không tìm thấy".

> Gợi ý: Sử dụng `try`, `except`, và các loại lỗi phù hợp để đảm bảo chương trình luôn hoạt động ổn định.