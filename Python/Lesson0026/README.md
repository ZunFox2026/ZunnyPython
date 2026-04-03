# Python 26: Lập Trình Cơ Bản Từ A đến Z

## Giới thiệu

Chào mừng bạn đến với bài học thứ 26 trong chuỗi "Lập Trình Cơ Bản Từ A đến Z" – một hành trình toàn diện giúp bạn làm chủ ngôn ngữ Python từ những bước đầu tiên. Bài học này dành cho người mới bắt đầu, tập trung vào các khái niệm cơ bản nhưng thiết yếu như biến, kiểu dữ liệu, cấu trúc điều khiển và hàm. Mục tiêu là cung cấp nền tảng vững chắc để bạn tự tin phát triển các chương trình đơn giản và hiểu rõ cách Python hoạt động.

## Lý thuyết

Trong Python, mọi chương trình đều bắt đầu từ việc khai báo biến và sử dụng các kiểu dữ liệu cơ bản như số nguyên (`int`), số thực (`float`), chuỗi (`str`) và kiểu luận lý (`bool`). Bạn có thể sử dụng các cấu trúc điều khiển như `if`, `for`, và `while` để kiểm soát luồng chương trình. Ngoài ra, việc định nghĩa hàm bằng từ khóa `def` giúp tái sử dụng mã một cách hiệu quả. Hiểu rõ các khái niệm này là bước đệm quan trọng để học các chủ đề nâng cao hơn.

## Ví dụ

Dưới đây là một ví dụ đơn giản minh họa việc sử dụng biến, vòng lặp và hàm:

```python
def chao_tan(ten):
    print(f"Xin chào, {ten}!")

# Nhập tên từ người dùng
ten_nguoi_dung = input("Nhập tên của bạn: ")

# Gọi hàm
chao_tan(ten_nguoi_dung)

# Vòng lặp in số từ 1 đến 5
for i in range(1, 6):
    print(i)
```

Chương trình này sẽ hỏi tên người dùng, chào họ, rồi in các số từ 1 đến 5.

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập một số và in ra bình phương của số đó.
2. Tạo hàm `kiem_tra_chan_le(n)` để kiểm tra và in ra số `n` là chẵn hay lẻ.
3. Dùng vòng lặp `while` để in các số từ 10 về 1.

> Gợi ý: Sử dụng `input()` để nhận dữ liệu, `int()` để chuyển đổi kiểu, và `print()` để hiển thị kết quả.