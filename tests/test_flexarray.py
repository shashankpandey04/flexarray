import unittest
from flexarray.array import Array

class TestArray(unittest.TestCase):

    def test_static_array(self):
        arr = Array(3)
        arr[0] = 10
        arr[2] = 20
        self.assertEqual(arr[0], 10)
        self.assertEqual(arr[2], 20)
        self.assertEqual(len(arr), 3)

        arr[5] = 50
        self.assertEqual(len(arr), 6)
        self.assertEqual(arr[5], 50)

    def test_malloc(self):
        arr = Array()
        arr.malloc(5)
        self.assertEqual(len(arr), 5)
        self.assertEqual(arr[0], None)

    def test_realloc(self):
        arr = Array(2)
        arr[0] = 100
        arr[1] = 200
        arr.realloc(5)
        self.assertEqual(len(arr), 5)
        self.assertEqual(arr[0], 100)
        self.assertEqual(arr[1], 200)

    def test_free(self):
        arr = Array(3)
        arr.free()
        self.assertEqual(len(arr), 0)

if __name__ == '__main__':
    unittest.main()
