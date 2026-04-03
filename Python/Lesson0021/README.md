# Python 21 cấp Cơ bản

## Giới thiệu

Bài học thứ 21 trong chuỗi "Python 21 cấp Cơ bản" giúp bạn củng cố kiến thức về **hàm trong Python** – một khái niệm nền tảng quan trọng giúp tổ chức và tái sử dụng mã hiệu quả. Hàm cho phép bạn gói gọn một đoạn mã thực hiện một nhiệm vụ cụ thể, sau đó gọi lại bất cứ khi nào cần mà không cần viết lại. Đây là bước tiến quan trọng để viết chương trình sạch, rõ ràng và dễ bảo trì.

## Lý thuyết

Hàm trong Python được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, dấu ngoặc đơn `()` và dấu hai chấm `:`. Các câu lệnh trong hàm được viết lùi vào (indent). Bạn có thể truyền dữ liệu vào hàm thông qua **tham số**, và hàm có thể trả về giá trị bằng lệnh `return`.

Cú pháp cơ bản:
```python
def ten_ham(tham_so):
    # nội dung hàm
    return gia_tri
```

Hàm có thể không có tham số, không trả về giá trị, hoặc cả hai. Việc sử dụng hàm giúp giảm sự trùng lặp mã, tăng tính modul hóa và dễ kiểm thử.

## Ví dụ

Dưới đây là một hàm đơn giản tính bình phương của một số:

```python
def tinh_binh_phuong(x):
    return x ** 2

# Gọi hàm
ket_qua = tinh_binh_phuong(5)
print("Bình phương của 5 là:", ket_qua)  # Output: Bình phương của 5 là: 25
```

Một ví dụ khác với hàm không trả về giá trị:
```python
def xin_chao(ten):
    print("Xin chào,", ten)

xin_chao("An")  # Output: Xin chào, An
```

## Bài tập

1. Viết hàm `tinh_tong(a, b)` nhận hai số và trả về tổng của chúng.
2. Viết hàm `kiem_tra_chan_le(n)` in ra "Chẵn" nếu `n` chia hết cho 2, ngược lại in "Lẻ".
3. Viết hàm `in_danh_sach(danh_sach)` để in từng phần tử trong danh sách ra màn hình, mỗi phần tử trên một dòng.

> Gợi ý: Sử dụng vòng lặp `for` bên trong hàm. Thử gọi các hàm này với dữ liệu mẫu để kiểm tra kết quả.