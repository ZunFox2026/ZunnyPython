import inspect

def ham_bai_tap(x: int, y: str = "test", z: list = None):
    if z is None:
        z = []
    return x > 0 and len(y) in z

class LopBaiTap:
    def __init__(self, gia_tri: int):
        self.gia_tri = gia_tri

    def phuong_thuc_1(self, a: float) -> float:
        return a * self.gia_tri

    def phuong_thuc_2(self, b: str = "ok") -> bool:
        return b == "ok"

# Bài tập 1: Viết hàm in thông tin chi tiết về một hàm
# def in_thong_tin_ham(func):
#     ...

# Bài tập 2: Kiểm tra tính hợp lệ của tham số khi gọi hàm
# def kiem_tra_loi_goi(func, *args, **kwargs):
#     ... 

# Bài tập 3: Viết decorator @theo_doi để ghi log
# @theo_doi
# def ham_thu(x, y=10):
#     return x + y

# Bài tập 4: Tìm và in thông tin về một phương thức trong lớp
# def tim_phuong_thuc_cua_lop(cls, ten_phuong_thuc):
#     ...