# Python 6 cấp Cơ bản – Bài 6

## Giới thiệu

Chào mừng bạn đến với bài học thứ 6 trong chuỗi "Python 6 cấp Cơ bản"! Bài học này sẽ giúp bạn làm quen với **vòng lặp `for`** – một trong những cấu trúc điều khiển quan trọng nhất trong lập trình Python. Vòng lặp cho phép bạn thực hiện một đoạn mã nhiều lần một cách tự động, rất hữu ích khi xử lý danh sách, dãy số hoặc lặp qua các phần tử dữ liệu.

Sau bài học này, bạn sẽ hiểu cách sử dụng `for` để tiết kiệm thời gian và viết code hiệu quả hơn.

## Lý thuyết

Vòng lặp `for` trong Python được dùng để lặp qua một dãy (sequence) như danh sách (list), chuỗi (string), dãy số (range)... Cú pháp cơ bản như sau:

```python
for biến in dãy:
    # Khối lệnh lặp lại
```

Hàm `range()` thường được dùng để tạo dãy số. Ví dụ:
- `range(5)` tạo dãy 0, 1, 2, 3, 4.
- `range(1, 6)` tạo dãy 1, 2, 3, 4, 5.

## Ví dụ

Dưới đây là ví dụ in các số từ 1 đến 5:

```python
for i in range(1, 6):
    print("Số:", i)
```

Kết quả:
```
Số: 1
Số: 2
Số: 3
Số: 4
Số: 5
```

Bạn cũng có thể lặp qua một danh sách:

```python
danh_sach = ["Táo", "Cam", "Chuối"]
for fruit in danh_sach:
    print("Trái cây:", fruit)
```

## Bài tập

1. Viết chương trình sử dụng vòng lặp `for` để in các số từ 10 đến 15.
2. Tạo một danh sách tên bạn bè, sau đó in lời chào cho từng người. Ví dụ: `Xin chào, Minh!`
3. Dùng `range(0, 10, 2)` để in các số chẵn từ 0 đến 8.

> Gợi ý: `range(start, stop, step)` – step là bước nhảy.

Hãy thử tự viết code và chạy thử! Vòng lặp là nền tảng để học các chủ đề nâng cao hơn như xử lý dữ liệu và thuật toán.