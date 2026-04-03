# Bài học 4: Hàm và Tham số trong Python

Chào mừng bạn đến với bài học thứ 4 trong khóa học Python cơ bản! Trong bài học này, chúng ta sẽ tìm hiểu về **hàm (function)** và **tham số (parameter)** — một trong những khái niệm quan trọng nhất khi lập trình, giúp bạn viết code rõ ràng, tái sử dụng được và dễ bảo trì.

## 🎯 Mục tiêu bài học
Sau bài học này, bạn sẽ có thể:
- Hiểu được hàm là gì và tại sao cần dùng hàm.
- Biết cách định nghĩa và gọi một hàm trong Python.
- Sử dụng tham số và đối số khi làm việc với hàm.
- Viết hàm có trả về giá trị bằng lệnh `return`.
- Áp dụng hàm vào các tình huống thực tế.

---

## 📚 Lý thuyết chi tiết

### 1. Hàm là gì?
Hàm (function) là một khối lệnh thực hiện một nhiệm vụ cụ thể. Khi bạn định nghĩa một hàm, bạn có thể gọi nó nhiều lần mà không cần viết lại mã.

Ví dụ: Thay vì viết cùng đoạn mã in lời chào nhiều lần, bạn có thể đóng gói nó vào một hàm và gọi khi cần.

### 2. Cú pháp định nghĩa hàm
```python
# Định nghĩa hàm
def ten_ham():
    # Các câu lệnh thực hiện
    print("Xin chào!")

# Gọi hàm
ten_ham()
```

### 3. Tham số và đối số
- **Tham số (parameter)**: là biến được khai báo trong dấu ngoặc đơn khi định nghĩa hàm.
- **Đối số (argument)**: là giá trị bạn truyền vào khi gọi hàm.

Ví dụ:
```python
def xin_chao(ten):
    print(f"Xin chào {ten}!")

xin_chao("An")  # "An" là đối số
```

### 4. Giá trị trả về (return)
Hàm có thể trả về một giá trị bằng lệnh `return`. Giá trị này có thể được lưu vào biến hoặc sử dụng trong biểu thức.

```python
def cong(a, b):
    return a + b

ket_qua = cong(3, 5)
print(ket_qua)  # In ra 8
```

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Hàm chào hỏi với tên
```python
def chao_ten(ten):
    print(f"Chào bạn {ten}! Rất vui được gặp bạn.")

chao_ten("Lan")
```

### Ví dụ 2: Hàm tính diện tích hình chữ nhật
```python
def tinh_dien_tich(chieu_dai, chieu_rong):
    dien_tich = chieu_dai * chieu_rong
    return dien_tich

# Gọi hàm
dien_tich = tinh_dien_tich(10, 5)
print(f"Diện tích hình chữ nhật: {dien_tich}")
```

### Ví dụ 3: Hàm kiểm tra số chẵn/lẻ
```python
def kiem_tra_chan_le(so):
    if so % 2 == 0:
        return "chẵn"
    else:
        return "lẻ"

print(kiem_tra_chan_le(7))  # In ra "lẻ"
print(kiem_tra_chan_le(4))  # In ra "chẵn"
```

---

## ✍️ Bài tập thực hành

1. **Viết hàm chào hỏi cá nhân hóa**
   - Viết hàm `chao_hoi(ho, ten)` nhận họ và tên, in ra lời chào như: "Chào bạn Nguyễn Văn Nam!"

2. **Tính điểm trung bình**
   - Viết hàm `tinh_diem_trung_binh(toan, ly, hoa)` tính và trả về điểm trung bình của 3 môn.

3. **Kiểm tra độ dài mật khẩu**
   - Viết hàm `kiem_tra_mat_khau(mat_khau)` trả về `True` nếu mật khẩu dài ít nhất 8 ký tự, ngược lại trả về `False`.

4. **Tính tuổi từ năm sinh**
   - Viết hàm `tinh_tuoi(nam_sinh)` trả về tuổi hiện tại (giả sử năm nay là 2025).

5. **Hàm in menu**
   - Viết hàm `in_menu()` in ra một menu đơn giản (ví dụ: 1. Thêm, 2. Sửa, 3. Xóa, 0. Thoát).

> 💡 Gợi ý: Dùng lệnh `return` khi cần trả về giá trị, dùng `print()` khi chỉ cần hiển thị.

---

## 🧠 Tổng kết
- Hàm giúp tái sử dụng mã, tránh lặp lại.
- Dùng `def` để định nghĩa hàm.
- Tham số giúp hàm linh hoạt hơn với các giá trị đầu vào.
- Dùng `return` để trả kết quả từ hàm.
- Hàm không nhất thiết phải có tham số hoặc trả về giá trị.

Hãy luyện tập thường xuyên để làm chủ kỹ năng viết hàm — nền tảng cho mọi chương trình Python!
