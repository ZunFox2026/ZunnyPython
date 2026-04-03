# Bài học Python Nâng cao số 90: Tối ưu hóa hiệu suất với `functools.lru_cache`

## 1. Mục tiêu bài học
- Hiểu được khái niệm **memoization** và vai trò của nó trong việc tối ưu hiệu suất.
- Biết cách sử dụng decorator `@lru_cache` từ module `functools` để tối ưu các hàm đệ quy hoặc các hàm tính toán tốn kém.
- Áp dụng `lru_cache` vào các bài toán thực tế như tính số Fibonacci, tổ hợp, tra cứu dữ liệu lặp lại.
- Nhận diện được các trường hợp phù hợp và không phù hợp để sử dụng `lru_cache`.

## 2. Lý thuyết chi tiết

### 2.1. Memoization là gì?
Memoization là kỹ thuật lưu trữ kết quả của các lời gọi hàm dựa trên các tham số đầu vào. Khi hàm được gọi lại với cùng tham số, thay vì tính toán lại, chương trình sẽ trả về kết quả đã lưu. Điều này giúp giảm đáng kể thời gian thực thi, đặc biệt với các hàm đệ quy.

### 2.2. `@lru_cache` trong Python
Python cung cấp decorator `@lru_cache` trong module `functools` để tự động thực hiện memoization. LRU (Least Recently Used) là cơ chế thay thế bộ nhớ đệm: khi bộ nhớ đầy, giá trị ít được dùng nhất sẽ bị xóa.

**Cú pháp:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def ten_ham():
    ...
```

- `maxsize`: số lượng kết quả tối đa được lưu. Nếu là `None`, bộ nhớ đệm không giới hạn (cẩn thận với bộ nhớ).
- Hàm được decorate **phải là hàm thuần (pure function)** – kết quả chỉ phụ thuộc vào tham số, không có side effect.

### 2.3. Khi nào nên dùng `lru_cache`?
- Hàm có tính toán tốn kém (đệ quy, xử lý số học phức tạp).
- Cùng đầu vào được gọi nhiều lần.
- Hàm không có trạng thái thay đổi (không phụ thuộc biến toàn cục thay đổi).

### 2.4. Khi nào không nên dùng?
- Hàm có side effect (in ra màn hình, thay đổi file, thay đổi biến toàn cục).
- Tham số không hashable (list, dict).
- Bộ nhớ đệm quá lớn ảnh hưởng hiệu năng.

## 3. Ví dụ minh họa

### Ví dụ 1: Tính số Fibonacci
Hàm đệ quy thông thường rất chậm do tính đi tính lại nhiều lần. Dùng `lru_cache` giúp tăng tốc đáng kể.

### Ví dụ 2: Tính tổ hợp C(n, k)
Tổ hợp cũng là hàm đệ quy, có nhiều lời gọi trùng. Memoization giúp tối ưu.

### Ví dụ 3: Hàm tra cứu giá sản phẩm với phí xử lý ảo
Giả lập hàm tốn thời gian (sleep), dùng `lru_cache` để tránh lặp lại xử lý.

## 4. Bài tập thực hành
1. Viết hàm tính dãy Lucas (giống Fibonacci nhưng bắt đầu bằng 2, 1) với `lru_cache`.
2. Viết hàm đệ quy tính tổng các phần tử trong dãy số Fibonacci từ 1 đến n, tối ưu bằng `lru_cache`.
3. Viết hàm kiểm tra số nguyên tố, dùng `lru_cache` để lưu kết quả. Nhận xét hiệu quả.
4. Viết hàm `word_count(sentence)` đếm số từ, dùng `lru_cache`. Giải thích tại sao có thể/không dùng được.

## 5. Tổng kết
`@lru_cache` là công cụ mạnh để tối ưu hiệu suất trong Python, đặc biệt với các hàm đệ quy hoặc hàm có tính toán lặp lại. Tuy nhiên, cần hiểu rõ khi nào nên và không nên dùng để tránh lỗi hoặc lãng phí tài nguyên. Việc sử dụng đúng cách giúp chương trình vừa nhanh hơn, vừa dễ đọc hơn.

> ✅ **Lưu ý**: Luôn kiểm tra tính **hashable** của tham số và đảm bảo hàm là **pure function** khi dùng `lru_cache`.