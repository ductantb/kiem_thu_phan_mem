import pytest
from src.tax import calc_tax

def test_tax_case_1():
    with pytest.raises(ValueError):
        calc_tax(-1, 100)

def test_tax_case_2():
    assert calc_tax(100, 80) == (0.0, 0.0)

def test_tax_case_3():
    assert calc_tax(100, 120) == (0.05, 5.0)

def test_tax_case_4():
    assert calc_tax(100, 160) == (0.10, 10.0)

def test_tax_case_5():
    assert calc_tax(100, 300) == (0.15, 15.0)

def test_DF1_negative_I_raises():
    with pytest.raises(ValueError):
        calc_tax(100, -5)

def test_DF2_r_equals_0_boundary():
    assert calc_tax(100, 100) == (0.0, 0.0)

def test_DF3_r_equals_0_3_boundary():
    assert calc_tax(100, 130) == (0.05, 5.0)


