#test_sample_calc.py
import sample_calc as sc

def test_func_for_positive_int():
    input_value = 3                     # 1. test input
    func_output = sc.func(input_value)  # 2. call function
    assert func_output == 4             # 3. compare output with expected