# 🧪 Kiểm Thử Và Đảm Bảo Chất Lượng Phần Mềm

Repository này lưu trữ **tài liệu, slide và bài tập thực hành** cho môn *Kiểm Thử Phần Mềm*.  
Bên cạnh các ví dụ từ tài liệu, repo còn bao gồm **một bài toán thực tế do sinh viên tự thiết kế**, mô phỏng cách các quốc gia áp dụng mức thuế thương mại dựa trên cán cân xuất–nhập khẩu.

Bài toán có nhiều nhánh điều kiện và được xây dựng để phục vụ mục tiêu:
- Phân tích **Control Flow Graph (CFG)**  
- Thiết kế test case theo độ phủ **C1 – C2 – C3**  
- Nhận diện lỗi logic và rủi ro trong tính toán  

---

# 🌍 Bài toán tự xây dựng – *Tính thuế thương mại dựa trên cán cân xuất–nhập khẩu (E–I)*

Bài toán mô phỏng cách **một quốc gia A** bị tính mức thuế bởi **các quốc gia khác** dựa trên sự thay đổi cán cân thương mại của quốc gia A.

### ✔️ Ý nghĩa các tham số:

| Tham số | Ý nghĩa |
|--------|---------|
| **E** | Giá trị **xuất khẩu** (Export) của quốc gia A |
| **I** | Giá trị **nhập khẩu** (Import) của quốc gia A |

Cán cân thương mại là thước đo cho sức khỏe kinh tế và khả năng cạnh tranh của một quốc gia. Các quốc gia thường áp dụng mức thuế cao hơn khi **nhập khẩu tăng nhanh hơn xuất khẩu**, vì điều này có thể gây mất cân bằng kinh tế và tạo rủi ro thương mại.

---

# 📌 Quy tắc tính thuế thương mại

Ta định nghĩa **tỷ lệ biến động thương mại r** như sau:

\[
r = \frac{I - E}{\max(E, 1)}
\]

Ý nghĩa của r:
- r ≤ 0 → quốc gia **xuất siêu** → không áp thuế
- r > 0 → quốc gia **nhập siêu** → áp mức thuế tương ứng theo mức độ mất cân bằng

### ✔️ Mức thuế theo r:

| Điều kiện (r)        | Giải thích                          | Thuế suất áp dụng |
|----------------------|--------------------------------------|--------------------|
| r ≤ 0                | Xuất siêu / không nhập siêu          | **0%**            |
| 0 < r ≤ 0.3          | Nhập siêu nhẹ                        | **5%**            |
| 0.3 < r ≤ 0.6        | Nhập siêu trung bình                 | **10%**           |
| r > 0.6              | Nhập siêu nặng                       | **15%**           |

### ✔️ Số tiền thuế phải nộp:

\[
tax\_amount = E \times tax\_rate
\]

— Thuế đánh trên **giá trị xuất khẩu E** vì đây là dòng hàng hóa quốc gia A đưa ra thị trường quốc tế và bị đánh thuế bởi các quốc gia khác.

---

# 🧩 Mã nguồn bài toán

```python
def calc_tax(E: float, I: float) -> tuple[float, float]:
    """
    Tính mức thuế thương mại dựa trên cán cân xuất–nhập khẩu của một quốc gia.

    Tham số:
        E (float): Giá trị xuất khẩu (Export)
        I (float): Giá trị nhập khẩu (Import)

    Trả về:
        (tax_rate, tax_amount):
            - tax_rate: Thuế suất áp dụng (%)
            - tax_amount: Số tiền thuế phải nộp

    Quy tắc:
        r = (I - E) / max(E, 1)
        r <= 0      → tax_rate = 0.00
        r <= 0.3    → tax_rate = 0.05
        r <= 0.6    → tax_rate = 0.10
        r > 0.6     → tax_rate = 0.15
    """

    if E < 0 or I < 0:
        raise ValueError("Giá trị E và I phải không âm")

    r = (I - E) / max(E, 1)

    if r <= 0:
        tax_rate = 0.0
    elif r <= 0.3:
        tax_rate = 0.05
    elif r <= 0.6:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = E * tax_rate
    return tax_rate, tax_amount
```
# 🧪 PHẦN KIỂM THỬ – PHÂN TÍCH & THIẾT KẾ TEST CASE

Phần này mô tả cách áp dụng **kỹ thuật kiểm thử hộp trắng** cho bài toán `calc_tax(E, I)`.

Bao gồm:
- Xây dựng CFG  
- Xác định các quyết định logic  
- Sinh đường đi độc lập  
- Thiết kế test case đảm bảo các mức độ bao phủ C1–C2–C3  
- Kiểm thử biên, kiểm thử lỗi  
- Chạy test tự động và đo coverage  
