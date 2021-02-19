import unittest

from parameterized import parameterized, parameterized_class


@parameterized_class(('name', 'age'), [
    ("John", 30),
    ("Jane", 13),
    ("Vikki", 13)
])
class ParamExample(unittest.TestCase):
    @parameterized.expand([
        ('run', 5),
        ('walk', 2),
        ('swim', 3)
    ])
    def test_fitness(self, action, num):
        print(f'{self.name} went for a {num} mile {action}.')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
