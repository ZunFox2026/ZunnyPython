# Làm quen với đa luồng trong C++
## Giới thiệu
Đa luồng (multithreading) là một kỹ thuật trong lập trình cho phép một chương trình thực hiện nhiều tác vụ đồng thời. Điều này giúp tăng hiệu suất và tốc độ của chương trình, đặc biệt là khi thực hiện các tác vụ đòi hỏi thời gian xử lý lâu. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`.

## Lý thuyết
Khi sử dụng đa luồng, chương trình của bạn sẽ tạo ra nhiều luồng (thread) khác nhau. Mỗi luồng sẽ chạy độc lập và thực hiện một phần của chương trình. Để sử dụng đa luồng trong C++, bạn cần bao gồm thư viện `<thread>` và tạo ra các đối tượng `std::thread`. Mỗi đối tượng `std::thread` sẽ đại diện cho một luồng độc lập.

Ví dụ về tạo ra một luồng mới:
```cpp
#include <thread>
#include <iostream>

void inThongDiep() {
    std::cout << "Xin chào từ luồng mới!" << std::endl;
}

int main() {
    std::thread luongMoi(inThongDiep);
    luongMoi.join(); // chờ luồng mới kết thúc
    std::cout << "Kết thúc chương trình." << std::endl;
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra một luồng mới bằng cách gọi hàm `inThongDiep()` thông qua đối tượng `std::thread`. Sau đó, chúng ta sử dụng hàm `join()` để chờ luồng mới kết thúc trước khi tiếp tục thực hiện chương trình.

## Ví dụ
Một ví dụ khác về sử dụng đa luồng trong C++ là việc tính tổng của một dãy số lớn. Thay vì tính tổng toàn bộ dãy số trong một luồng duy nhất, chúng ta có thể chia dãy số thành nhiều phần nhỏ và tính tổng từng phần trong các luồng khác nhau.

Ví dụ về tính tổng của một dãy số lớn:
```cpp
#include <thread>
#include <iostream>

const int SO_PHAN = 4;
const int SO_PHAN_TU = 1000000;

int tong[SO_PHAN] = {0};

void tinhTong(int batDau, int ketThuc, int viTri) {
    for (int i = batDau; i < ketThuc; i++) {
        tong[viTri] += i;
    }
}

int main() {
    std::thread luong[SO_PHAN];
    int phan = SO_PHAN_TU / SO_PHAN;

    for (int i = 0; i < SO_PHAN; i++) {
        int batDau = i * phan;
        int ketThuc = (i == SO_PHAN - 1) ? SO_PHAN_TU : (i + 1) * phan;
        luong[i] = std::thread(tinhTong, batDau, ketThuc, i);
    }

    for (int i = 0; i < SO_PHAN; i++) {
        luong[i].join();
    }

    int ketQua = 0;
    for (int i = 0; i < SO_PHAN; i++) {
        ketQua += tong[i];
    }

    std::cout << "Tổng của dãy số là: " << ketQua << std::endl;
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra 4 luồng để tính tổng của 4 phần khác nhau của dãy số. Sau đó, chúng ta chờ tất cả các luồng kết thúc và tính tổng kết quả từ từng luồng.

## Bài tập
Bài tập cho bạn đọc là viết một chương trình sử dụng đa luồng để tính tổng của một dãy số lớn. Dãy số này sẽ được chia thành nhiều phần nhỏ và tính tổng từng phần trong các luồng khác nhau. Sau đó, hãy tính tổng kết quả từ từng luồng và in ra màn hình.

Yêu cầu:

- Dãy số có 10 triệu phần tử.
- Chia dãy số thành 5 phần nhỏ.
- Tính tổng từng phần trong 5 luồng khác nhau.
- Tính tổng kết quả từ từng luồng và in ra màn hình.

Đây là một bài tập cơ bản về đa luồng trong C++, giúp bạn làm quen với kỹ thuật này và tăng tốc độ xử lý của chương trình.