##########################################################
# BÀI TẬP THỰC HÀNH - Bài học 92: Decorator nâng cao
# Không chỉnh sửa file này sau khi nộp bài
# Viết lời giải trong file solutions.py
##########################################################

# Bài 1: Viết decorator @repeat(n)
# Gọi hàm lặp lại n lần và trả về danh sách kết quả
# Ví dụ: @repeat(3) sẽ gọi hàm 3 lần
# def repeat(n):
#     ...

# @repeat(3)
# def hello():
#     print("Xin chào!")
#     return "OK"


# Bài 2: Viết class decorator @TimeIt
# In ra thời gian thực thi mỗi lần gọi hàm
# class TimeIt:
#     ...

# @TimeIt
# def tinh_toan(n):
#     return sum(i * i for i in range(n))


# Bài 3: Viết decorator @only_allow_types
# Kiểm tra kiểu dữ liệu của các đối số
# Nếu sai kiểu → báo lỗi
# @only_allow_types(int, int)
# def cong(a, b):
#     return a + b


# Bài 4: Viết decorator @cache_method
# Cache kết quả của phương thức (theo tham số)
# Áp dụng cho phương thức trong lớp
# class MayTinh:
#     @cache_method
#     def fibonacci(self, n):
#         if n < 2:
#             return n
#         return self.fibonacci(n-1) + self.fibonacci(n-2)


# Bài 5: Viết decorator @ensure_result
# Kiểm tra kết quả trả về có thỏa điều kiện không
# Nếu không → báo lỗi
# @ensure_result(lambda x: x > 0)
# def nghich_dao(a):
#     return 1 / a if a != 0 else 0
