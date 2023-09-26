import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def setUp(self):
        self.standard_array = [1, 2, 3, 4, 5]
        self.empty_array = []

    def test_get(self):
        self.assertEqual(arrs.get(self.standard_array, 1, "test"), 2)
        self.assertEqual(arrs.get(self.standard_array, 5, "test"), "test")
        self.assertEqual(arrs.get(self.standard_array, 3), 4)
        self.assertEqual(arrs.get(self.empty_array, 0, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice(self.standard_array, 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice(self.standard_array, 1), [2, 3, 4, 5])
        self.assertEqual(arrs.my_slice(self.standard_array, -3), [3, 4, 5])
        self.assertEqual(arrs.my_slice(self.standard_array, -3, -1), [3, 4])
        self.assertEqual(arrs.my_slice(self.standard_array, None, None), self.standard_array)
        self.assertEqual(arrs.my_slice(self.empty_array), [])

if __name__ == '__main__':
    unittest.main()
