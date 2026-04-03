# Python 12 Cấp Cơ Bản – Bài 12: Hàm trong Python

## Giới thiệu

Trong lập trình Python, **hàm** (function) là một khối mã thực hiện một nhiệm vụ cụ thể và có thể được gọi lại nhiều lần. Việc sử dụng hàm giúp chương trình trở nên ngắn gọn, dễ đọc, dễ bảo trì và tái sử dụng. Bài học này sẽ giới thiệu cách định nghĩa và sử dụng hàm trong Python, một trong những khái niệm quan trọng nhất trong lập trình.

## Lý thuyết

Trong Python, hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, dấu ngoặc đơn `()` và dấu hai chấm `:`. Các câu lệnh bên trong hàm phải được thụt lề. Có thể truyền dữ liệu vào hàm thông qua **tham số**, và hàm có thể trả về giá trị bằng câu lệnh `return`.

Cú pháp cơ bản:
```python
def ten_ham(tham_so):
    # Các câu lệnh
    return gia_tri
```

Hàm có thể không có tham số và không trả về giá trị. Python cũng hỗ trợ hàm với tham số mặc định, tham số tùy chọn và trả về nhiều giá trị.

## Ví dụ

Dưới đây là một ví dụ đơn giản về hàm tính tổng hai số:

```python
def tinh_tong(a, b):
    tong = a + b
    return tong

# Gọi hàm
ket_qua = tinh_tong(5, 3)
print("Tổng là:", ket_qua)  # Kết quả: Tổng là: 8
```

Hàm `tinh_tong` nhận hai tham số `a` và `b`, tính tổng và trả về kết quả. Sau đó, chúng ta gọi hàm và in ra kết quả.

## Bài tập

1. Viết hàm `tinh_tich(x, y)` nhận vào hai số và trả về tích của chúng.
2. Viết hàm `chao_ten(ten)` in ra dòng chào “Xin chào, [ten]!”.
3. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra số `n` là chẵn hay lẻ.

> Gợi ý: Sử dụng toán tử `%` để kiểm tra chia dư. Nếu `n % 2 == 0` thì `n` là số chẵn.

Bạn hãy thử tự viết các hàm này và kiểm tra kết quả!