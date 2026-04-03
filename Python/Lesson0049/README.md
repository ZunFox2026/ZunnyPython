# Python 49 - Xử Lý Chuỗi và Hàm Cơ Bản

## Giới thiệu

Trong lập trình Python, xử lý chuỗi là một kỹ năng cơ bản và quan trọng. Chuỗi (string) là kiểu dữ liệu được sử dụng để lưu trữ văn bản, và Python cung cấp nhiều hàm và phương thức tích hợp giúp thao tác với chuỗi một cách dễ dàng. Bài học này sẽ giới thiệu các thao tác cơ bản như nối chuỗi, trích xuất ký tự, thay đổi định dạng và sử dụng một số hàm phổ biến như `len()`, `upper()`, `lower()`, `replace()`, `split()`...

## Lý thuyết

Một chuỗi trong Python là một dãy ký tự được bao bởi cặp dấu nháy đơn (`'...'`) hoặc nháy kép (`"..."`). Một số hàm và phương thức thường dùng:

- `len(s)`: trả về độ dài chuỗi.
- `s.upper()`: chuyển tất cả ký tự thành chữ in hoa.
- `s.lower()`: chuyển về chữ thường.
- `s.replace(old, new)`: thay thế chuỗi con.
- `s.split(delim)`: tách chuỗi theo ký tự phân cách.
- `s.strip()`: loại bỏ khoảng trắng ở đầu và cuối.

## Ví dụ

```python
# Ví dụ xử lý chuỗi cơ bản
ten = "Nguyen Van An"
print("Chuỗi gốc:", ten)

# In hoa toàn bộ
print("In hoa:", ten.upper())

# In thường
print("In thường:", ten.lower())

# Độ dài chuỗi
print("Độ dài:", len(ten))

# Thay thế từ
moi = ten.replace("Van", "Thi")
print("Sau khi thay thế:", moi)

# Tách chuỗi
danh_sach = ten.split(" ")
print("Tách theo khoảng trắng:", danh_sach)
```

**Kết quả:**
```
Chuỗi gốc: Nguyen Van An
In hoa: NGUYEN VAN AN
In thường: nguyen van an
Độ dài: 14
Sau khi thay thế: Nguyen Thi An
Tách theo khoảng trắng: ['Nguyen', 'Van', 'An']
```

## Bài tập

1. Nhập vào một chuỗi từ người dùng và in ra độ dài của chuỗi đó.
2. Viết chương trình chuyển chuỗi nhập vào thành chữ in hoa và in kết quả.
3. Thay thế tất cả ký tự khoảng trắng trong chuỗi bằng dấu gạch dưới `_`.
4. Tách một câu thành danh sách các từ, rồi in từng từ ra màn hình.

> Gợi ý: Dùng `input()` để nhận dữ liệu, kết hợp các phương thức xử lý chuỗi đã học.