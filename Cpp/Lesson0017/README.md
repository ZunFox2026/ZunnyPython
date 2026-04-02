# Tìm hiểu về đa luồng trong C++
## Giới thiệu
Trong lập trình, đa luồng (multithreading) là một kỹ thuật cho phép chương trình thực hiện nhiều nhiệm vụ cùng một lúc. Điều này giúp cải thiện hiệu suất và tốc độ xử lý của chương trình. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`. Bài viết này sẽ giới thiệu về đa luồng trong C++ và cách sử dụng nó.

## Lý thuyết
Đa luồng trong C++ cho phép tạo ra nhiều luồng (thread) độc lập, mỗi luồng thực hiện một nhiệm vụ riêng. Mỗi luồng có bộ nhớ và tài nguyên riêng, và có thể giao tiếp với các luồng khác thông qua các phương tiện như biến chung, hàng đợi,... Khi sử dụng đa luồng, cần lưu ý về vấn đề đồng bộ hóa (synchronization) để tránh xung đột giữa các luồng.

Ví dụ, chúng ta có thể tạo một luồng mới bằng cách sử dụng constructor của lớp `std::thread`:
```cpp
#include <thread>
#include <iostream>

void hamThread() {
    std::cout << "Xin chào từ luồng mới!" << std::endl;
}

int main() {
    std::thread t(hamThread);
    t.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một luồng mới bằng cách gọi constructor của lớp `std::thread` và truyền vào hàm `hamThread` sẽ được thực hiện trong luồng mới.

## Ví dụ
Một ví dụ khác về đa luồng trong C++ là việc sử dụng đa luồng để thực hiện nhiều nhiệm vụ cùng một lúc. Ví dụ, chúng ta có thể tạo hai luồng, một luồng để tính tổng các số từ 1 đến 100, và một luồng để tính tích các số từ 1 đến 100:
```cpp
#include <thread>
#include <iostream>

void tinhTong(int n) {
    int tong = 0;
    for (int i = 1; i <= n; i++) {
        tong += i;
    }
    std::cout << "Tổng các số từ 1 đến " << n << " là: " << tong << std::endl;
}

void tinhTich(int n) {
    int tich = 1;
    for (int i = 1; i <= n; i++) {
        tich *= i;
    }
    std::cout << "Tích các số từ 1 đến " << n << " là: " << tich << std::endl;
}

int main() {
    std::thread t1(tinhTong, 100);
    std::thread t2(tinhTich, 100);
    t1.join();
    t2.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo hai luồng `t1` và `t2`, một luồng để tính tổng các số từ 1 đến 100, và một luồng để tính tích các số từ 1 đến 100. Hai luồng này được thực hiện cùng một lúc, giúp cải thiện hiệu suất của chương trình.

## Bài tập
Bài tập cho bạn đọc là viết một chương trình C++ sử dụng đa luồng để thực hiện các nhiệm vụ sau:
- Tạo hai luồng, một luồng để in ra các số từ 1 đến 100, và một luồng để in ra các chữ cái từ A đến Z.
- Sử dụng đa luồng để tính tổng và tích các số từ 1 đến 100.