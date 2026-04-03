# Bài học 3: Vòng lặp for và while trong Python

Chào mừng bạn đến với bài học thứ 3 trong khóa học Python cơ bản! Trong bài học này, chúng ta sẽ tìm hiểu về **vòng lặp**, một trong những khái niệm cốt lõi trong lập trình. Cụ thể, chúng ta sẽ học cách sử dụng hai loại vòng lặp phổ biến nhất trong Python: `for` và `while`.

Vòng lặp giúp chúng ta thực hiện một đoạn mã nhiều lần mà không cần viết lại, rất hữu ích khi xử lý danh sách, tính toán lặp lại hoặc kiểm tra điều kiện.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu được khái niệm vòng lặp trong lập trình.
- Sử dụng vòng lặp `for` để lặp qua danh sách, chuỗi, hoặc dãy số.
- Sử dụng vòng lặp `while` để lặp khi điều kiện còn đúng.
- Phân biệt được khi nào nên dùng `for` và khi nào dùng `while`.
- Viết chương trình đơn giản sử dụng vòng lặp.

---

## Lý thuyết chi tiết

### 1. Vòng lặp `for`

Vòng lặp `for` được dùng để lặp qua một dãy (sequence) như danh sách (list), chuỗi (string), hoặc dãy số (dùng `range()`).

Cú pháp cơ bản:
```python
for biến in dãy:
    # các lệnh thực thi
```

Ví dụ:
```python
for i in range(5):
    print(i)
```
Kết quả:
```
0
1
2
3
4
```

Hàm `range(n)` tạo ra dãy số từ 0 đến n-1.

Bạn cũng có thể lặp qua danh sách:
```python
danh_sach = ["Táo", "Cam", "Chuối"]
for fruit in danh_sach:
    print("Tôi thích", fruit)
```

### 2. Vòng lặp `while`

Vòng lặp `while` lặp lại một khối lệnh **khi điều kiện còn đúng**.

Cú pháp:
```python
while điều_kiện:
    # các lệnh thực thi
```

Ví dụ:
```python
i = 0
while i < 5:
    print(i)
    i += 1  # tăng i lên 1
```

⚠️ Lưu ý: Bạn phải đảm bảo rằng điều kiện cuối cùng sẽ sai, nếu không vòng lặp sẽ chạy vô hạn!

### So sánh for và while

| `for` | `while` |
|------|--------|
| Dùng khi biết trước số lần lặp | Dùng khi không biết trước số lần lặp |
| Lặp qua dãy (list, string, range) | Lặp khi điều kiện đúng |
| Khó gây lỗi vô hạn | Dễ gây lỗi vô hạn nếu không cập nhật biến |

---

## Ví dụ minh họa

### Ví dụ 1: In các số chẵn từ 0 đến 10

```python
print("Các số chẵn từ 0 đến 10:")
for i in range(0, 11, 2):  # bắt đầu từ 0, đến 10, bước nhảy 2
    print(i)
```

### Ví dụ 2: Đoán số (sử dụng while)

Chương trình chọn số ngẫu nhiên từ 1 đến 10, người dùng đoán cho đến khi đúng.

```python
import random

so_bi_mat = random.randint(1, 10)
print("Tôi đã chọn một số từ 1 đến 10.")

doan = 0
while doan != so_bi_mat:
    doan = int(input("Hãy đoán số: "))
    if doan < so_bi_mat:
        print("Quá nhỏ!")
    elif doan > so_bi_mat:
        print("Quá lớn!")
    else:
        print("Chính xác! Bạn đã thắng!")
```

### Ví dụ 3: In từng ký tự trong chuỗi

```python
chuoi = "Python"
for ky_tu in chuoi:
    print(ky_tu)
```

---

## Bài tập thực hành

1. **In bảng cửu chương 5**
   - Dùng vòng lặp `for` in bảng cửu chương 5 (từ 5x1 đến 5x10).

2. **Tính tổng các số từ 1 đến n**
   - Nhập số nguyên dương n từ người dùng.
   - Dùng vòng lặp `while` để tính tổng các số từ 1 đến n.

3. **Đếm ngược từ 10 về 0**
   - Dùng vòng lặp `for` hoặc `while` để in đếm ngược từ 10 về 0.

4. **In hình vuông ký tự**
   - Nhập kích thước hình vuông (ví dụ: 5).
   - Dùng vòng lặp lồng nhau in ra hình vuông bằng dấu `*`.

5. **Kiểm tra số nguyên tố đơn giản**
   - Nhập một số n.
   - Dùng vòng lặp kiểm tra xem n có phải là số nguyên tố không (chỉ chia hết cho 1 và chính nó).

---

## Tổng kết

Trong bài học này, bạn đã học được:
- Cách dùng vòng lặp `for` để lặp qua dãy số, danh sách, chuỗi.
- Cách dùng vòng lặp `while` để lặp khi điều kiện đúng.
- Phân biệt khi nào dùng `for`, khi nào dùng `while`.
- Ứng dụng vòng lặp vào các tình huống thực tế như đoán số, in bảng cửu chương, đếm ngược.

Vòng lặp là nền tảng để xây dựng các chương trình phức tạp hơn. Hãy luyện tập thật nhiều để làm chủ kỹ năng này!

Hãy chạy file `main.py` để xem các ví dụ, làm bài tập trong `exercises.py`, và tham khảo lời giải trong `solutions.py`.

Chúc bạn học tốt!