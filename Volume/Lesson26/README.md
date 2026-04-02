# Làm việc với thời gian
## Giới thiệu
Làm việc với thời gian là một phần quan trọng trong lập trình, giúp chúng ta có thể thực hiện các tác vụ theo thời gian thực, theo lịch trình hoặc theo yêu cầu. Trong Python, chúng ta có thể sử dụng các thư viện như `time`, `datetime` để làm việc với thời gian. Bài này sẽ giới thiệu về cách sử dụng các thư viện này và cung cấp các ví dụ minh họa.

## Lý thuyết
Thư viện `time` cung cấp các hàm để làm việc với thời gian, bao gồm:
- `time()`: trả về thời gian hiện tại tính theo số giây từ ngày 1/1/1970.
- `sleep()`: tạm dừng chương trình trong một khoảng thời gian nhất định.
- `localtime()`: trả về thông tin về thời gian hiện tại tại máy tính cục bộ.

Thư viện `datetime` cung cấp các lớp để làm việc với thời gian, bao gồm:
- `date`: biểu diễn một ngày tháng năm.
- `time`: biểu diễn một thời gian trong ngày.
- `datetime`: biểu diễn một ngày tháng năm và thời gian.

## Ví dụ
Ví dụ về cách sử dụng thư viện `time`:
```python
import time
print("Thời gian hiện tại:", time.time())
time.sleep(2)  # tạm dừng chương trình trong 2 giây
print("Thời gian hiện tại sau khi tạm dừng:", time.time())
```
Ví dụ về cách sử dụng thư viện `datetime`:
```python
from datetime import datetime
now = datetime.now()
print("Thời gian hiện tại:", now)
print("Ngày tháng năm:", now.date())
print("Giờ phút giây:", now.time())
```
## Bài tập
Bài tập 1: Viết chương trình in ra thời gian hiện tại và tạm dừng trong 5 giây.
Bài tập 2: Viết chương trình in ra ngày tháng năm hiện tại và thời gian hiện tại.
Bài tập 3: Viết chương trình tính toán thời gian chênh lệch giữa hai thời điểm.