# Python 21 cấp Cơ bản - Bài học đầu tiên: Cú pháp cơ bản và cấu trúc điều khiển
# File: python_basic_lesson.py
# Mục tiêu: Hiểu các khái niệm cơ bản: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm

def main():
    # --- 1. Biến và kiểu dữ liệu cơ bản ---
    print("=== Bài 1: Biến và Kiểu dữ liệu ===")
    
    # Biến số nguyên
    tuoi = 20
    print(f"Tuổi của tôi là: {tuoi}")
    
    # Biến số thực
    chieu_cao = 1.75
    print(f"Chiều cao: {chieu_cao} mét")
    
    # Biến chuỗi
    ten = "Minh"
    print(f"Xin chào, tôi tên là {ten}")
    
    # Biến boolean
    da_tot_nghiep = True
    print(f"Đã tốt nghiệp: {da_tot_nghiep}")

    # --- 2. Câu điều kiện (if-elif-else) ---
    print("\n=== Bài 2: Câu điều kiện ===")
    
    diem = 85
    
    if diem >= 90:
        xep_loai = "Xuất sắc"
    elif diem >= 80:
        xep_loai = "Giỏi"
    elif diem >= 70:
        xep_loai = "Khá"
    else:
        xep_loai = "Trung bình"
    
    print(f"Với số điểm {diem}, xếp loại: {xep_loai}")
    
    # Ví dụ 2: Kiểm tra số chẵn/lẻ
    so = 12
    if so % 2 == 0:
        print(f"{so} là số chẵn")
    else:
        print(f"{so} là số lẻ")

    # --- 3. Vòng lặp for và while ---
    print("\n=== Bài 3: Vòng lặp ===")
    
    # Vòng lặp for: in các số từ 1 đến 5
    print("In số từ 1 đến 5:")
    for i in range(1, 6):
        print(f"Số: {i}")
    
    # Vòng lặp while: đếm ngược từ 3
    print("Đếm ngược từ 3:")
    dem = 3
    while dem > 0:
        print(f"{dem}...")
        dem -= 1
    print("Hết giờ!")

    # --- 4. Hàm đơn giản ---
    print("\n=== Bài 4: Định nghĩa hàm ===")
    
    # Hàm tính bình phương
    def binh_phuong(n):
        """Trả về bình phương của số n"""
        return n ** 2
    
    # Hàm chào người dùng
    def chao_ten(ten):
        """In lời chào theo tên"""
        print(f"Xin chào, {ten}! Rất vui được gặp bạn.")
    
    # Sử dụng hàm
    print(f"Bình phương của 7 là: {binh_phuong(7)}")
    chao_ten("Lan")

    # --- 5. Bài tập nhỏ ---
    print("\n=== Bài tập nhỏ ===")
    print("Bài tập: Viết chương trình kiểm tra một số có phải là số nguyên tố không.")
    
    def kiem_tra_nguyen_to(n):
        """Kiểm tra xem n có phải là số nguyên tố không"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Kiểm thử với một vài số
    so_kiem_tra = [2, 4, 17, 25]
    for so in so_kiem_tra:
        if kiem_tra_nguyen_to(so):
            print(f"{so} là số nguyên tố")
        else:
            print(f"{so} không phải là số nguyên tố")

    # --- Kết thúc bài học ---
    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản đầu tiên về Python!")
    print("Hãy luyện tập thêm để nắm vững kiến thức nhé!")

# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

### 📌 **Giải thích ngắn:**

- **Các ví dụ**:  
  1. Sử dụng biến kiểu `int`, `float`, `str`, `bool`.  
  2. Dùng `if-elif-else` để xếp loại học lực.  
  3. Dùng `for` và `while` để lặp.

- **Bài tập nhỏ**:  
  Viết hàm kiểm tra số nguyên tố – một bài toán cơ bản giúp luyện `vòng lặp` và `điều kiện`.

---

### 💡 Cách chạy:
1. Lưu nội dung trên vào file `python_basic_lesson.py`
2. Mở terminal và chạy:  
   ```bash
   python python_basic_lesson.py
   ```

> ✅ Phù hợp cho người mới bắt đầu học Python theo lộ trình 21 cấp độ cơ bản!