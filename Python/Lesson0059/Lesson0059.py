"""
Bài học: Python 59 - Xử Lý Chuỗi Cơ Bản
Mục tiêu: Hiểu và sử dụng các thao tác cơ bản trên chuỗi trong Python.
"""

def main():
    # === 1. Khởi tạo và in chuỗi ===
    chuoi = "Xin chào, đây là bài học xử lý chuỗi cơ bản!"
    print("Chuỗi gốc:", chuoi)

    # === 2. Truy cập ký tự trong chuỗi ===
    # Chuỗi là dãy ký tự, có thể truy cập bằng chỉ số (index)
    print("Ký tự đầu tiên:", chuoi[0])  # 'X'
    print("Ký tự cuối cùng:", chuoi[-1])  # '!'
    print("Ký tự thứ 5:", chuoi[4])  # 'h'

    # === 3. Cắt chuỗi (slicing) ===
    # Cú pháp: chuoi[begin:end:step]
    print("5 ký tự đầu:", chuoi[:5])  # 'Xin c'
    print("Từ vị trí 5 đến 10:", chuoi[5:11])  # 'hào, '
    print("Chuỗi đảo ngược:", chuoi[::-1])  # Đảo ngược toàn bộ chuỗi

    # === 4. Các phương thức xử lý chuỗi phổ biến ===

    # Đổi chữ hoa/thường
    print("Viết hoa toàn bộ:", chuoi.upper())
    print("Viết thường toàn bộ:", chuoi.lower())
    print("Viết hoa chữ cái đầu mỗi từ:", chuoi.title())

    # Loại bỏ khoảng trắng đầu/cuối
    chuoi_co_khoang_trang = "   Chuỗi có khoảng trắng   "
    print("Chuỗi sau khi strip():", chuoi_co_khoang_trang.strip())

    # Thay thế nội dung
    chuoi_moi = chuoi.replace("chào", "đón")
    print("Sau khi thay thế 'chào' thành 'đón':", chuoi_moi)

    # Tìm kiếm vị trí chuỗi con
    vi_tri = chuoi.find("chuỗi")
    if vi_tri != -1:
        print(f"Chuỗi 'chuỗi' xuất hiện tại vị trí: {vi_tri}")
    else:
        print("Không tìm thấy chuỗi con.")

    # Tách chuỗi thành danh sách
    danh_sach_tu = chuoi.split()  # Mặc định tách theo khoảng trắng
    print("Danh sách các từ:", danh_sach_tu)

    # Gộp danh sách thành chuỗi
    chuoi_gop = "-".join(danh_sach_tu)
    print("Chuỗi sau khi join bằng '-':", chuoi_gop)

    # Kiểm tra chuỗi bắt đầu/kết thúc bằng
    print("Có bắt đầu bằng 'Xin' không?", chuoi.startswith("Xin"))
    print("Có kết thúc bằng '!' không?", chuoi.endswith("!"))

    # Kiểm tra loại ký tự
    print("'abc'.isalpha():", "abc".isalpha())  # True - chỉ chứa chữ cái
    print("'123'.isdigit():", "123".isdigit())  # True - chỉ chứa số
    print("'abc123'.isalnum():", "abc123".isalnum())  # True - chữ và số

    # === VÍ DỤ 1: Đếm số từ trong chuỗi ===
    print("\n=== VÍ DỤ 1: Đếm số từ ===")
    van_ban = "Học lập trình Python rất thú vị và bổ ích"
    so_tu = len(van_ban.split())
    print(f"Văn bản: '{van_ban}'")
    print(f"Số từ: {so_tu}")

    # === VÍ DỤ 2: Chuẩn hóa tên người dùng ===
    print("\n=== VÍ DỤ 2: Chuẩn hóa tên người dùng ===")
    ten_nguoi_dung = "  nguyễn  văn  minh  "
    ten_chuan = ten_nguoi_dung.strip().title()  # Xóa khoảng trắng, viết hoa chữ cái đầu mỗi từ
    print(f"Tên gốc: '{ten_nguoi_dung}'")
    print(f"Tên chuẩn hóa: '{ten_chuan}'")

    # === BÀI TẬP NHỎ ===
    print("\n=== BÀI TẬP NHỎ ===")
    print("Bài tập: Nhập một chuỗi, hãy:")
    print("1. Đếm số từ")
    print("2. Viết hoa chữ cái đầu mỗi từ")
    print("3. Kiểm tra xem chuỗi có chứa từ 'Python' không")

    # Nhập từ người dùng
    chuoi_nhap = input("\nNhập một chuỗi: ").strip()

    # Xử lý
    so_tu_baitap = len(chuoi_nhap.split())
    chuoi_viet_hoa = chuoi_nhap.title()
    co_python = "python" in chuoi_nhap.lower()

    # In kết quả
    print(f"1. Số từ: {so_tu_baitap}")
    print(f"2. Chuỗi viết hoa: {chuoi_viet_hoa}")
    print(f"3. Có chứa 'Python'? {'Có' if co_python else 'Không'}")

    # Gợi ý mở rộng: Đảo ngược từng từ trong chuỗi
    print("\nBonus: Đảo ngược từng từ trong chuỗi")
    cac_tu = chuoi_nhap.split()
    tu_dao_nguoc = [tu[::-1] for tu in cac_tu]
    chuoi_dao_tung_tu = " ".join(tu_dao_nguoc)
    print(f"Chuỗi sau khi đảo từng từ: {chuoi_dao_tung_tu}")


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```

---

✅ **Tổng kết bài học**:
- Chuỗi trong Python là bất biến (immutable).
- Có thể truy cập ký tự bằng chỉ số và cắt chuỗi bằng slicing.
- Nhiều phương thức hữu ích: `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, v.v.
- Bài tập giúp luyện tập thao tác thực tế với chuỗi.

📌 **Lưu ý**: Chạy file `.py` này trong môi trường Python để xem kết quả và làm bài tập tương tác.