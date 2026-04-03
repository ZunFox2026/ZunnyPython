# Bài học 1: Biến, Kiểu Dữ Liệu, Nhập Xuất Cơ Bản

Chào mừng bạn đến với bài học đầu tiên trong hành trình học Python! Bài học này sẽ giúp bạn làm quen với các khái niệm cơ bản nhất khi lập trình: **biến**, **kiểu dữ liệu**, và cách **nhập xuất dữ liệu** từ người dùng.

Bạn sẽ học cách lưu trữ thông tin, làm việc với các loại dữ liệu phổ biến như số, chữ, và tương tác với người dùng thông qua bàn phím và màn hình.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu và sử dụng biến để lưu trữ dữ liệu.
- Nhận biết các kiểu dữ liệu cơ bản: số nguyên, số thực, chuỗi, boolean.
- Sử dụng lệnh `print()` để xuất thông tin ra màn hình.
- Sử dụng lệnh `input()` để nhập dữ liệu từ người dùng.
- Áp dụng kiến thức vào các chương trình đơn giản như tính toán, chào hỏi, chuyển đổi đơn vị.

---

## Lý thuyết chi tiết

### 1. Biến (Variable)

Biến là một tên gọi để lưu trữ dữ liệu trong chương trình. Bạn có thể hình dung biến như một cái hộp có nhãn dán, và bên trong chứa giá trị nào đó.

**Cú pháp gán giá trị:**
```python
ten_bien = gia_tri
```

Ví dụ:
```python
tuoi = 20
ho_ten = "Nguyễn Văn A"
```

### 2. Các kiểu dữ liệu cơ bản

- **int (số nguyên):** như `5`, `-10`, `1000`
- **float (số thực):** như `3.14`, `-2.5`, `0.0`
- **str (chuỗi ký tự):** như `"Hello"`, `'Python'`, `"123"` (có dấu nháy)
- **bool (logic):** chỉ nhận giá trị `True` hoặc `False`

Bạn có thể kiểm tra kiểu dữ liệu bằng hàm `type()`.

### 3. Nhập và xuất dữ liệu

- **Xuất dữ liệu:** Dùng lệnh `print()` để in ra màn hình.
  ```python
  print("Xin chào bạn!")
  print(100)
  print(tuoi)
  ```

- **Nhập dữ liệu:** Dùng lệnh `input()` để đọc dữ liệu từ người dùng.
  ```python
  ten = input("Nhập tên của bạn: ")
  ```
  Lưu ý: `input()` luôn trả về **chuỗi** (str), nên nếu muốn số, phải chuyển đổi kiểu.

### 4. Chuyển đổi kiểu dữ liệu

- `int(chuoi)` → chuyển chuỗi thành số nguyên
- `float(chuoi)` → chuyển thành số thực
- `str(so)` → chuyển số thành chuỗi

Ví dụ:
```python
chieu_cao = float(input("Chiều cao (m): "))
```

---

## Ví dụ minh họa

### Ví dụ 1: Chào hỏi người dùng

```python
ten = input("Tên của bạn là gì? ")
print("Xin chào,", ten, "!")
```

### Ví dụ 2: Tính tổng hai số

```python
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
tong = so1 + so2
print("Tổng là:", tong)
```

### Ví dụ 3: Chuyển đổi nhiệt độ C sang F

```python
celsius = float(input("Nhập nhiệt độ C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} độ C = {fahrenheit} độ F")
```

---

## Bài tập thực hành

1. Viết chương trình nhập tên và tuổi, rồi in ra lời chào có kèm tuổi.
2. Viết chương trình tính diện tích hình chữ nhật khi biết chiều dài và chiều rộng.
3. Viết chương trình chuyển đổi từ km sang mét (1 km = 1000 m).
4. Viết chương trình nhập điểm 3 môn học, tính điểm trung bình.
5. Viết chương trình hỏi người dùng năm sinh, rồi tính và in ra tuổi hiện tại (giả sử năm nay là 2025).

> 💡 Gợi ý: Dùng `input()`, chuyển kiểu nếu cần, và `print()` để hiển thị kết quả.

---

## Tổng kết

Bài học đầu tiên đã giới thiệu các nền tảng cơ bản nhất của Python:
- **Biến** giúp lưu trữ dữ liệu.
- Có 4 **kiểu dữ liệu** chính: `int`, `float`, `str`, `bool`.
- Dùng `print()` để **xuất**, `input()` để **nhập**.
- Nhớ chuyển kiểu dữ liệu khi cần thiết!

Hãy luyện tập thật nhiều với các bài tập để thành thạo. Ở bài tiếp theo, chúng ta sẽ học về **câu điều kiện** (if/else) để chương trình có thể "ra quyết định"!
