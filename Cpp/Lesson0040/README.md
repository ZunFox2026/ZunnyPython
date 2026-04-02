# Làm quen với đa luồng
## Giới thiệu
Làm quen với đa luồng là một chủ đề quan trọng trong lập trình, đặc biệt là khi bạn muốn tối ưu hóa hiệu suất của chương trình. Đa luồng (multithreading) cho phép chương trình thực hiện nhiều nhiệm vụ đồng thời, giúp giảm thời gian chờ đợi và tăng tốc độ xử lý. Trong bài này, chúng ta sẽ tìm hiểu về đa luồng, cách nó hoạt động và cách áp dụng nó trong lập trình C++.

## Lý thuyết
Trong lập trình, đa luồng là kỹ thuật cho phép chương trình tạo ra nhiều luồng (thread) thực hiện song song các nhiệm vụ khác nhau. Mỗi luồng là một đơn vị thực hiện độc lập, có thể chạy đồng thời với các luồng khác. Điều này giúp chương trình có thể thực hiện nhiều nhiệm vụ cùng lúc, giảm thời gian chờ đợi và tăng tốc độ xử lý. Trong C++, chúng ta có thể tạo ra các luồng bằng cách sử dụng thư viện `<thread>` và lớp `std::thread`.

Ví dụ, chúng ta có thể tạo ra một luồng mới bằng cách gọi hàm `std::thread` và truyền vào một hàm mà chúng ta muốn thực hiện:
```cpp
#include <thread>
#include <iostream>

void hello() {
    std::cout << "Xin chào!" << std::endl;
}

int main() {
    std::thread t(hello);
    t.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra một luồng mới bằng cách gọi hàm `std::thread` và truyền vào hàm `hello`. Sau đó, chúng ta gọi hàm `join` để chờ đợi luồng hoàn thành.

## Ví dụ
Dưới đây là một ví dụ minh họa về đa luồng trong C++:
```cpp
#include <thread>
#include <iostream>

void printNumbers() {
    for (int i = 0; i < 10; i++) {
        std::cout << i << std::endl;
    }
}

void printLetters() {
    for (char c = 'a'; c <= 'j'; c++) {
        std::cout << c << std::endl;
    }
}

int main() {
    std::thread t1(printNumbers);
    std::thread t2(printLetters);
    t1.join();
    t2.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra hai luồng mới bằng cách gọi hàm `std::thread` và truyền vào hai hàm `printNumbers` và `printLetters`. Sau đó, chúng ta gọi hàm `join` để chờ đợi cả hai luồng hoàn thành.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một chương trình đa luồng trong C++ để thực hiện các nhiệm vụ sau:
* Tạo ra hai luồng mới để thực hiện hai hàm khác nhau.
* Hàm thứ nhất sẽ in ra các số từ 1 đến 10.
* Hàm thứ hai sẽ in ra các chữ cái từ 'a' đến 'j'.
* Sử dụng hàm `join` để chờ đợi cả hai luồng hoàn thành.
* Chạy chương trình và quan sát kết quả.

Hy vọng qua bài này, bạn đã hiểu được cách làm việc với đa luồng trong C++ và có thể áp dụng nó vào các dự án của mình.