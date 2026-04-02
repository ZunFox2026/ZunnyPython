# README – Bài 11 (Cơ bản): **Xử lý danh sách và vòng lặp trong Python**

---

## Giới thiệu  
Bài 11 là một phần của khóa học lập trình Python cấp **Cơ bản**, tập trung vào việc **xử lý danh sách (list)** và **sử dụng vòng lặp** để thực hiện các thao tác phổ biến như duyệt, lọc, biến đổi và tổng hợp dữ liệu. Khi hoàn thành bài này, bạn sẽ biết cách:

- Tạo và truy cập danh sách bằng các chỉ số và phương thức nội建.  
- Dùng vòng lặp `for` và `while` để lặp qua các phần tử.  
- Áp dụng các hàm tích hợp (`len`, `sum`, `max`, `min`, `sorted`) và list comprehension để viết mã ngắn gọn, hiệu quả.  
- Giải quyết các bài tập thực tế như thống kê điểm số, lọc chuỗi, hoặc tính toán ma trận đơn giản.

---

## Lý thuyết  

### 1. Danh sách (list) trong Python  
- Là một **các đối tượng có thứ tự**, thay đổi được (mutable).  
- Khai báo bằng dấu ngoặc vuông: `my_list = [1, 2, 3]` hoặc `my_list = []`.  
- Truy cập phần tử qua chỉ số (bắt đầu từ 0): `my_list[0]`.  
- Các phương thức thường dùng: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, `reverse()`.  

### 2. Vòng lặp `for`  
- Dùng để lặp qua từng phần tử của một iterable (list, tuple, string, range…).  
- Cú pháp:  
  ```python
  for bien in iterable:
      # thân vòng lặp
  ```  
- Có thể kèm `else` (thực hiện khi vòng lặp kết thúc mà không gặp `break`).  

### 3. Vòng lặp `while`  
- Lặp miễn là điều kiện còn đúng.  
- Cú pháp:  
  ```python
  while dieu_kien:
      # thân vòng lặp
  ```  
- Cẩn thận với vòng lặp vô hạn – luôn cập nhật biến điều kiện.  

### 4. List comprehension  
- Cách viết ngắn gọn để tạo danh sách mới từ một iterable có thể có điều kiện lọc.  
- Cú pháp: `[bieu_thuc for bien in iterable if dieu_kien]`.  

---

## Ví dụ  

**Yêu cầu:** Cho danh sách điểm số của lớp. Tính điểm trung bình, đếm số sinh viên đạt điểm ≥ 8 và tạo danh sách mới chứa chỉ những điểm chẵn.

```python
# Danh sách điểm số (0-10)
diem = [7, 9, 5, 8, 6, 10, 4, 8, 3, 9]

# 1. Điểm trung moyenne
trung_binh = sum(diem) / len(diem)
print(f"Điểm trung bình: {trung_binh:.2f}")

# 2. Đếm sinh viên có điểm >= 8
so_sv_cao = sum(1 for d in diem if d >= 8)
print(f"Số sinh viên điểm ≥ 8: {so_sv_cao}")

# 3. Danh sách điểm chẵn (lọc bằng list comprehension)
diems_chan = [d for d in diem if d % 2 == 0]
print(f"Điểm chẵn: {diems_chan}")

# 4. Sắp xếp danh sách tăng dần (không thay đổi danh sách gốc)
diem_sap_xep = sorted(diem)
print(f"Danh sách sau khi sắp xếp: {diem_sap_xep}")
```

**Kết quả chạy:**  
```
Điểm trung bình: 6.90
Số sinh viên điểm ≥ 8: 4
Điểm chẵn[