# Làm quen với đa luồng
## Giới thiệu
Trong lập trình, đa luồng (multithreading) là một kỹ thuật cho phép chương trình thực hiện nhiều nhiệm vụ đồng thời. Điều này giúp tăng hiệu suất và khả năng đáp ứng của chương trình. Trong bài viết này, chúng ta sẽ tìm hiểu về đa luồng và cách thực hiện nó trong ngôn ngữ C++.

## Lý thuyết
Đa luồng là một kỹ thuật cho phép chương trình tạo ra nhiều luồng thực hiện (thread) để thực hiện các nhiệm vụ khác nhau. Mỗi luồng thực hiện là một đơn vị thực hiện độc lập, có thể chạy đồng thời với các luồng thực hiện khác. Điều này giúp chương trình có thể thực hiện nhiều nhiệm vụ đồng thời, tăng hiệu suất và khả năng đáp ứng.

Trong C++, chúng ta có thể tạo ra các luồng thực hiện bằng cách sử dụng lớp `std::thread`. Lớp này cung cấp các phương thức để tạo ra, quản lý và điều khiển các luồng thực hiện.

Ví dụ, chúng ta có thể tạo ra một luồng thực hiện mới bằng cách sử dụng phương thức `std::thread` như sau:
```cpp
#include <thread>
#include <iostream>

void ham_thread() {
    std::cout << "Luồng thực hiện mới" << std::endl;
}

int main() {
    std::thread t(ham_thread);
    t.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra một luồng thực hiện mới bằng cách sử dụng phương thức `std::thread` và truyền vào hàm `ham_thread` để thực hiện. Sau đó, chúng ta sử dụng phương thức `join` để chờ đợi luồng thực hiện mới kết thúc trước khi kết thúc chương trình.

## Ví dụ
Chúng ta có thể sử dụng đa luồng để thực hiện các nhiệm vụ đồng thời. Ví dụ, chúng ta có thể tạo ra một chương trình có thể thực hiện cả việc đọc và ghi file đồng thời.

```cpp
#include <thread>
#include <iostream>
#include <fstream>

void doc_file() {
    std::ifstream file("input.txt");
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }
    file.close();
}

void ghi_file() {
    std::ofstream file("output.txt");
    file << "Nội dung mới" << std::endl;
    file.close();
}

int main() {
    std::thread t1(doc_file);
    std::thread t2(ghi_file);
    t1.join();
    t2.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo ra hai luồng thực hiện mới để đọc và ghi file đồng thời. Điều này giúp chương trình có thể thực hiện cả hai nhiệm vụ đồng thời, tăng hiệu suất và khả năng đáp ứng.

## Bài tập
Bài tập 1: Tạo ra một chương trình có thể thực hiện cả việc tính tổng và tính tích của một mảng số nguyên đồng thời.

Bài tập 2: Tạo ra một chương trình có thể thực hiện cả việc đọc và ghi file đồng thời, trong đó file được đọc từ một nguồn và file được ghi vào một đích khác.

Bài tập 3: Tạo ra một chương trình có thể thực hiện cả việc tìm kiếm và sắp xếp một mảng số nguyên đồng thời.

Hy vọng rằng qua bài viết này, bạn đã có một cái nhìn tổng quan về đa luồng và cách thực hiện nó trong ngôn ngữ C++. Chúc bạn thành công trong các bài tập và dự án tiếp theo!