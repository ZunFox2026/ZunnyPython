# Python 44 Cấp Cơ Bản

## Giới thiệu

Bài học "Python 44 Cấp Cơ Bản" là một phần trong chuỗi bài học giúp người mới bắt đầu làm quen và nắm vững các khái niệm lập trình cơ bản trong Python. Bài học này tập trung vào việc sử dụng vòng lặp `for` để xử lý dữ liệu trong danh sách (list), một cấu trúc dữ liệu phổ biến và thiết yếu trong Python. Qua bài học, người học sẽ hiểu cách duyệt qua các phần tử trong danh sách, thao tác với từng giá trị và áp dụng vào các tình huống thực tế đơn giản.

## Lý thuyết

Vòng lặp `for` trong Python cho phép duyệt qua các phần tử của một chuỗi (như danh sách, chuỗi ký tự, tuple,...) một cách dễ dàng. Cú pháp cơ bản như sau:

```python
for phần_tử in danh_sách:
    # Thực hiện công việc với phần_tử
```

Với danh sách (list), bạn có thể truy cập từng phần tử mà không cần dùng chỉ số, giúp code ngắn gọn và dễ đọc hơn. Ngoài ra, Python cung cấp nhiều phương thức hỗ trợ như `append()`, `len()`, giúp thao tác với danh sách hiệu quả.

## Ví dụ

Dưới đây là ví dụ in ra từng phần tử trong danh sách tên học sinh:

```python
danh_sach_hoc_sinh = ["An", "Bình", "Chi", "Dũng"]

for ten in danh_sach_hoc_sinh:
    print(f"Xin chào, {ten}!")
```

Kết quả in ra:
```
Xin chào, An!
Xin chào, Bình!
Xin chào, Chi!
Xin chào, Dũng!
```

## Bài tập

1. Tạo một danh sách chứa các số nguyên từ 1 đến 5. Dùng vòng lặp `for` để in ra bình phương của từng số.
2. Viết chương trình nhập vào 3 tên người dùng, lưu vào danh sách, sau đó in lời chào tới từng người.
3. Tạo danh sách điểm số (ví dụ: [8, 6, 9, 7, 10]), dùng vòng lặp để đếm có bao nhiêu điểm lớn hơn hoặc bằng 8.

> Gợi ý: Dùng biến đếm khởi tạo bằng 0 và tăng dần trong vòng lặp.