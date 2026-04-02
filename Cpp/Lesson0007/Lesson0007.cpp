#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới để ghi
    ofstream tepTinGhi("example.txt");
    if (tepTinGhi.is_open()) {
        // Ghi nội dung vào tệp tin
        tepTinGhi << "Xin chào, thế giới!";
        tepTinGhi.close();
        cout << "Ghi tệp tin thành công!" << endl;
    } else {
        cout << "Không thể mở tệp tin để ghi!" << endl;
    }

    // Đọc nội dung từ tệp tin
    ifstream tepTinDoc("example.txt");
    if (tepTinDoc.is_open()) {
        string dong;
        while (getline(tepTinDoc, dong)) {
            // In nội dung đọc được
            cout << "Nội dung tệp tin: " << dong << endl;
        }
        tepTinDoc.close();
    } else {
        cout << "Không thể mở tệp tin để đọc!" << endl;
    }

    return 0;
}