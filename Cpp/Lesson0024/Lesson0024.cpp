#include <iostream>
#include <stdexcept>

// Hàm này sẽ ném ra một ngoại lệ khi tham số truyền vào nhỏ hơn 0
double chia(double a, double b) {
    if (b < 0) {
        throw std::invalid_argument("Tham số thứ hai phải lớn hơn 0");
    }
    if (b == 0) {
        throw std::runtime_error("Không thể chia cho 0");
    }
    return a / b;
}

int main() {
    try {
        // Thực hiện hành động có thể ném ra ngoại lệ
        double ketQua = chia(10, 0);
        std::cout << "Kết quả: " << ketQua << std::endl;
    } catch (const std::invalid_argument& e) {
        // Xử lý ngoại lệ khi tham số không hợp lệ
        std::cerr << "Lỗi: " << e.what() << std::endl;
    } catch (const std::runtime_error& e) {
        // Xử lý ngoại lệ khi chia cho 0
        std::cerr << "Lỗi: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        // Xử lý ngoại lệ chung
        std::cerr << "Lỗi: " << e.what() << std::endl;
    }

    return 0;
}