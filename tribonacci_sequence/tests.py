import unittest
import tribonacci_sequence as ts


class Tests(unittest.TestCase):

    def test_empty_return(self):
        signature = [1, 1, 1]
        n = 0
        self.assertEqual(ts.tribonacci(signature, n), [])

    def test_return_less_than_signature(self):
        signature = [1, 1, 1]
        n = 2
        self.assertEqual(ts.tribonacci(signature, n), [1, 1])

    def test_return_signature_only(self):
        signature = [1, 1, 1]
        n = 3
        self.assertEqual(ts.tribonacci(signature, n), [1, 1, 1])

    def test_return_several(self):
        signature = [1, 1, 1]
        n = 5
        self.assertEqual(ts.tribonacci(signature, n), [1, 1, 1, 3, 5])

    def test_return_shifted(self):
        signature = [0, 1, 1]
        n = 5
        self.assertEqual(ts.tribonacci(signature, n), [0, 1, 1, 2, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
