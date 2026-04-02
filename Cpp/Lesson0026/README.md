# Tìm hiểu về đa luồng trong C++
## Giới thiệu
Đa luồng (Multithreading) là một kỹ thuật cho phép một chương trình thực hiện nhiều tác vụ đồng thời. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`. Bài viết này sẽ giới thiệu về đa luồng trong C++ và cách sử dụng nó.

## Lý thuyết
Đa luồng trong C++ cho phép tạo ra nhiều luồng (thread) khác nhau. Mỗi luồng có thể thực hiện một tác vụ riêng biệt. Các luồng này có thể chạy đồng thời, giúp tăng tốc độ thực hiện chương trình. Để sử dụng đa luồng trong C++, chúng ta cần tạo ra các đối tượng `std::thread` và sử dụng hàm `std::thread::join()` để chờ đợi các luồng hoàn thành.

Ví dụ, chúng ta có thể tạo ra hai luồng, một luồng thực hiện công việc A và một luồng thực hiện công việc B. Khi đó, chương trình sẽ thực hiện cả công việc A và B đồng thời.

```cpp
#include <thread>
#include <iostream>

void congViecA() {
    std::cout << "Cong viec A" << std::endl;
}

void congViecB() {
    std::cout << "Cong viec B" << std::endl;
}

int main() {
    std::thread t1(congViecA);
    std::thread t2(congViecB);

    t1.join();
    t2.join();

    return 0;
}
```

## Ví dụ
Một ví dụ khác về đa luồng trong C++ là việc sử dụng đa luồng để thực hiện các công việc nặng. Ví dụ, chúng ta có thể tạo ra một luồng để tính tổng các số từ 1 đến 1000000 và một luồng để tính tổng các số từ 1000001 đến 2000000. Khi đó, chương trình sẽ thực hiện cả hai công việc đồng thời.

```cpp
#include <thread>
#include <iostream>

void tinhTong(int batDau, int ketThuc) {
    int tong = 0;
    for (int i = batDau; i <= ketThuc; i++) {
        tong += i;
    }
    std::cout << "Tong tu " << batDau << " den " << ketThuc << ": " << tong << std::endl;
}

int main() {
    std::thread t1(tinhTong, 1, 1000000);
    std::thread t2(tinhTong, 1000001, 2000000);

    t1.join();
    t2.join();

    return 0;
}
```

## Bài tập
Bài tập về đa luồng trong C++:

- Tạo một chương trình đa luồng để tính tổng các số từ 1 đến 1000000 và tổng các số từ 1000001 đến 2000000 đồng thời.
- Tạo một chương trình đa luồng để thực hiện các công việc sau đồng thời:
  - Công việc A: In ra màn hình các số từ 1 đến 10.
  - Công việc B: In ra màn hình các số từ 11 đến 20.
  - Công việc C: In ra màn hình các số từ 21 đến 30.

Bài tập này sẽ giúp bạn hiểu rõ hơn về đa luồng trong C++ và cách sử dụng nó để tăng tốc độ thực hiện chương trình.