```markdown
<div align="center">
  <img src="image/zunny.png" alt="Zunny Python" width="180" style="border-radius: 50%; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
  
  # 🐍 ZunnyPython – Học Python cùng Zunny
  
  **Từ zero đến hero với Python – Dự án mã nguồn mở của Zun Technologies**
  
  ![](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
  ![](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
  ![](https://img.shields.io/badge/Status-Học%20mỗi%20ngày-brightgreen?style=for-the-badge)
  ![](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-cyan?style=for-the-badge)
  
</div>

---

## 📖 Giới thiệu

**ZunnyPython** là lộ trình học Python miễn phí, được thiết kế dành cho **người mới bắt đầu** và những ai muốn **nâng cao kỹ năng lập trình**. Dưới sự dẫn dắt của **Zunny** – linh vật công nghệ của Zun Technologies, bạn sẽ chinh phục Python qua hàng loạt ví dụ thực tế, bài tập đa dạng và dự án thú vị.

> *"Python dễ như ăn bánh, chỉ cần bạn có Zunny chỉ đường!"* – 🦊☁️

---

## 🎯 Bạn sẽ học được gì?

- ✅ Cú pháp Python từ cơ bản đến nâng cao  
- ✅ Cấu trúc dữ liệu (list, tuple, dict, set)  
- ✅ Lập trình hướng đối tượng (OOP)  
- ✅ Xử lý file, ngoại lệ  
- ✅ Làm việc với API, JSON  
- ✅ Tự động hóa tác vụ với Python  
- ✅ Xây dựng ứng dụng CLI, web scraper đơn giản  

---

## 🚀 Bắt đầu nhanh

```bash
# Clone repository
git clone https://github.com/ZunFox20/ZunnyPython.git
cd ZunnyPython

# Chạy thử chương trình đầu tiên
python lessons/00_hello_world.py
```

Yêu cầu: Python 3.8 trở lên. Tải tại python.org (nhớ tick "Add Python to PATH").

---

📚 Nội dung chi tiết

Bài Chủ đề Code mẫu
00 Hello World & cài đặt print("Hello Zunny!")
01 Biến, kiểu dữ liệu name = "Zunny"; age = 3
02 Nhập/xuất dữ liệu input("Tên bạn: ")
03 Câu lệnh rẽ nhánh if, elif, else
04 Vòng lặp for, while
05 Hàm cơ bản def chao():
06 List, Tuple my_list = [1,2,3]
07 Dict, Set {"key":"value"}
08 Xử lý chuỗi nâng cao split(), join(), strip()
09 Đọc/ghi file open(), read(), write()
10 Xử lý ngoại lệ try/except/finally
11 Module và Package import math
12 OOP – Class & Object class Zunny:
13 Kế thừa, đa hình class ConCa(Zunny):
14 Decorator @staticmethod
15 Generator yield
16 Làm việc với JSON json.loads()
17 Gọi API bằng requests requests.get()
18 Web scraping cơ bản BeautifulSoup
19 Tự động hóa file, thư mục os, shutil
20 Dự án 1: Todo CLI todo.py
21 Dự án 2: Quản lý sinh viên student_manager.py
22 Dự án 3: Lấy tỷ giá USD exchange_rate.py

📂 Mỗi bài học đều có file .py riêng trong thư mục lessons/ và projects/.

---

💻 Code mẫu nổi bật

1. Đọc file và xử lý ngoại lệ

```python
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Không tìm thấy file!")
except Exception as e:
    print(f"Lỗi: {e}")
```

2. Lấy dữ liệu từ API

```python
import requests

response = requests.get('https://api.github.com/repos/ZunFox20/ZunnyPython')
if response.status_code == 200:
    data = response.json()
    print(f"Stars: {data['stargazers_count']}")
else:
    print("Gọi API thất bại")
```

3. Lớp Zunny đơn giản

```python
class Zunny:
    def __init__(self, name):
        self.name = name
    
    def teach(self, lesson):
        print(f"🦊 {self.name} đang dạy: {lesson}")
    
    def say_hello(self):
        return f"Xin chào, mình là {self.name}!"

z = Zunny("Zunny")
print(z.say_hello())
z.teach("Python OOP")
```

4. List comprehension thông minh

```python
numbers = [1, 2, 3, 4, 5]
squared_even = [x**2 for x in numbers if x % 2 == 0]
print(squared_even)  # [4, 16]
```

---

🛠️ Cách học hiệu quả

1. Clone repo về máy.
2. Chạy từng file trong thư mục lessons/ theo thứ tự.
3. Đọc comment trong code – mình giải thích rất chi tiết.
4. Sửa code, thử nghiệm – cách nhanh nhất để nhớ.
5. Làm bài tập (có đáp án trong thư mục solutions/).
6. Đặt câu hỏi qua Telegram bot hoặc email.

---

🤝 Đóng góp

Dự án được xây dựng bởi cộng đồng, cho cộng đồng. Bạn có thể:

· Báo lỗi hoặc đề xuất bài học mới qua Issues.
· Gửi Pull Request cải thiện nội dung.
· Dịch sang ngôn ngữ khác.
· Chia sẻ với bạn bè!

---

📫 Liên hệ & Hỗ trợ

· Telegram Bot: @Zunnycloud_bot – hỗ trợ tự động 24/7
· Email: zunny932@gmail.com
· GitHub Issues: Tạo issue mới

---

📜 Giấy phép

MIT © 2026 Zun Technologies – Mã nguồn mở, tự do sử dụng và phát triển.

---

<div align="center">
  <sub>Made with ☁️ and 💙 by <strong>Zun Technologies</strong> – where Zunny lives.</sub>
</div>
```
