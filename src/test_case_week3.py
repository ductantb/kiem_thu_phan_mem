# test_paths.py
import pytest
from src.tax import calc_tax

def test_P1_error():
    with pytest.raises(ValueError): calc_tax(-1, 100)

def test_P2_lambda_le_0():
    assert calc_tax(100, 80) == (0.0, 0.0)

def test_P3_0_lt_lambda_le_0_30():
    assert calc_tax(100, 120) == (0.05, 5.0)

def test_P4_0_30_lt_lambda_le_0_60():
    assert calc_tax(100, 160) == (0.10, 10.0)

def test_P5_lambda_gt_0_60():
    assert calc_tax(100, 300) == (0.15, 15.0)
