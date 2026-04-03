# Python 63: Lập Trình Cơ Bản cho Người Mới Bắt Đầu

## Giới thiệu

Chào mừng bạn đến bài học thứ 63 trong chuỗi bài học về Python – dành riêng cho người mới bắt đầu! Trong bài này, chúng ta sẽ tìm hiểu những khái niệm cơ bản nhất trong lập trình Python, giúp bạn làm quen với cú pháp, cách viết chương trình đơn giản và tư duy lập trình. Dù bạn chưa từng học lập trình trước đây, bài học này sẽ cung cấp nền tảng vững chắc để bạn tiếp tục hành trình chinh phục Python.

## Lý thuyết

Lập trình là cách chúng ta giao tiếp với máy tính để thực hiện các công việc cụ thể. Python là một ngôn ngữ lập trình dễ học, cú pháp rõ ràng và gần với ngôn ngữ tự nhiên. Một số khái niệm cơ bản bạn cần biết:

- **Biến (Variable)**: Dùng để lưu trữ dữ liệu, ví dụ: `ten = "An"`.
- **Kiểu dữ liệu**: Như số nguyên (`int`), số thực (`float`), chuỗi (`str`), và kiểu logic (`bool`).
- **In dữ liệu**: Dùng hàm `print()` để hiển thị thông tin ra màn hình.
- **Nhập liệu**: Dùng hàm `input()` để người dùng nhập dữ liệu từ bàn phím.

## Ví dụ

Dưới đây là một chương trình Python đơn giản:

```python
# Nhập tên từ người dùng và chào hỏi
ten = input("Nhập tên của bạn: ")
tuoi = int(input("Nhập tuổi của bạn: "))

print("Xin chào,", ten)
print("Bạn", tuoi, "tuổi.")
if tuoi >= 18:
    print("Bạn đã trưởng thành.")
else:
    print("Bạn còn nhỏ tuổi.")
```

Chương trình này minh họa cách sử dụng biến, nhập liệu, in kết quả và câu lệnh điều kiện `if-else`.

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập chiều cao (cm) và cân nặng (kg), sau đó tính và in chỉ số BMI.
2. Viết chương trình kiểm tra một số nguyên nhập vào là chẵn hay lẻ.
3. Viết chương trình hỏi tên người dùng và in ra lời chào kèm theo tên, ví dụ: "Chào bạn Nguyễn Văn A!".

> Gợi ý: Dùng `input()`, `int()`, `print()` và câu lệnh `if` để hoàn thành bài tập.

Chúc bạn học lập trình vui vẻ và tiến bộ từng ngày!