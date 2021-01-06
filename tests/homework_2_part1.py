import unittest


'''
Part 1

A: Create the following functionality:

The function should take 2 values representing the length and width of a rectangle.
The function should determine if the rectangle is a square.
When the rectangle is a square, the function should respond True
Otherwise it should respond False

B: Create tests for your function
'''

class IsSquareTestCase(unittest.TestCase):
    def test_is_square_valid(self):
        self.assertTrue(is_square(5, 5))
        self.assertTrue(is_square(5.0, 5))
        self.assertTrue(is_square(3.1, 3.1))
        self.assertTrue(is_square('2', '2'))
        self.assertTrue(is_square('25.0', '25.00'))

        self.assertFalse(is_square(6, 5))
        self.assertFalse(is_square(5.1, 5))
        self.assertFalse(is_square(222.1, 222.1234))
        self.assertFalse(is_square(0, 0))
        self.assertFalse(is_square(0, 99))
        self.assertFalse(is_square(22, 0))
        self.assertFalse(is_square(-99, 77))

        self.assertRaises(TypeError, lambda: is_square('five', 5))
        self.assertRaises(TypeError, lambda: is_square([5], 5))
        self.assertRaises(TypeError, lambda: is_square(3, (3, None)))
        self.assertRaises(TypeError, lambda: is_square(False, (3, None)))


def is_square(width, height):
    if type(width) == str:
        width = width.split('.')[0]
        if width.isdigit():
            width = float(width)
        else:
            raise TypeError("width must be numerical")
    elif type(width) != int and type(width) != float:
        raise TypeError("width must be numerical")

    if type(height) == str:
        height = height.split('.')[0]
        if height.isdigit():
            height = float(height)
        else:
            raise TypeError("height must be numerical")
    elif type(height) != int and type(height) != float:
        raise TypeError("height must be numerical")

    if width <= 0 or height <= 0:
        return False
    elif float(width) == float(height):
        return True
    else:
        return False


if __name__ == '__main__':
    unittest.main()