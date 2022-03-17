import unittest
from Tasks.Zachet_1 import rocket_rent


class MyTestCase(unittest.TestCase):
    def test_invalid(self):
        self.assertFalse(rocket_rent([(0, 12), (2, 6)]))
        self.assertFalse(rocket_rent([(0, 12), (12, 15), (14, 24)]))
        self.assertFalse(rocket_rent([(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17), (13, 14), (18, 23)]))
        self.assertFalse(rocket_rent([(22, 24), (12, 15), (14, 24)]))

    def test_valid(self):
        self.assertTrue(rocket_rent([(12, 15), (19, 23), (7, 10), (16, 17)]))
        self.assertTrue(rocket_rent([(10, 12), (12, 15), (17, 19), (19, 23), (7, 10), (16, 17), (0, 6)]))
        self.assertTrue(rocket_rent([(0, 12), (12, 15), (15, 24)]))


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()