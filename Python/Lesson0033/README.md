# Python 33 Cấp Cơ Bản

## Giới thiệu

Bài học "Python 33 Cấp Cơ Bản" là bài thứ 33 trong chuỗi các bài học giúp người mới bắt đầu làm quen với ngôn ngữ lập trình Python. Bài học này tập trung vào việc hiểu và sử dụng **hàm (function)** – một khái niệm cốt lõi trong lập trình. Hàm giúp tổ chức mã nguồn, tái sử dụng code và làm cho chương trình dễ đọc, dễ bảo trì hơn. Sau bài học này, bạn sẽ nắm được cách định nghĩa, gọi và truyền tham số cho hàm trong Python.

## Lý thuyết

Trong Python, hàm là một khối lệnh thực hiện một nhiệm vụ cụ thể và chỉ được thực thi khi được gọi. Hàm giúp chia nhỏ chương trình thành các phần nhỏ, dễ quản lý. Cú pháp cơ bản để định nghĩa hàm trong Python là:

```python
def tên_hàm(tham_số):
    # khối lệnh
    return giá_trị_trả_về
```

- `def` là từ khóa để định nghĩa hàm.
- `tên_hàm` nên mang tính mô tả và viết thường, phân tách bằng dấu gạch dưới nếu cần.
- `tham_số` là dữ liệu đầu vào (có thể có hoặc không).
- `return` dùng để trả về kết quả (không bắt buộc).

Hàm có thể không có tham số, không trả về giá trị, hoặc cả hai.

## Ví dụ

Dưới đây là một ví dụ đơn giản về hàm tính bình phương của một số:

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
2. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra xem số `n` là chẵn hay lẻ.
3. Viết hàm `in_chuoi_lap_lai(chuoi, lan)` in chuỗi `chuoi` ra màn hình `lan` lần.

Hãy thực hành các bài tập trên để củng cố kiến thức về hàm trong Python!