class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a+b == expected_sum, f'Сума перемінних {a} і {b} не дорівнює {expected_sum}'

    def test_check_math2(self):
        a = 5
        b = 10
        expected_sum = 14
        assert a+b == expected_sum, f'Сума перемінних {a} і {b} не дорівнює {expected_sum}'

    def test_check_math3(self):
        a = 5
        b = a
        expected_sum = 14
        assert a+b == expected_sum, f'Сума перемінних {a} і {b} не дорівнює {expected_sum}'

