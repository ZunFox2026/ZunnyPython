#include <iostream>
#include <thread>

// Hàm này sẽ chạy trên một luồng riêng
void chay_trong_luong_rieng() {
    // Đây là ví dụ về một hàm chạy trong một luồng riêng
    for (int i = 0; i < 10; i++) {
        std::cout << "Luồng riêng: " << i << std::endl;
    }
}

int main() {
    // Tạo một luồng mới
    std::thread luong_rieng(chay_trong_luong_rieng);

    // Chạy trên luồng chính
    for (int i = 0; i < 10; i++) {
        std::cout << "Luồng chính: " << i << std::endl;
    }

    // Đợi cho luồng riêng kết thúc
    luong_rieng.join();

    return 0;
}