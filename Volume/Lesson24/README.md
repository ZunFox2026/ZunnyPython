# Làm việc với thư viện thời gian
## Giới thiệu
Thư viện thời gian là một trong những thư viện quan trọng trong Python, giúp chúng ta làm việc với thời gian và ngày tháng một cách hiệu quả. Thư viện này cung cấp nhiều chức năng khác nhau, từ việc tạo đối tượng thời gian đến việc thực hiện các phép toán trên thời gian. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với thư viện thời gian trong Python.

## Lý thuyết
Thư viện thời gian trong Python được gọi là `datetime`. Đây là một thư viện mạnh mẽ và linh hoạt, cung cấp nhiều lớp và phương thức khác nhau để làm việc với thời gian. Một số lớp quan trọng trong thư viện `datetime` bao gồm:
- `date`: đại diện cho một ngày tháng
- `time`: đại diện cho một thời điểm trong ngày
- `datetime`: đại diện cho một ngày tháng và thời điểm
- `timedelta`: đại diện cho một khoảng thời gian

Chúng ta có thể tạo đối tượng thời gian bằng cách sử dụng các lớp trên. Ví dụ, để tạo một đối tượng `date`, chúng ta có thể sử dụng phương thức `date(year, month, day)`. Tương tự, để tạo một đối tượng `time`, chúng ta có thể sử dụng phương thức `time(hour, minute, second)`.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với thư viện thời gian:
```python
from datetime import date, time, datetime, timedelta

# Tạo một đối tượng date
ngay_hom_nay = date(2024, 9, 16)
print(ngay_hom_nay)

# Tạo một đối tượng time
thoi_gian_hien_tai = time(10, 30, 0)
print(thoi_gian_hien_tai)

# Tạo một đối tượng datetime
thoi_gian_day_du = datetime(2024, 9, 16, 10, 30, 0)
print(thoi_gian_day_du)

# Tính toán khoảng thời gian
khoang_thoi_gian = timedelta(days=7)
ngay_tuan_sau = ngay_hom_nay + khoang_thoi_gian
print(ngay_tuan_sau)
```
## Bài tập
Để thực hành làm việc với thư viện thời gian, hãy thực hiện các bài tập sau:
- Tạo một đối tượng `date` đại diện cho ngày sinh của bạn.
- Tạo một đối tượng `time` đại diện cho thời gian hiện tại.
- Tính toán khoảng thời gian giữa ngày sinh của bạn và ngày hiện tại.
- In ra ngày và tháng của ngày hiện tại.