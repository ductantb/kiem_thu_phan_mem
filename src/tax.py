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