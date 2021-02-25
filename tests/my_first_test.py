import unittest


class TestsForFindSum(unittest.TestCase):
    @unittest.expectedFailure
    def test_adding_positive_numbers(self):
        actual = find_sum(7, 14)
        self.assertEqual(27, actual)

    def test_adding_negative_numbers(self):
        actual = find_sum(-17, 14)
        self.assertEqual(-3, actual)


def find_sum(first, second):
    result = first + second
    print(result)
    return result


if __name__ == '__main__':
    unittest.main()
