import unittest
import random

from Tasks.Zachet_2 import my_sort


class MyTestCase(unittest.TestCase):
    def test_sorted(self):
        arr = [random.randint(13, 25) for _ in range(1000000)]
        self.assertEqual(
            sorted(arr),
            my_sort(arr)
        )


if __name__ == '__main__':
    unittest.main()
