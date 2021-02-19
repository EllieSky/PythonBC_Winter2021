import csv
import os
import unittest

from parameterized import parameterized, parameterized_class

from tests import PROJ_PATH


def get_data_from_csv():
    with open(os.path.join(PROJ_PATH, 'data', 'data.csv')) as file:
        reader = csv.reader(file)
        next(reader)
        return list(map(tuple, reader))

@parameterized_class(('name', 'age'), [
    ("John", 30),
    ("Jane", 13),
    ("Vikki", 13)
])
class ParamExample(unittest.TestCase):
    # @parameterized.expand([
    #     ('run', 5),
    #     ('walk', 2),
    #     ('swim', 3)
    # ])
    @parameterized.expand(get_data_from_csv())
    def test_fitness(self, action, num):
        print(f'{self.name} went for a {num} mile {action}.')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
