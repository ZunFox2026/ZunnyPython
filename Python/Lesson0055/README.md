# Bài 55: Python Cơ bản

## Giới thiệu

Python là một ngôn ngữ lập trình bậc cao, dễ học và mạnh mẽ, được sử dụng rộng rãi trong nhiều lĩnh vực như phát triển web, phân tích dữ liệu, trí tuệ nhân tạo và tự động hóa. Bài học này sẽ giới thiệu những khái niệm cơ bản nhất trong Python, giúp người mới bắt đầu làm quen với cú pháp và cách viết chương trình đơn giản. Đây là bước đầu tiên quan trọng để phát triển kỹ năng lập trình.

## Lý thuyết

Python sử dụng cú pháp đơn giản, gần với ngôn ngữ tự nhiên. Một số khái niệm cơ bản bao gồm:
- **Biến**: Dùng để lưu trữ dữ liệu. Không cần khai báo kiểu dữ liệu.
- **Kiểu dữ liệu**: Số nguyên (`int`), số thực (`float`), chuỗi (`str`), logic (`bool`), v.v.
- **In ra màn hình**: Dùng hàm `print()`.
- **Nhập dữ liệu**: Dùng hàm `input()`.
- **Câu lệnh điều kiện**: `if`, `elif`, `else`.
- **Vòng lặp**: `for`, `while`.

Python phân biệt khoảng trắng (indentation) thay vì dấu ngoặc, do đó việc thụt đầu dòng rất quan trọng.

## Ví dụ

Dưới đây là một chương trình Python đơn giản, yêu cầu người dùng nhập tên và tuổi, sau đó in ra lời chào:

```python
# Nhập thông tin từ người dùng
ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi của bạn: "))

# In ra lời chào
print(f"Xin chào, {ten}! Bạn {tuoi} tuổi.")

# Kiểm tra tuổi
if tuoi >= 18:
    print("Bạn đã đủ tuổi trưởng thành.")
else:
    print("Bạn chưa đủ tuổi trưởng thành.")
```

Chương trình này minh họa cách sử dụng biến, hàm `input()`, `print()`, kiểu dữ liệu và câu lệnh điều kiện.

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập hai số, sau đó in ra tổng, hiệu, tích và thương của hai số đó.
2. Viết chương trình kiểm tra một số nhập vào là chẵn hay lẻ.
3. Viết chương trình in ra các số từ 1 đến 10 bằng vòng lặp `for`.
4. Viết chương trình tính tổng các số từ 1 đến n (với n do người dùng nhập).

> Gợi ý: Sử dụng vòng lặp `for` và câu lệnh điều kiện để hoàn thành bài tập.