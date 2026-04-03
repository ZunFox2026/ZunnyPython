# Python 32 Cấp Cơ Bản

## Giới thiệu

Chào mừng bạn đến với bài học thứ 32 trong chuỗi bài học "Python 32 Cấp Cơ Bản" – một hành trình từng bước giúp người mới bắt đầu làm quen và làm chủ ngôn ngữ lập trình Python. Bài học hôm nay sẽ giới thiệu về khái niệm **hàm (function)** trong Python – một công cụ thiết yếu giúp tổ chức và tái sử dụng mã hiệu quả. Hàm giúp chia nhỏ chương trình thành các phần nhỏ, dễ quản lý, giúp code gọn gàng và chuyên nghiệp hơn.

## Lý thuyết

Trong Python, **hàm** là một khối lệnh thực hiện một nhiệm vụ cụ thể và có thể được gọi (sử dụng) nhiều lần trong chương trình. Hàm giúp tránh lặp lại code và tăng khả năng bảo trì. Cú pháp định nghĩa hàm như sau:

```python
def tên_hàm(tham_số):
    # Các câu lệnh
    return giá_trị
```

- Từ khóa `def` dùng để khai báo hàm.
- `tên_hàm` nên mang tính mô tả, dễ hiểu.
- `tham_số` là dữ liệu đầu vào (có thể có hoặc không).
- `return` trả về kết quả (không bắt buộc).

## Ví dụ

Dưới đây là một ví dụ đơn giản về hàm tính bình phương của một số:

```python
def tinh_binh_phuong(x):
    return x ** 2

# Gọi hàm
ket_qua = tinh_binh_phuong(5)
print("Bình phương của 5 là:", ket_qua)
```

**Kết quả:**
```
Bình phương của 5 là: 25
```

## Bài tập

1. Viết một hàm có tên `tinh_tong` nhận vào hai tham số `a` và `b`, trả về tổng của chúng.
2. Viết hàm `in_loi_chao` nhận vào một tham số `ten`, in ra lời chào "Xin chào, [ten]!".
3. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra nếu `n` là số chẵn hay lẻ.

> Gợi ý: Sử dụng toán tử `%` để kiểm tra chia hết cho 2.

Hãy thử tự viết code và chạy thử các hàm này để làm chủ kiến thức!