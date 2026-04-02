#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Tạo một tệp mới để viết dữ liệu
    ofstream tepViet("tep_viet.txt");
    
    // Kiểm tra nếu tệp được mở thành công
    if (tepViet.is_open()) {
        // Viết dữ liệu vào tệp
        tepViet << "Xin chào, đây là tệp văn bản được tạo bằng C++!" << endl;
        
        // Đóng tệp
        tepViet.close();
        cout << "Đã tạo tệp thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp!" << endl;
    }

    // Mở tệp để đọc dữ liệu
    ifstream tepDoc("tep_viet.txt");
    
    // Kiểm tra nếu tệp được mở thành công
    if (tepDoc.is_open()) {
        char chuoi[100];
        
        // Đọc dữ liệu từ tệp
        while (tepDoc.getline(chuoi, 100)) {
            cout << chuoi << endl;
        }
        
        // Đóng tệp
        tepDoc.close();
    } else {
        cout << "Không thể mở tệp!" << endl;
    }

    return 0;
}