"""
Bài học: Python 49 - Xử Lý Chuỗi và Hàm Cơ Bản
Mục tiêu:
- Hiểu cách xử lý chuỗi trong Python.
- Sử dụng các hàm cơ bản để thao tác với chuỗi.
- Áp dụng vào các ví dụ và bài tập thực tế.
"""

def main():
    # === 1. Giới thiệu về chuỗi trong Python ===
    # Chuỗi là dãy ký tự, được bao quanh bởi nháy đơn hoặc nháy kép
    chuoi_1 = "Xin chào Python!"
    chuoi_2 = 'Học lập trình vui vẻ'

    print("Chuỗi 1:", chuoi_1)
    print("Chuỗi 2:", chuoi_2)

    # === 2. Truy cập ký tự trong chuỗi ===
    # Chuỗi là dãy có thứ tự, có thể truy cập bằng chỉ số (index)
    print("\n=== Truy cập ký tự ===")
    print("Ký tự đầu tiên của chuỗi 1:", chuoi_1[0])  # X
    print("Ký tự cuối cùng của chuỗi 1:", chuoi_1[-1])  # !

    # === 3. Cắt chuỗi (Slicing) ===
    print("\n=== Cắt chuỗi ===")
    print("Cắt từ vị trí 4 đến 9:", chuoi_1[4:10])  # "chào"
    print("Cắt từ đầu đến vị trí 7:", chuoi_1[:7])   # "Xin ch"
    print("Cắt từ vị trí 4 đến cuối:", chuoi_1[4:])   # "chào Python!"

    # === 4. Một số phương thức xử lý chuỗi phổ biến ===
    print("\n=== Xử lý chuỗi với các phương thức ===")

    # Đổi chữ hoa/thường
    print("Viết hoa toàn bộ:", chuoi_1.upper())        # XIN CHÀO PYTHON!
    print("Viết thường toàn bộ:", chuoi_1.lower())     # xin chào python!

    # Loại bỏ khoảng trắng đầu/cuối
    chuoi_co_khoang_trang = "   Dữ liệu thô   "
    print("Chuỗi gốc:", repr(chuoi_co_khoang_trang))
    print("Sau khi strip():", repr(chuoi_co_khoang_trang.strip()))

    # Thay thế chuỗi
    chuoi_thay_the = chuoi_1.replace("Python", "Lập Trình")
    print("Sau khi thay thế:", chuoi_thay_the)

    # Tách chuỗi thành danh sách
    chuoi_tach = "apple,banana,orange"
    danh_sach = chuoi_tach.split(",")
    print("Tách chuỗi theo dấu phẩy:", danh_sach)

    # Nối chuỗi
    chuoi_moi = " và ".join(danh_sach)
    print("Nối lại bằng ' và ':", chuoi_moi)

    # Kiểm tra chuỗi bắt đầu/kết thúc bằng gì
    print("Có bắt đầu bằng 'Xin' không?", chuoi_1.startswith("Xin"))  # True
    print("Có kết thúc bằng '!' không?", chuoi_1.endswith("!"))       # True

    # === 5. Hàm cơ bản xử lý chuỗi ===
    def dem_tu(chuoi, tu):
        """Hàm đếm số lần xuất hiện của một từ trong chuỗi"""
        return chuoi.lower().count(tu.lower())

    def dao_nguoc_chuoi(chuoi):
        """Hàm đảo ngược chuỗi"""
        return chuoi[::-1]

    def kiem_tra_palindrome(chuoi):
        """Kiểm tra chuỗi đối xứng (palindrome)"""
        chuoi_sach = chuoi.lower().replace(" ", "")
        return chuoi_sach == dao_nguoc_chuoi(chuoi_sach)

    # === 6. Ví dụ minh họa ===
    print("\n=== Ví dụ minh họa ===")

    # Ví dụ 1: Đếm từ
    van_ban = "Python là ngôn ngữ lập trình Python mạnh mẽ và Python rất dễ học"
    so_lan_xuat_hien = dem_tu(van_ban, "python")
    print(f"Từ 'python' xuất hiện {so_lan_xuat_hien} lần")

    # Ví dụ 2: Đảo ngược chuỗi
    print("Đảo ngược 'hello':", dao_nguoc_chuoi("hello"))

    # Ví dụ 3: Kiểm tra palindrome
    chuoi_palindrome = "A man a plan a canal Panama"
    print(f"'{chuoi_palindrome}' có phải palindrome? {kiem_tra_palindrome(chuoi_palindrome)}")

    # === 7. Bài tập nhỏ ===
    print("\n=== Bài tập nhỏ ===")
    print("Bài tập: Viết hàm chuẩn hóa tên người (viết hoa chữ cái đầu mỗi từ)")
    
    def chuan_hoa_ten(ho_ten):
        """Chuẩn hóa tên người: mỗi từ viết hoa chữ cái đầu"""
        # Tách từ, loại khoảng trắng thừa, viết hoa chữ đầu mỗi từ
        cac_tu = ho_ten.strip().split()
        ten_chuan = " ".join([tu.capitalize() for tu in cac_tu])
        return ten_chuan

    # Kiểm thử hàm chuẩn hóa
    ten_thu = "  nguyễn  văn  minh  "
    print(f"Tên gốc: '{ten_thu}'")
    print(f"Tên chuẩn hóa: '{chuan_hoa_ten(ten_thu)}'")

    # Gợi ý mở rộng: kiểm tra email đơn giản
    def kiem_tra_email(email):
        """Kiểm tra email có hợp lệ không (rất đơn giản)"""
        return "@" in email and "." in email and email.count("@") == 1

    email = "user@example.com"
    print(f"Email '{email}' có hợp lệ? {kiem_tra_email(email)}")

    print("\nChương trình kết thúc. Cảm ơn bạn đã học về xử lý chuỗi!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**
- Bài học giới thiệu các thao tác chuỗi cơ bản: truy cập, cắt, thay thế, tách, nối.
- Các hàm được định nghĩa để minh họa: đếm từ, đảo chuỗi, kiểm tra palindrome.
- Bài tập nhỏ: chuẩn hóa tên người và kiểm tra email đơn giản.
- Dễ hiểu, dễ mở rộng, phù hợp với người mới học.