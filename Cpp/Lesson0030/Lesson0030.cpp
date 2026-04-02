#include <iostream>
#include <thread>
#include <chrono>

// Hàm này sẽ được chạy trong một luồng khác
void hamKhac() {
    // In ra thông báo từ luồng khác
    std::cout << "Xin chào từ luồng khác!" << std::endl;
    
    // Ngủ 2 giây để minh họa luồng đang chạy
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    // In ra thông báo khác từ luồng khác
    std::cout << "Luồng khác đã chạy xong!" << std::endl;
}

int main() {
    // Tạo một luồng mới và chạy hàm hamKhac trong luồng đó
    std::thread luongKhac(hamKhac);
    
    // In ra thông báo từ luồng chính
    std::cout << "Xin chào từ luồng chính!" << std::endl;
    
    // Ngủ 1 giây để minh họa luồng chính đang chạy
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    // In ra thông báo khác từ luồng chính
    std::cout << "Luồng chính đang chạy..." << std::endl;
    
    // Đợi luồng khác chạy xong trước khi kết thúc chương trình
    luongKhac.join();
    
    // In ra thông báo cuối cùng từ luồng chính
    std::cout << "Chương trình đã chạy xong!" << std::endl;
    
    return 0;
}