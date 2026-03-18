# Antoanthongtin_NguyenHoangVanThanh20234035
Tổng hợp bài tập thực hành An Toàn Thông Tin - E9
## Bài tập tuần 4: Cài đặt thuật toán mã hóa RC4

Đây là mã nguồn Python mô phỏng thuật toán RC4 được tùy chỉnh theo yêu cầu của bài tập thực hành.

### 📝 Chi tiết bài toán
Thuật toán được cài đặt với thông số đầu vào cụ thể:
- **Vector trạng thái (State Vector):** $S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]$ (Kích thước $N = 10$, tính toán theo modulo 10).
- **Khóa hạt mầm (Seed Key):** $K = [2, 4, 1, 7]$
- **Bản rõ (Plaintext):** `cybersecurity`

### ⚙️ Luồng hoạt động của chương trình
1. **Giai đoạn KSA (Key-Scheduling Algorithm):** Khởi tạo và xáo trộn mảng $S$ dựa trên khóa $K$ bằng các phép toán modulo 10.
2. **Giai đoạn PRGA (Pseudo-Random Generation Algorithm):** Sinh dòng khóa (Keystream) có độ dài bằng với chiều dài chuỗi bản rõ (13 ký tự).
3. **Mã hóa (Encryption):** Chuyển đổi chuỗi `cybersecurity` sang mã thập phân ASCII và thực hiện phép toán XOR bitwise với dòng khóa để tạo ra bản mã $C(t)$.

### 🚀 Hướng dẫn chạy chương trình
Đảm bảo máy tính đã cài đặt Python 3. Mở terminal tại thư mục chứa dự án và chạy lệnh sau:

```bash
python rc4_assignment.py
