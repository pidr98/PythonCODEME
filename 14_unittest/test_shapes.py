import unittest
from shapes import rectangle, triangle

class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.sideA = 6
        self.sideB = 5


    def test_rectangle_with_correct_value(self):
        result = rectangle(6, 5)
        self.assertEqual(result, 30)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.sideA, self.sideB), 15)


    def tearDown(self):
        del self.sideA
        del self.sideB


if __name__ == '__main__':
    unittest.main()