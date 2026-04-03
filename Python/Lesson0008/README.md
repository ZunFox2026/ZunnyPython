# Python 8 Cấp Cơ Bản

## Giới thiệu

Bài học thứ 8 trong chuỗi "Python Cấp Cơ Bản" giúp người học làm quen với khái niệm **hàm (function)** trong Python. Hàm là một khối mã được tổ chức, tái sử dụng để thực hiện một hoặc nhiều hành động cụ thể. Việc sử dụng hàm giúp chương trình rõ ràng, dễ bảo trì và tránh lặp lại code. Đây là một trong những khái niệm cốt lõi khi học lập trình.

## Lý thuyết

Trong Python, hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm và dấu ngoặc đơn `()`. Các tham số (nếu có) được khai báo bên trong ngoặc, và khối lệnh trong hàm cần được thụt lề đúng cách.

Cú pháp cơ bản:
```python
def ten_ham(tham_so):
    # Các câu lệnh
    return ket_qua  # (tùy chọn)
```

Hàm có thể không trả về giá trị (chỉ thực hiện hành động), hoặc trả về kết quả bằng lệnh `return`. Sau khi định nghĩa, hàm cần được **gọi** để thực thi.

## Ví dụ

Dưới đây là ví dụ về hàm tính bình phương của một số:

```python
def tinh_binh_phuong(x):
    ket_qua = x ** 2
    return ket_qua

# Gọi hàm
so = 5
print(f"Bình phương của {so} là {tinh_binh_phuong(so)}")
```

Kết quả:
```
Bình phương của 5 là 25
```

## Bài tập

1. Viết hàm `tinh_tong(a, b)` nhận vào hai số và trả về tổng của chúng.
2. Viết hàm `in_loi_chao(ten)` in ra dòng chào "Xin chào, [ten]!".
3. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra số `n` là chẵn hay lẻ.

> Gợi ý: Sử dụng toán tử `%` để kiểm tra chia dư. Nếu `n % 2 == 0` thì là số chẵn.

Thử nghiệm các hàm này với các giá trị khác nhau để hiểu rõ cách hoạt động. Khi thành thạo, bạn có thể kết hợp nhiều hàm để xây dựng chương trình nhỏ.