# Python 11 Cấp Cơ Bản

## Giới thiệu

Bài 11 trong chuỗi bài học "Python Cấp Cơ Bản" giúp người học làm quen với khái niệm **hàm (function)** trong Python — một trong những thành phần cốt lõi để viết code rõ ràng, tái sử dụng và dễ quản lý. Hàm giúp nhóm các đoạn mã thực hiện một nhiệm vụ cụ thể, từ đó tránh lặp lại code và tăng tính tổ chức cho chương trình.

## Lý thuyết

Hàm trong Python được định nghĩa bằng từ khóa `def`, theo sau là tên hàm và cặp dấu ngoặc đơn `()`. Các tham số (nếu có) được đặt bên trong ngoặc, và khối lệnh của hàm được viết lùi vào (indent). Khi gọi hàm, ta sử dụng tên hàm kèm theo dấu ngoặc.

Cú pháp:
```python
def ten_ham(tham_so):
    # Các câu lệnh
    return ket_qua  # (tùy chọn)
```

Hàm có thể trả về giá trị bằng lệnh `return`. Nếu không có `return`, hàm sẽ trả về `None` mặc định.

## Ví dụ

Dưới đây là ví dụ về một hàm đơn giản tính bình phương của một số:

```python
def tinh_binh_phuong(x):
    return x ** 2

# Gọi hàm
ket_qua = tinh_binh_phuong(5)
print("Bình phương của 5 là:", ket_qua)
```

Kết quả:
```
Bình phương của 5 là: 25
```

Hàm `tinh_binh_phuong` nhận một tham số `x`, tính bình phương và trả về kết quả. Sau đó, ta gọi hàm và in kết quả ra màn hình.

## Bài tập

1. Viết hàm `tinh_tong` nhận hai tham số `a` và `b`, trả về tổng của chúng. Gọi hàm với các giá trị 3 và 7, in kết quả.
2. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra `"Chẵn"` nếu `n` chia hết cho 2, ngược lại in `"Lẻ"`.
3. Viết hàm `in_loi_chao(ten)` in ra lời chào dạng `"Xin chào, [ten]!"`. Gọi hàm với tên của bạn.

> Gợi ý: Sử dụng `def` để định nghĩa hàm, `return` (nếu cần) và gọi hàm để kiểm tra kết quả.