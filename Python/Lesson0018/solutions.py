# solutions.py
# Lời giải bài tập Bài học 18

# Bài 1: Viết hàm chia_hai_so(a, b) trả về a/b
# Xử lý lỗi chia cho 0 và nhập sai kiểu dữ liệu

def chia_hai_so(a, b):
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except TypeError:
        print("Lỗi: Dữ liệu nhập vào phải là số!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None


# Bài 2: Viết chương trình đọc file diem.txt và in nội dung
# Xử lý lỗi nếu file không tồn tại

def doc_file_diem():
    try:
        with open("diem.txt", "r", encoding="utf-8") as f:
            print("Nội dung file diem.txt:")
            for dong in f:
                print(dong.strip())
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file diem.txt!")
    except PermissionError:
        print("Lỗi: Không có quyền đọc file!")
    except Exception as e:
        print(f"Lỗi khác xảy ra: {e}")


# Bài 3: Viết hàm tim_phan_tu(danh_sach, chi_so)
# Trả về phần tử tại chỉ số, xử lý lỗi nếu chỉ số vượt quá

def tim_phan_tu(danh_sach, chi_so):
    try:
        return danh_sach[chi_so]
    except IndexError:
        print(f"Lỗi: Chỉ số {chi_so} vượt quá độ dài danh sách!")
        return None
    except TypeError:
        print("Lỗi: Chỉ số phải là số nguyên!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None


# Bài 4: Viết chương trình nhập tên và tuổi
# Xử lý để tuổi là số nguyên dương

def nhap_thong_tin():
    ten = input("Nhập tên bạn: ")
    
    while True:
        try:
            tuoi = int(input("Nhập tuổi bạn: "))
            if tuoi <= 0:
                print("Tuổi phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break  # Thoát vòng lặp nếu hợp lệ
        except ValueError:
            print("Lỗi: Tuổi phải là một số nguyên. Vui lòng nhập lại.")
    
    print(f"Xin chào {ten}, bạn {tuoi} tuổi.")


# Bài 5: Viết hàm tinh_can_bac_hai(x)
# Tính căn bậc hai, nhưng chỉ khi x >= 0
# Nếu x < 0, phát sinh lỗi ValueError

def tinh_can_bac_hai(x):
    try:
        if x < 0:
            # Phát sinh lỗi nếu x âm
            raise ValueError("Không thể tính căn bậc hai của số âm!")
        return x ** 0.5
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None