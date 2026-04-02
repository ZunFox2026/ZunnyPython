# Tìm số lớn nhất
## Giới thiệu
Bài "Tìm số lớn nhất" là một trong những bài cơ bản trong chương trình học Python. Mục tiêu của bài học này là giúp học viên hiểu cách tìm số lớn nhất trong một danh sách các số. Đây là một kỹ năng quan trọng trong lập trình, vì nó thường được sử dụng trong nhiều ứng dụng khác nhau, từ tìm kiếm số lớn nhất trong một tập dữ liệu đến xác định giá trị tối đa trong một phạm vi.

## Lý thuyết
Để tìm số lớn nhất trong một danh sách, chúng ta có thể sử dụng hàm `max()` trong Python. Hàm này sẽ trả về giá trị lớn nhất trong một tập hợp các giá trị. Ngoài ra, chúng ta cũng có thể sử dụng vòng lặp để so sánh từng giá trị trong danh sách và tìm ra giá trị lớn nhất.

Cú pháp của hàm `max()` như sau:
```python
max(danh_sach)
```
Trong đó, `danh_sach` là một tập hợp các giá trị.

Ví dụ, nếu chúng ta có một danh sách các số `[1, 2, 3, 4, 5]`, chúng ta có thể sử dụng hàm `max()` để tìm số lớn nhất như sau:
```python
so_lon_nhat = max([1, 2, 3, 4, 5])
print(so_lon_nhat)  # Output: 5
```
## Ví dụ
Dưới đây là một ví dụ minh họa về cách tìm số lớn nhất trong một danh sách:
```python
# Định nghĩa một danh sách các số
danh_sach_so = [10, 20, 30, 40, 50]

# Tìm số lớn nhất trong danh sách
so_lon_nhat = max(danh_sach_so)

# In ra số lớn nhất
print("Số lớn nhất là:", so_lon_nhat)
```
Kết quả của ví dụ trên sẽ là `Số lớn nhất là: 50`.

## Bài tập
Bài tập dưới đây sẽ giúp bạn thực hành tìm số lớn nhất trong một danh sách:

* Định nghĩa một danh sách các số tự nhiên.
* Tìm số lớn nhất trong danh sách bằng cách sử dụng hàm `max()`.
* In ra số lớn nhất.
* Thử thay đổi danh sách các số và thực hiện lại bài tập để kiểm tra kết quả.

Ví dụ, bạn có thể định nghĩa một danh sách các số như sau:
```python
danh_sach_so = [25, 36, 49, 64, 81]
```
Sau đó, bạn có thể tìm số lớn nhất trong danh sách bằng cách sử dụng hàm `max()`:
```python
so_lon_nhat = max(danh_sach_so)
print("Số lớn nhất là:", so_lon_nhat)
```
Kết quả sẽ là `Số lớn nhất là: 81`.