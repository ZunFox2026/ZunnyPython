#include <iostream>

// Hàm main là điểm bắt đầu của chương trình
int main() {
    // In ra màn hình "Xin chào, tôi là C++!"
    std::cout << "Xin chào, tôi là C++!" << std::endl;

    // Khai báo biến tên
    std::string ten;

    // Yêu cầu người dùng nhập tên
    std::cout << "Nhập tên của bạn: ";
    std::cin >> ten;

    // In ra màn hình "Xin chào, " + tên người dùng
    std::cout << "Xin chào, " << ten << "!" << std::endl;

    // Trả về 0 để kết thúc chương trình
    return 0;
}