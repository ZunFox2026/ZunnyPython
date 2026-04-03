# Bài học Python Cấp độ Trung cấp - Bài 14: Làm việc với File JSON

## Mục tiêu bài học
- Hiểu được JSON là gì và tại sao nó được sử dụng phổ biến trong lập trình.
- Biết cách đọc và ghi dữ liệu JSON bằng Python.
- Ứng dụng JSON để lưu trữ và xử lý dữ liệu cấu trúc như danh sách người dùng, cấu hình ứng dụng, dữ liệu API.
- Rèn luyện kỹ năng thao tác với file và xử lý lỗi khi làm việc với JSON.

## Lý thuyết chi tiết

### JSON là gì?
JSON (JavaScript Object Notation) là một định dạng dữ liệu dạng văn bản, dễ đọc và dễ viết, được sử dụng rộng rãi để truyền dữ liệu giữa máy client và server. Trong Python, JSON được biểu diễn tương tự như dictionary và list.

Ví dụ về dữ liệu JSON:
```json
{
  "ten": "An",
  "tuoi": 20,
  "mon_hoc": ["Toán", "Lý", "Hóa"]
}
```

### Đọc và ghi file JSON trong Python
Python cung cấp module `json` để làm việc với dữ liệu JSON.

- `json.dumps()`: Chuyển đối tượng Python thành chuỗi JSON.
- `json.loads()`: Chuyển chuỗi JSON thành đối tượng Python.
- `json.dump()`: Ghi dữ liệu Python vào file JSON.
- `json.load()`: Đọc dữ liệu từ file JSON và chuyển thành đối tượng Python.

### Ví dụ cơ bản
```python
import json

# Ghi dữ liệu ra file JSON
data = {"ten": "Binh", "diem": 8.5}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Đọc dữ liệu từ file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data_doc = json.load(f)
    print(data_doc)
```

## Ví dụ minh họa

### Ví dụ 1: Quản lý danh sách sinh viên
Lưu danh sách sinh viên vào file JSON và đọc lại.

### Ví dụ 2: Cập nhật điểm số sinh viên
Đọc dữ liệu sinh viên, cập nhật điểm một sinh viên, sau đó lưu lại.

### Ví dụ 3: Xử lý dữ liệu từ API giả lập
Tạo một hàm mô phỏng việc nhận dữ liệu từ API ở dạng JSON và xử lý nó.

## Bài tập thực hành
1. Tạo file JSON chứa thông tin sách (tên sách, tác giả, năm xuất bản).
2. Viết hàm tìm kiếm sách theo tên tác giả.
3. Cập nhật năm xuất bản của một cuốn sách trong file JSON.
4. Đọc file JSON và in ra danh sách sách theo định dạng đẹp.
5. Xử lý lỗi khi file JSON không tồn tại.

## Tổng kết
- JSON là định dạng dữ liệu phổ biến, dễ sử dụng trong Python.
- Module `json` giúp đọc/ghi dữ liệu một cách đơn giản.
- Cần xử lý lỗi khi thao tác với file để chương trình ổn định.
- Ứng dụng JSON trong lưu cấu hình, trao đổi dữ liệu API, quản lý dữ liệu nhỏ.

Hãy thực hành các bài tập để nắm vững kỹ năng làm việc với JSON!