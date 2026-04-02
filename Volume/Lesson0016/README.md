# Làm việc với thời gian
Bài học này sẽ hướng dẫn bạn cách làm việc với thời gian trong Python, bao gồm cách hiển thị thời gian, tính toán thời gian và sử dụng các thư viện thời gian.

## Giới thiệu
Thời gian là một phần quan trọng trong lập trình, và Python cung cấp nhiều cách để làm việc với thời gian. Trong bài học này, bạn sẽ học cách hiển thị thời gian, tính toán thời gian và sử dụng các thư viện thời gian.

## Lý thuyết
Python cung cấp nhiều cách để làm việc với thời gian, bao gồm:
- Sử dụng hàm `time()` từ thư viện `time` để lấy thời gian hiện tại.
- Sử dụng hàm `datetime()` từ thư viện `datetime` để tạo đối tượng thời gian.
- Sử dụng hàm `timedelta()` từ thư viện `datetime` để tính toán thời gian.

Thư viện `time` cung cấp các hàm để lấy thời gian hiện tại, chẳng hạn như `time()`, `gmtime()`, `localtime()`. Thư viện `datetime` cung cấp các lớp để tạo đối tượng thời gian, chẳng hạn như `datetime`, `date`, `time`.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với thời gian trong Python:
- Hiển thị thời gian hiện tại:
  ```python
import time
print(time.time())
```
- Tạo đối tượng thời gian:
  ```python
import datetime
now = datetime.datetime.now()
print(now)
```
- Tính toán thời gian:
  ```python
import datetime
now = datetime.datetime.now()
future = now + datetime.timedelta(days=1)
print(future)
```

## Bài tập
Bài tập này sẽ giúp bạn thực hành làm việc với thời gian trong Python. Hãy thực hiện các nhiệm vụ sau:
- Viết một chương trình để hiển thị thời gian hiện tại.
- Viết một chương trình để tạo đối tượng thời gian và hiển thị thông tin về thời gian đó.
- Viết một chương trình để tính toán thời gian sau 1 ngày, 1 tuần, 1 tháng từ thời gian hiện tại.
- Viết một chương trình để so sánh thời gian giữa hai ngày khác nhau.

Với những kiến thức và ví dụ trên, bạn đã có thể làm việc với thời gian trong Python. Hãy thực hành và áp dụng những kiến thức này vào các dự án thực tế của mình.