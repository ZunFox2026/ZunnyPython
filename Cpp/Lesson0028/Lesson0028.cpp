#include <iostream>
#include <thread>

// Hàm này sẽ được thực hiện bởi một luồng khác
void hamLuongKhac() {
    // In ra thông điệp từ luồng khác
    std::cout << "Xin chào từ luồng khác!" << std::endl;
}

int main() {
    // Tạo một luồng mới và gán hàm hamLuongKhac() cho nó
    std::thread luongKhac(hamLuongKhac);

    // In ra thông điệp từ luồng chính
    std::cout << "Xin chào từ luồng chính!" << std::endl;

    // Đợi cho luồng khác kết thúc trước khi tiếp tục
    luongKhac.join();

    return 0;
}