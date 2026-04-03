# Python 38: Lập Trình Cơ Bản cho Người Mới Bắt Đầu

## Giới thiệu

Bài học này dành cho những ai mới bắt đầu làm quen với lập trình Python. Chúng ta sẽ cùng tìm hiểu những khái niệm cơ bản nhất, giúp bạn xây dựng nền tảng vững chắc để tiếp tục học các chủ đề nâng cao hơn. Python là ngôn ngữ dễ đọc, cú pháp đơn giản và phù hợp với người mới bắt đầu. Chỉ với vài dòng mã, bạn đã có thể tạo ra các chương trình hữu ích.

## Lý thuyết

Trong lập trình Python cơ bản, bạn cần nắm vững một số khái niệm nền tảng:

- **Biến (variable)**: Dùng để lưu trữ dữ liệu. Ví dụ: `tuoi = 20`
- **Kiểu dữ liệu**: Số nguyên (`int`), số thực (`float`), chuỗi (`str`), logic (`bool`)
- **Nhập/xuất dữ liệu**: Dùng `input()` để nhập, `print()` để xuất
- **Câu lệnh điều kiện**: `if`, `elif`, `else` giúp chương trình rẽ nhánh
- **Vòng lặp**: `for` và `while` dùng để lặp lại hành động

## Ví dụ

Dưới đây là một chương trình nhỏ kiểm tra xem một số do người dùng nhập vào là chẵn hay lẻ:

```python
# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra chẵn hay lẻ
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")
```

**Giải thích**:  
- `input()` nhận dữ liệu từ bàn phím, `int()` chuyển chuỗi thành số nguyên  
- Toán tử `%` lấy phần dư. Nếu chia cho 2 dư 0 thì là số chẵn

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập tên và in ra lời chào: `Xin chào, [tên]!`
2. Nhập vào một số và in ra bảng cửu chương từ 1 đến 10 của số đó.
3. Viết chương trình kiểm tra một số có phải là số dương, âm hay bằng 0.

> Gợi ý: Sử dụng `if-elif-else` và vòng lặp `for` để hoàn thành bài tập.  
> Hãy thử chạy và sửa lỗi nếu có – đó là một phần quan trọng của học lập trình!