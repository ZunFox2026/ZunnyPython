import json
import os

# Bài tập 1: Tạo file JSON chứa thông tin sách
def tao_file_sach():
    # Dữ liệu sách mẫu
    danh_sach_sach = [
        {"tua_sach": "Lập trình Python", "tac_gia": "Nguyen Van A", "nam_xb": 2020},
        {"tua_sach": "Cấu trúc dữ liệu", "tac_gia": "Tran Thi B", "nam_xb": 2019},
        {"tua_sach": "AI cho người mới", "tac_gia": "Le Van C", "nam_xb": 2021}
    ]
    
    # Ghi vào file sach.json
    with open("sach.json", "w", encoding="utf-8") as f:
        json.dump(danh_sach_sach, f, ensure_ascii=False, indent=4)
    
    print("Đã tạo file sach.json thành công.")

# Bài tập 2: Tìm kiếm sách theo tên tác giả
def tim_sach_theo_tac_gia(ten_tac_gia):
    # Kiểm tra file có tồn tại không
    if not os.path.exists("sach.json"):
        print("File sach.json không tồn tại.")
        return []
    
    # Đọc dữ liệu từ file
    with open("sach.json", "r", encoding="utf-8") as f:
        danh_sach = json.load(f)
    
    # Tìm các sách có tác giả khớp (không phân biệt hoa thường)
    ket_qua = []
    for sach in danh_sach:
        if sach["tac_gia"].lower() == ten_tac_gia.lower():
            ket_qua.append(sach)
    
    return ket_qua

# Bài tập 3: Cập nhật năm xuất bản của sách
def cap_nhat_nam_xb(ten_sach, nam_moi):
    if not os.path.exists("sach.json"):
        print("File sach.json không tồn tại.")
        return False
    
    with open("sach.json", "r", encoding="utf-8") as f:
        danh_sach = json.load(f)
    
    cap_nhat = False
    for sach in danh_sach:
        if sach["tua_sach"].lower() == ten_sach.lower():
            sach["nam_xb"] = nam_moi
            cap_nhat = True
            break  # Giả sử tên sách là duy nhất
    
    if cap_nhat:
        with open("sach.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=4)
    
    return cap_nhat

# Bài tập 4: In danh sách sách theo định dạng đẹp
def in_danh_sach_sach():
    if not os.path.exists("sach.json"):
        print("Không tìm thấy file sach.json")
        return
    
    with open("sach.json", "r", encoding="utf-8") as f:
        danh_sach = json.load(f)
    
    print("Danh sách sách:")
    for sach in danh_sach:
        print(f"[{sach['tua_sach']}] - {sach['tac_gia']} ({sach['nam_xb']})")

# Bài tập 5: Xử lý lỗi khi file không tồn tại
def doc_file_an_toan(ten_file):
    # Cách 1: Dùng os.path.exists
    if not os.path.exists(ten_file):
        print(f"Cảnh báo: File '{ten_file}' không tồn tại. Trả về danh sách rỗng.")
        return []
    
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Lỗi: File '{ten_file}' chứa dữ liệu JSON không hợp lệ.")
        return []
    except Exception as e:
        print(f"Lỗi không xác định khi đọc file: {e}")
        return []

# Gọi thử các hàm để kiểm tra (có thể bỏ comment khi chạy)
# tao_file_sach()
# print(tim_sach_theo_tac_gia("Nguyen Van A"))
# cap_nhat_nam_xb("Lập trình Python", 2022)
# in_danh_sach_sach()
# print(doc_file_an_toan("sach.json"))