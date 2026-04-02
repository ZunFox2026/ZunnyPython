#include <iostream> // Thư viện input/output
#include <thread>   // Thư viện đa luồng
#include <chrono>  // Thư viện thời gian

// Hàm sẽ được gọi bởi luồng con
void hamCon() {
    // In thông điệp từ luồng con
    std::cout << "Xin chào từ luồng con!" << std::endl;
    
    // Ngủ 1 giây để minh họa luồng chính và con chạy song song
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    // In thông điệp từ luồng con sau khi ngủ
    std::cout << "Luồng con đã ngủ xong!" << std::endl;
}

int main() {
    // In thông điệp từ luồng chính
    std::cout << "Xin chào từ luồng chính!" << std::endl;
    
    // Tạo một luồng con
    std::thread luongCon(hamCon);
    
    // Ngủ 1 giây để minh họa luồng chính và con chạy song song
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    // In thông điệp từ luồng chính sau khi ngủ
    std::cout << "Luồng chính đã ngủ xong!" << std::endl;
    
    // Chờ luồng con kết thúc
    luongCon.join();
    
    // In thông điệp từ luồng chính sau khi luồng con kết thúc
    std::cout << "Luồng chính đã kết thúc!" << std::endl;
    
    return 0;
}