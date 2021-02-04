# Virginia Link
# Unit test in class activity calculator unittest
# 02/04/2021

import unittest
import calculator


class Test(unittest.TestCase):
    # Tests for add
    def test_add1(self):
        result = calculator.add(2,2)
        self.assertEqual(result, 4)
    def test_add2(self):
        result = calculator.add(0,0)
        self.assertEqual(result,0)
    # Tests for sub
    def test_sub1(self):
        result = calculator.sub(2,2)
        self.assertEqual(result,0)
    def test_sub2(self):
        result = calculator.sub(0,1)
        self.assertEqual(result,-1)
    # Tests for mult
    def test_mult1(self):
        result = calculator.mult(2,2)
        self.assertEqual(result,4)
    def test_mult2(self):
        result = calculator.mult(2,0)
        self.assertEqual(result,0)
    # Tests for div
    def test_div1(self):
        result = calculator.div(2,2)
        self.assertEqual(result,1)
    def test_div2(self):
        self.assertRaises(ZeroDivisionError, calculator.div, 2, 0)


if __name__ == '__main__':
    unittest.main()





