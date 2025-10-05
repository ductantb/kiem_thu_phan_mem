def calc_tax(E: float, I: float) -> tuple[float, float]:
    """
    Tính thuế dựa trên tỷ lệ tăng trưởng thu nhập.

    Tham số:
        E (float): Thu nhập ban đầu.
        I (float): Thu nhập hiện tại.

    Trả về:
        tuple[float, float]: (tax_rate, tax_amount)
            - tax_rate: Tỷ lệ thuế áp dụng (%)
            - tax_amount: Số tiền thuế phải nộp

    Quy tắc tính:
        r = (I - E) / max(E, 1)
        Nếu r <= 0      → tax_rate = 0.00
        Nếu r <= 0.3    → tax_rate = 0.05
        Nếu r <= 0.6    → tax_rate = 0.10
        Ngược lại       → tax_rate = 0.15
    """
    # Kiểm tra đầu vào hợp lệ
    if E < 0 or I < 0:
        raise ValueError("Giá trị E và I phải không âm")

    # Tính tỷ lệ tăng trưởng r
    r = (I - E) / max(E, 1)

    # Xác định mức thuế theo tỷ lệ
    if r <= 0:
        tax_rate = 0.0
    elif r <= 0.3:
        tax_rate = 0.05
    elif r <= 0.6:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    # Tính số tiền thuế
    tax_amount = E * tax_rate
    return tax_rate, tax_amount