# Bài học 5: List và các thao tác cơ bản

Chào mừng bạn đến với Bài học 5 trong khóa học Python dành cho người mới bắt đầu! Trong bài học này, bạn sẽ tìm hiểu về **List** — một trong những cấu trúc dữ liệu quan trọng và thường dùng nhất trong Python.

List cho phép bạn lưu trữ nhiều giá trị trong một biến duy nhất. Bạn có thể thêm, bớt, thay đổi và truy cập các phần tử một cách dễ dàng. Đây là nền tảng để xử lý dữ liệu trong các chương trình thực tế như quản lý danh sách học sinh, danh sách mua sắm, điểm số, v.v.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu được List là gì và tại sao nó hữu ích
- Tạo và truy cập các phần tử trong List
- Thực hiện các thao tác cơ bản: thêm, xóa, sửa, tìm kiếm phần tử
- Áp dụng List vào các tình huống thực tế

---

## Lý thuyết chi tiết

### 1. List là gì?

List (danh sách) là một tập hợp có thứ tự, có thể thay đổi (mutable) và cho phép phần tử trùng lặp. Các phần tử trong list được ngăn cách bởi dấu phẩy và nằm trong dấu ngoặc vuông `[]`.

**Ví dụ:**
```python
fruits = ["táo", "chuối", "cam"]
diem = [8, 9, 7, 10]
mixed = ["Alice", 25, True, 8.5]
```

### 2. Truy cập phần tử trong List

Bạn có thể truy cập phần tử bằng chỉ số (index). Chỉ số bắt đầu từ 0.

- `list[0]` → phần tử đầu tiên
- `list[-1]` → phần tử cuối cùng

**Ví dụ:**
```python
fruits = ["táo", "chuối", "cam"]
print(fruits[0])   # In ra: táo
print(fruits[-1])  # In ra: cam
```

### 3. Các thao tác cơ bản

| Thao tác | Cú pháp | Mô tả |
|--------|--------|------|
| Thêm phần tử | `list.append(x)` | Thêm x vào cuối list |
| Chèn phần tử | `list.insert(i, x)` | Chèn x vào vị trí i |
| Xóa phần tử | `list.remove(x)` | Xóa phần tử đầu tiên có giá trị x |
| Xóa theo chỉ số | `del list[i]` hoặc `list.pop(i)` | Xóa phần tử tại vị trí i |
| Sửa phần tử | `list[i] = x` | Gán giá trị mới cho phần tử tại vị trí i |
| Tìm kiếm | `x in list` | Kiểm tra x có trong list không |
| Độ dài list | `len(list)` | Trả về số lượng phần tử |

---

## Ví dụ minh họa

### Ví dụ 1: Quản lý danh sách mua sắm

Tạo một chương trình đơn giản để thêm, hiển thị và xóa món đồ khỏi danh sách mua sắm.

### Ví dụ 2: Tính điểm trung bình học sinh

Lưu trữ điểm số của một học sinh và tính điểm trung bình.

### Ví dụ 3: Tìm phần tử lớn nhất trong danh sách

Tìm số lớn nhất trong danh sách số bằng cách duyệt qua list.

---

## Bài tập thực hành

1. Tạo danh sách tên bạn bè và in ra người đầu tiên, người cuối cùng.
2. Viết chương trình thêm 3 món ăn vào danh sách yêu thích, sau đó xóa một món bất kỳ.
3. Nhập 5 số từ bàn phím, lưu vào list và in ra tổng các số.
4. Đếm số lần xuất hiện của một giá trị trong list.
5. Đảo ngược thứ tự các phần tử trong list mà không dùng hàm reverse().

> 💡 Gợi ý: Sử dụng vòng lặp `for`, các hàm như `append()`, `remove()`, `len()` và chỉ số âm.

---

## Tổng kết

List là công cụ mạnh mẽ để lưu trữ và xử lý nhiều giá trị cùng lúc. Trong bài học này, bạn đã học cách:
- Tạo và truy cập list
- Thực hiện các thao tác thêm, xóa, sửa, tìm kiếm
- Ứng dụng list vào các tình huống đời thực

Hãy luyện tập thường xuyên để thành thạo các thao tác với list — vì đây là nền tảng cho các bài học tiếp theo như vòng lặp, hàm và xử lý dữ liệu.

Chúc bạn học tốt!
