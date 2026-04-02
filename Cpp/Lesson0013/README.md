# Làm quen với Xử lý tệp
## Giới thiệu
Xử lý tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và truy xuất dữ liệu từ các tệp trên đĩa cứng. Trong C++, chúng ta có thể sử dụng các lớp như `ifstream` và `ofstream` để thực hiện các thao tác này. Bài viết này sẽ giới thiệu về cách làm quen với xử lý tệp trong C++.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng các lớp sau để xử lý tệp:
- `ifstream`: Sử dụng để đọc dữ liệu từ tệp.
- `ofstream`: Sử dụng để ghi dữ liệu vào tệp.
- `fstream`: Sử dụng để đọc và ghi dữ liệu vào tệp.

Để sử dụng các lớp này, chúng ta cần bao gồm thư viện `fstream` trong chương trình. Ví dụ:
```cpp
#include <fstream>
```
Sau đó, chúng ta có thể tạo một đối tượng của lớp tương ứng và sử dụng các phương thức như `open()`, `close()`, `read()`, `write()` để thực hiện các thao tác trên tệp.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng `ofstream` để ghi dữ liệu vào tệp:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
        std::cout << "Dữ liệu đã được ghi vào tệp.\n";
    } else {
        std::cout << "Không thể mở tệp.\n";
    }
    return 0;
}
```
Và đây là một ví dụ về cách sử dụng `ifstream` để đọc dữ liệu từ tệp:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << "\n";
        }
        file.close();
    } else {
        std::cout << "Không thể mở tệp.\n";
    }
    return 0;
}
```
## Bài tập
Bài tập này yêu cầu bạn thực hiện các thao tác sau:
1. Tạo một tệp văn bản có tên là `student.txt` với nội dung sau:
   - Mã sinh viên
   - Tên sinh viên
   - Điểm trung bình
2. Viết chương trình C++ để đọc dữ liệu từ tệp `student.txt` và hiển thị thông tin lên màn hình.
3. Viết chương trình C++ để ghi dữ liệu vào tệp `student.txt` và hiển thị thông báo thành công khi ghi xong.

Đây là một số gợi ý để bạn bắt đầu:
- Sử dụng `std::ofstream` để ghi dữ liệu vào tệp.
- Sử dụng `std::ifstream` để đọc dữ liệu từ tệp.
- Sử dụng `std::getline` để đọc từng dòng dữ liệu từ tệp.
- Sử dụng `std::cout` để hiển thị thông tin lên màn hình.