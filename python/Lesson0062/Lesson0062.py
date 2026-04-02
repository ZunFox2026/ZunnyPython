# Bài 62: Lập Trình Cơ Bản về Tính Sóng

# Hàm tính sóng sine
def tinh_sine(t):
    # Sử dụng thư viện math để tính sine
    import math
    # Trả về giá trị sine của t
    return math.sin(t)

# Hàm tính sóng cosine
def tinh_cosine(t):
    # Sử dụng thư viện math để tính cosine
    import math
    # Trả về giá trị cosine của t
    return math.cos(t)

# Hàm vẽ đồ thị sóng
def ve_do_thi_sine():
    # Sử dụng thư viện matplotlib để vẽ đồ thị
    import matplotlib.pyplot as plt
    import numpy as np

    # Tạo mảng giá trị t từ 0 đến 4π
    t = np.linspace(0, 4 * np.pi, 1000)

    # Tính giá trị sine của t
    sine = [tinh_sine(i) for i in t]

    # Vẽ đồ thị sóng sine
    plt.plot(t, sine)
    plt.title('Đồ thị sóng sine')
    plt.xlabel('t')
    plt.ylabel('Sine(t)')
    plt.grid(True)
    plt.show()

# Hàm vẽ đồ thị sóng cosine
def ve_do_thi_cosine():
    # Sử dụng thư viện matplotlib để vẽ đồ thị
    import matplotlib.pyplot as plt
    import numpy as np

    # Tạo mảng giá trị t từ 0 đến 4π
    t = np.linspace(0, 4 * np.pi, 1000)

    # Tính giá trị cosine của t
    cosine = [tinh_cosine(i) for i in t]

    # Vẽ đồ thị sóng cosine
    plt.plot(t, cosine)
    plt.title('Đồ thị sóng cosine')
    plt.xlabel('t')
    plt.ylabel('Cosine(t)')
    plt.grid(True)
    plt.show()

# Chạy hàm vẽ đồ thị sóng sine và cosine
ve_do_thi_sine()
ve_do_thi_cosine()