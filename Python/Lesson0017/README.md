# Python 17: Làm Quen Với Biến và Kiểu Dữ Liệu

## Giới thiệu

Trong lập trình Python, **biến** và **kiểu dữ liệu** là hai khái niệm cơ bản và quan trọng nhất mà mọi người học lập trình cần nắm vững. Biến giúp lưu trữ dữ liệu, còn kiểu dữ liệu xác định loại giá trị mà biến đó có thể chứa. Bài học này sẽ giúp bạn hiểu rõ cách khai báo biến, sử dụng các kiểu dữ liệu phổ biến như số, chuỗi, và kiểu boolean trong Python.

## Lý thuyết

Trong Python, bạn không cần khai báo kiểu dữ liệu khi tạo biến. Python tự động xác định kiểu dựa trên giá trị được gán.

- **Biến**: Là tên dùng để lưu trữ dữ liệu. Tên biến phải bắt đầu bằng chữ cái hoặc gạch dưới, không chứa ký tự đặc biệt.
- **Các kiểu dữ liệu cơ bản**:
  - `int`: số nguyên (ví dụ: `5`, `-3`)
  - `float`: số thực (ví dụ: `3.14`, `-0.5`)
  - `str`: chuỗi ký tự, đặt trong dấu nháy đơn hoặc kép (ví dụ: `"Hello"`)
  - `bool`: giá trị đúng/sai (`True` hoặc `False`)

## Ví dụ

```python
# Khai báo biến và gán giá trị
ten = "An"           # kiểu str
tuoi = 15            # kiểu int
chieu_cao = 1.65     # kiểu float
la_hoc_sinh = True   # kiểu bool

# In thông tin ra màn hình
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
print("Là học sinh:", la_hoc_sinh)
```

**Kết quả:**
```
Tên: An
Tuổi: 15
Chiều cao: 1.65 m
Là học sinh: True
```

## Bài tập

1. Tạo một biến `ho_ten` và gán tên của bạn vào đó, sau đó in ra màn hình.
2. Tạo biến `nam_sinh` và tính toán tuổi hiện tại dựa trên năm hiện tại (ví dụ: 2025 - nam_sinh).
3. Tạo một biến `diem_tb` kiểu float và gán giá trị điểm trung bình học kỳ (ví dụ: 8.7).
4. In ra màn hình toàn bộ thông tin: tên, tuổi, điểm trung bình và một giá trị boolean cho biết bạn có phải học sinh giỏi (điểm >= 8.0) hay không.

> 💡 Gợi ý: Dùng `input()` để nhập tên và năm sinh từ người dùng (sẽ học kỹ hơn ở bài sau).