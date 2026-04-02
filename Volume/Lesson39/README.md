# Tìm phần tử lớn nhất
Bài này sẽ hướng dẫn bạn cách tìm phần tử lớn nhất trong một danh sách số.

## Giới thiệu
Trong nhiều trường hợp, chúng ta cần tìm phần tử lớn nhất trong một danh sách số. Ví dụ, tìm điểm số cao nhất trong một lớp học, tìm giá trị lớn nhất trong một tập dữ liệu, v.v. Bài này sẽ giới thiệu cách sử dụng Python để tìm phần tử lớn nhất trong một danh sách số.

## Lý thuyết
Để tìm phần tử lớn nhất trong một danh sách số, chúng ta có thể sử dụng hàm `max()` trong Python. Hàm `max()` sẽ trả về giá trị lớn nhất trong một danh sách. Ngoài ra, chúng ta cũng có thể sử dụng vòng lặp để tìm phần tử lớn nhất.

Ví dụ, nếu chúng ta có một danh sách số như sau: `[1, 3, 5, 7, 9]`, chúng ta có thể sử dụng hàm `max()` để tìm phần tử lớn nhất:
```python
danh_sach = [1, 3, 5, 7, 9]
pham_vi_lon_nhat = max(danh_sach)
print(pham_vi_lon_nhat)  # Output: 9
```
Hoặc chúng ta có thể sử dụng vòng lặp để tìm phần tử lớn nhất:
```python
danh_sach = [1, 3, 5, 7, 9]
pham_vi_lon_nhat = danh_sach[0]
for phan_tu in danh_sach:
    if phan_tu > pham_vi_lon_nhat:
        pham_vi_lon_nhat = phan_tu
print(pham_vi_lon_nhat)  # Output: 9
```
## Ví dụ
Chúng ta có một danh sách số như sau: `[2, 4, 6, 8, 10]`. Hãy tìm phần tử lớn nhất trong danh sách này.

Sử dụng hàm `max()`:
```python
danh_sach = [2, 4, 6, 8, 10]
pham_vi_lon_nhat = max(danh_sach)
print(pham_vi_lon_nhat)  # Output: 10
```
Sử dụng vòng lặp:
```python
danh_sach = [2, 4, 6, 8, 10]
pham_vi_lon_nhat = danh_sach[0]
for phan_tu in danh_sach:
    if phan_tu > pham_vi_lon_nhat:
        pham_vi_lon_nhat = phan_tu
print(pham_vi_lon_nhat)  # Output: 10
```
## Bài tập
Cho một danh sách số như sau: `[5, 3, 1, 4, 2]`. Hãy tìm phần tử lớn nhất trong danh sách này bằng cách sử dụng hàm `max()` và vòng lặp. Sau đó, hãy in ra kết quả.