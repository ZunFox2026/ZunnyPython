# Làm quen với đa luồng
## Giới thiệu
Đa luồng (multithreading) là một kỹ thuật lập trình cho phép một chương trình thực hiện nhiều tác vụ đồng thời, cải thiện hiệu suất và tăng tốc độ xử lý. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`. Bài này sẽ giới thiệu về cơ bản của đa luồng trong C++ và cách sử dụng nó.

## Lý thuyết
Một chương trình C++ thông thường chỉ có một luồng chính (main thread), thực hiện tuần tự các câu lệnh. Tuy nhiên, với đa luồng, chúng ta có thể tạo ra nhiều luồng khác nhau, mỗi luồng thực hiện một nhiệm vụ riêng biệt. Mỗi luồng có bộ nhớ riêng và có thể chạy độc lập với các luồng khác.

Để tạo một luồng mới trong C++, chúng ta sử dụng hàm `std::thread`. Hàm này nhận vào một hàm hoặc một đối tượng callable (có thể gọi như một hàm) và tạo một luồng mới để thực hiện hàm đó. Ví dụ:
```cpp
#include <thread>
#include <iostream>

void inRaManHinh() {
    std::cout << "Xin chào từ luồng mới!" << std::endl;
}

int main() {
    std::thread luongMoi(inRaManHinh);
    luongMoi.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một luồng mới `luongMoi` và yêu cầu nó thực hiện hàm `inRaManHinh`. Hàm `join` được sử dụng để chờ đợi cho đến khi luồng mới kết thúc.

## Ví dụ
Một ví dụ khác về đa luồng trong C++ là tạo hai luồng, một luồng in ra màn hình các số chẵn từ 0 đến 10, và luồng kia in ra màn hình các số lẻ từ 1 đến 11.
```cpp
#include <thread>
#include <iostream>

void inSoChan() {
    for (int i = 0; i <= 10; i += 2) {
        std::cout << i << std::endl;
    }
}

void inSoLe() {
    for (int i = 1; i <= 11; i += 2) {
        std::cout << i << std::endl;
    }
}

int main() {
    std::thread luongChan(inSoChan);
    std::thread luongLe(inSoLe);
    luongChan.join();
    luongLe.join();
    return 0;
}
```
Chương trình trên sẽ tạo hai luồng, `luongChan` và `luongLe`, và yêu cầu chúng thực hiện các hàm `inSoChan` và `inSoLe` tương ứng.

## Bài tập
Bài tập cho bạn đọc là tạo một chương trình đa luồng trong C++ để thực hiện các nhiệm vụ sau:
- Tạo hai luồng, một luồng in ra màn hình các số tự nhiên từ 1 đến 10, và luồng kia in ra màn hình các số nguyên âm từ -1 đến -10.
- Sử dụng hàm `join` để chờ đợi cho đến khi cả hai luồng kết thúc.
- Thực hiện các nhiệm vụ trên và quan sát kết quả.