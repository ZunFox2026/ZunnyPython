# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ tệp tin. Trong C++, bạn có thể sử dụng các hàm và lớp để thực hiện các hoạt động này. Bài viết này sẽ giới thiệu về cách làm việc với tệp tin trong C++.

## Lý thuyết
Để làm việc với tệp tin trong C++, bạn cần sử dụng thư viện `<fstream>`. Thư viện này cung cấp các lớp `ifstream`, `ofstream` và `fstream` để đọc, viết và đọc/ghi tệp tin.

- `ifstream`: Sử dụng để đọc tệp tin.
- `ofstream`: Sử dụng để viết tệp tin.
- `fstream`: Sử dụng để đọc và viết tệp tin.

Các hàm thường dùng:
- `open()`: Mở tệp tin.
- `close()`: Đóng tệp tin.
- `read()`: Đọc dữ liệu từ tệp tin.
- `write()`: Ghi dữ liệu vào tệp tin.

Ví dụ về mở tệp tin:
```cpp
#include <fstream>
using namespace std;

int main() {
    ifstream file("example.txt");
    if (file.is_open()) {
        cout << "Tệp tin đã được mở." << endl;
        file.close();
    } else {
        cout << "Không thể mở tệp tin." << endl;
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về đọc và viết tệp tin:

```cpp
#include <fstream>
using namespace std;

int main() {
    // Viết tệp tin
    ofstream outfile("example.txt");
    if (outfile.is_open()) {
        outfile << "Xin chào, thế giới!" << endl;
        outfile.close();
        cout << "Đã viết vào tệp tin." << endl;
    } else {
        cout << "Không thể viết vào tệp tin." << endl;
    }

    // Đọc tệp tin
    ifstream infile("example.txt");
    if (infile.is_open()) {
        string line;
        while (getline(infile, line)) {
            cout << line << endl;
        }
        infile.close();
    } else {
        cout << "Không thể đọc tệp tin." << endl;
    }

    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình để ghi dữ liệu vào tệp tin. Dữ liệu sẽ được nhập từ người dùng.

Bài tập 2: Tạo một chương trình để đọc dữ liệu từ tệp tin và hiển thị lên màn hình.

Bài tập 3: Tạo một chương trình để sao chép nội dung từ tệp tin này sang tệp tin khác.

Những bài tập trên sẽ giúp bạn nắm vững hơn về cách làm việc với tệp tin trong C++. Hãy thực hành và tìm hiểu thêm về các hàm và lớp liên quan đến tệp tin trong C++.