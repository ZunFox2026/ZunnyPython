# Bài 26: Python Cơ bản
# Chủ đề: Tổng hợp kiến thức nền tảng (Biến, Danh sách, Hàm, Vòng lặp, Câu điều kiện, Xử lý chuỗi & Nhập/Xuất)

def tinh_tong(danh_sach_so):
    """Tính tổng các phần tử trong danh sách số."""
    tong = 0
    for so in danh_sach_so:
        tong += so
    return tong

def loc_so_chan(danh_sach_so):
    """Lọc và trả về danh sách các số chẵn."""
    return [so for so in danh_sach_so if so % 2 == 0]

def kiem_tra_doi_xung(chuoi):
    """Kiểm tra chuỗi có phải là đối xứng (palindrome) hay không."""
    chuan_hoa = chuoi.replace(" ", "").lower()
    return chuan_hoa == chuan_hoa[::-1]

def hien_thi_thong_tin(ten, tuoi, danh_sach_diem):
    """Hiển thị thông tin và xếp loại học lực dựa trên điểm trung bình."""
    diem_trung_binh = sum(danh_sach_diem) / len(danh_sach_diem)
    
    print(f"\n👤 Tên: {ten} | 🎂 Tuổi: {tuoi}")
    print(f"📊 Điểm trung bình: {diem_trung_binh:.2f}")
    
    if diem_trung_binh >= 8.5:
        xep_loai = "Giỏi 🌟"
    elif diem_trung_binh >= 7.0:
        xep_loai = "Khá 👍"
    elif diem_trung_binh >= 5.0:
        xep_loai = "Trung bình 📝"
    else:
        xep_loai = "Yếu ⚠️"
        
    print(f"🎓 Xếp loại: {xep_loai}")

def main():
    """Hàm chính: Điều phối các ví dụ minh họa kiến thức cơ bản."""
    print("="*45)
    print("📘 BÀI 26: THỰC HÀNH PYTHON CƠ BẢN")
    print("="*45)

    # 1. Làm việc với danh sách và số học cơ bản
    ds_so = [10, 7, 4, 19, 8, 3, 15, 12]
    print(f"\n📥 Danh sách ban đầu: {ds_so}")
    print(f"➕ Tổng các số: {tinh_tong(ds_so)}")
    print(f"🔢 Các số chẵn: {loc_so_chan(ds_so)}")

    # 2. Xử lý chuỗi cơ bản
    print("\n🔤 KIỂM TRA CHUỖI ĐỐI XỨNG")
    tu_1 = "radar"
    tu_2 = "Python"
    print(f"'{tu_1}' -> {'Đối xứng ✅' if kiem_tra_doi_xung(tu_1) else 'Không đối xứng ❌'}")
    print(f"'{tu_2}' -> {'Đối xứng ✅' if kiem_tra_doi_xung(tu_2) else 'Không đối xứng ❌'}")

    # 3. Tương tác người dùng & Cấu trúc điều khiển
    print("\n📝 NHẬP THÔNG TIN & XẾP LOẠI")
    try:
        ten = input("Nhập tên học viên: ").strip()
        if not ten:
            raise ValueError("Tên không được để trống.")
            
        tuoi = int(input("Nhập tuổi: "))
        if tuoi < 1:
            raise ValueError("Tuổi phải là số nguyên dương.")
            
        diem_str = input("Nhập các điểm cách nhau bởi dấu cách: ")
        ds_diem = [float(d) for d in diem_str.split()]
        
        if not ds_diem:
            raise ValueError("Danh sách điểm không được để trống.")
        if any(d < 0 or d > 10 for d in ds_diem):
            print("⚠️  Cảnh báo: Có điểm nằm ngoài khoảng 0-10.")
            
        hien_thi_thong_tin(ten, tuoi, ds_diem)
        
    except ValueError as e:
        print(f"❌ Lỗi định dạng dữ liệu: {e}")
    except Exception as e: