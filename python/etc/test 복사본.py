import unittest


def add_two_numbers(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_numbers_3_4(self):
        # 3+4 must be 7
        self.assertEqual(add_two_numbers(3, 4), 7)

    def test_numbers_0_0(self):
        # 0+0 must be 0
        self.assertEqual(add_two_numbers(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
