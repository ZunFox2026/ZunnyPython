# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ tệp. Trong C++, chúng ta có thể thực hiện các hoạt động này bằng cách sử dụng các hàm và đối tượng được cung cấp bởi thư viện chuẩn.

## Lý thuyết
Để làm việc với tệp trong C++, chúng ta cần bao gồm thư viện `fstream`. Thư viện này cung cấp hai lớp chính: `ifstream` (để đọc tệp) và `ofstream` (để ghi tệp). Ngoài ra, chúng ta cũng có thể sử dụng lớp `fstream` để thực hiện cả hai hoạt động đọc và ghi.

Khi làm việc với tệp, chúng ta cần thực hiện các bước sau:
- Mở tệp: Sử dụng hàm `open()` để mở tệp.
- Đọc/ghi tệp: Sử dụng các hàm như `read()`, `write()`, `getline()` để đọc và ghi dữ liệu.
- Đóng tệp: Sử dụng hàm `close()` để đóng tệp.

Ví dụ về mở và đóng tệp:
```cpp
#include <fstream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        // Ghi dữ liệu vào tệp
        file << "Xin chào, thế giới!";
        file.close();
    }
    return 0;
}
```

## Ví dụ
Ví dụ minh họa cách đọc và ghi tệp:

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Ghi dữ liệu vào tệp
    std::ofstream outfile("example.txt");
    if (outfile.is_open()) {
        outfile << "Dòng 1\n";
        outfile << "Dòng 2\n";
        outfile.close();
    }

    // Đọc dữ liệu từ tệp
    std::ifstream infile("example.txt");
    if (infile.is_open()) {
        std::string line;
        while (std::getline(infile, line)) {
            std::cout << line << std::endl;
        }
        infile.close();
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để ghi danh sách các sinh viên vào một tệp. Mỗi sinh viên có thông tin bao gồm tên, tuổi và điểm trung bình. Sử dụng cấu trúc dữ liệu để lưu trữ thông tin sinh viên.

Bài tập 2: Tạo một chương trình C++ để đọc tệp chứa danh sách các sinh viên và hiển thị thông tin của họ. Sử dụng cấu trúc dữ liệu giống như trong bài tập 1.

Bài tập 3: Tạo một chương trình C++ để quản lý danh sách các cuốn sách trong một thư viện. Cho phép người dùng thêm, xóa và tìm kiếm sách. Dữ liệu được lưu trữ trong một tệp.