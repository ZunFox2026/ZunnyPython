# Bài học Python nâng cao số 57: Tối ưu hóa hiệu suất với `functools` và `lru_cache`

Trong bài học này, chúng ta sẽ tìm hiểu cách sử dụng module `functools` – một công cụ mạnh mẽ trong Python – để tối ưu hóa hiệu suất chương trình, đặc biệt là với các hàm đệ quy hoặc các hàm tính toán tốn kém. Chúng ta sẽ tập trung vào decorator `@lru_cache`, một công cụ cực kỳ hiệu quả giúp ghi nhớ (cache) kết quả của các hàm, từ đó tránh việc tính toán lại những giá trị đã từng thực hiện.

## 1. Mục tiêu bài học

- Hiểu được vai trò của module `functools` trong việc xử lý hàm và tối ưu hiệu suất.
- Biết cách sử dụng `@lru_cache` để tối ưu các hàm đệ quy hoặc hàm có tính toán lặp đi lặp lại.
- Áp dụng `@lru_cache` vào các bài toán thực tế như dãy Fibonacci, bài toán quy hoạch động, và xử lý chuỗi.
- Nhận diện các tình huống nên và không nên dùng `@lru_cache`.

## 2. Lý thuyết chi tiết

### 2.1. Giới thiệu về `functools`

Module `functools` trong Python cung cấp các hàm cao cấp để làm việc với các hàm và đối tượng gọi được (callable). Một trong những công cụ mạnh mẽ nhất là `@lru_cache`, giúp lưu trữ kết quả của các lời gọi hàm dựa trên tham số truyền vào.

### 2.2. Cache và LRU (Least Recently Used)

- **Cache** là bộ nhớ tạm lưu trữ kết quả tính toán để sử dụng lại.
- **LRU Cache** là kiểu cache loại bỏ phần tử lâu nhất không được sử dụng khi bộ nhớ đầy.
- `@lru_cache` tự động lưu kết quả của hàm theo bộ tham số, nếu hàm được gọi lại với cùng tham số, nó sẽ trả về kết quả đã lưu mà không cần tính toán lại.

### 2.3. Cú pháp

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def ten_ham(tham_so):
    # logic tính toán
    return ket_qua
```

- `maxsize`: số lượng kết quả tối đa được lưu. Nếu `None`, không giới hạn (cẩn thận với bộ nhớ).
- Chỉ dùng cho các hàm **thuần (pure function)** – cùng đầu vào luôn cho cùng đầu ra, không có side effect.

## 3. Ví dụ minh họa

### Ví dụ 1: Tính số Fibonacci với và không dùng `@lru_cache`

Hàm Fibonacci truyền thống có độ phức tạp mũ do gọi đệ quy nhiều lần với cùng tham số. Dùng `@lru_cache` giúp giảm xuống O(n).

### Ví dụ 2: Đếm số cách đi lên cầu thang

Một người có thể đi 1 hoặc 2 bước mỗi lần. Đếm số cách đi lên bậc thang thứ n. Đây là bài toán quy hoạch động.

### Ví dụ 3: Tính độ dài dãy con chung lớn nhất (LCS)

Một bài toán xử lý chuỗi kinh điển, rất phù hợp để dùng `@lru_cache` do có nhiều lời gọi trùng lặp.

## 4. Bài tập thực hành

1. Viết hàm tính giai thừa đệ quy với `@lru_cache`. So sánh tốc độ với hàm thông thường.
2. Viết hàm đếm số cách phân tích số n thành tổng các số nguyên dương ≥ 1, mỗi cách chỉ dùng các số không giảm.
3. Viết hàm tìm số lượng cách điền ký tự vào một chuỗi để tạo thành chuỗi đối xứng (dựa trên từng vị trí có thể thay đổi).
4. Viết hàm tính tổng các phần tử trong danh sách con lớn nhất (Maximum Subarray) bằng đệ quy và `@lru_cache`.
5. (Nâng cao) Viết hàm kiểm tra xem có thể chia một danh sách số thành 2 nhóm có tổng bằng nhau không (Partition Problem), sử dụng `@lru_cache`.

**Gợi ý:** Dùng `@lru_cache` với tham số là các giá trị không đổi như tuple, số nguyên, chuỗi.

## 5. Tổng kết

- `functools.lru_cache` là công cụ mạnh để tối ưu hiệu suất hàm đệ quy hoặc hàm tính toán nặng.
- Chỉ nên dùng cho hàm thuần, tham số bất biến.
- Cẩn thận với `maxsize` để tránh tràn bộ nhớ.
- Kết hợp tốt với quy hoạch động, xử lý chuỗi, và các bài toán đệ quy phân tách.

Sau bài học này, bạn có thể áp dụng `@lru_cache` để tăng tốc nhiều chương trình Python một cách dễ dàng và hiệu quả.