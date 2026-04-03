# Python 13: Lập Trình Cơ Bản Từ A đến Z

## Giới thiệu

Bài học thứ 13 này tiếp tục hành trình khám phá lập trình Python từ con số 0, dành cho người mới bắt đầu. Chúng ta sẽ tìm hiểu các khái niệm cơ bản nhưng cực kỳ quan trọng trong Python như biến, kiểu dữ liệu, cấu trúc điều kiện và vòng lặp – nền tảng cốt lõi để phát triển các chương trình phức tạp hơn sau này. Sau bài học, bạn sẽ tự tin viết những đoạn mã Python đơn giản và hiểu cách chúng hoạt động.

## Lý thuyết

Trong Python, bạn có thể khai báo **biến** mà không cần chỉ định kiểu dữ liệu. Các kiểu dữ liệu cơ bản bao gồm:
- `int`: số nguyên (ví dụ: `5`, `-3`)
- `float`: số thực (ví dụ: `3.14`)
- `str`: chuỗi ký tự (ví dụ: `"xin chào"`)
- `bool`: giá trị logic (`True` hoặc `False`)

Cấu trúc điều kiện `if-elif-else` giúp chương trình đưa ra quyết định dựa trên điều kiện. Vòng lặp `for` dùng để lặp qua một dãy giá trị, rất hữu ích khi xử lý danh sách hoặc lặp lại công việc.

## Ví dụ

Dưới đây là một chương trình nhỏ kiểm tra số chẵn/lẻ:

```python
so = int(input("Nhập một số nguyên: "))

if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

print("Chương trình kết thúc.")
```

Khi chạy, chương trình sẽ yêu cầu người dùng nhập số, sau đó kiểm tra và in ra kết quả tương ứng.

## Bài tập

1. Viết chương trình nhập vào nhiệt độ Celsius và chuyển sang Fahrenheit theo công thức: `F = C * 9/5 + 32`.
2. Nhập một số nguyên dương và in ra các số từ 1 đến số đó bằng vòng lặp `for`.
3. Viết chương trình kiểm tra một năm có phải năm nhuận hay không (năm nhuận chia hết cho 4, nhưng nếu chia hết cho 100 thì phải chia hết cho 400).

> **Gợi ý**: Sử dụng `input()` để nhập dữ liệu, `int()` để chuyển đổi kiểu, và các toán tử so sánh như `==`, `%` để kiểm tra điều kiện.