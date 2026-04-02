# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin trên đĩa cứng. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp trong ngôn ngữ lập trình C++.

## Lý thuyết
Trong C++, chúng ta có thể làm việc với tệp bằng cách sử dụng các hàm và lớp trong thư viện `fstream`. Thư viện này cung cấp các lớp `ifstream` để đọc tệp, `ofstream` để ghi tệp và `fstream` để đọc và ghi tệp. Để mở một tệp, chúng ta sử dụng hàm `open()` và để đóng tệp, chúng ta sử dụng hàm `close()`. Chúng ta cũng có thể sử dụng toán tử `<<` để ghi dữ liệu vào tệp và toán tử `>>` để đọc dữ liệu từ tệp.

Ví dụ, để mở một tệp tên là `example.txt` và ghi dữ liệu vào tệp, chúng ta có thể sử dụng đoạn code sau:
```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream file("example.txt");
    if (file.is_open()) {
        file << "Đây là nội dung của tệp.";
        file.close();
    } else {
        cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Ví dụ
Chúng ta hãy xem xét một ví dụ khác về việc đọc dữ liệu từ một tệp. Giả sử chúng ta có một tệp tên là `data.txt` chứa các số nguyên, và chúng ta muốn đọc các số nguyên này và tính tổng của chúng. Chúng ta có thể sử dụng đoạn code sau:
```cpp
#include <fstream>
using namespace std;

int main() {
    ifstream file("data.txt");
    if (file.is_open()) {
        int num;
        int sum = 0;
        while (file >> num) {
            sum += num;
        }
        file.close();
        cout << "Tổng của các số nguyên trong tệp là: " << sum;
    } else {
        cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Bài tập
Bài tập cho bạn:
- Tạo một tệp tên là `student.txt` và ghi thông tin của các sinh viên vào tệp này, bao gồm họ tên, tuổi và điểm trung bình.
- Đọc dữ liệu từ tệp `student.txt` và hiển thị thông tin của các sinh viên.
- Tính điểm trung bình của tất cả các sinh viên và hiển thị kết quả.