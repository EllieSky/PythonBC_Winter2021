import unittest

from tests.my_first_test import find_sum


class TestTimeConverter(unittest.TestCase):
    def test_positive_hours(self):
        actual_seconds = self.convert_into_seconds(hours=4)
        # actual_seconds = convert_into_seconds(4, 0, 0)
        self.assertEqual(14400, actual_seconds)

    def test_positive_minutes(self):
        actual_seconds = self.convert_into_seconds(minutes=34)
        # actual_seconds = convert_into_seconds(0, 34, 0)
        self.assertEqual(2040, actual_seconds)

    def test_positive_minutes_and_seconds(self):
        actual_seconds = self.convert_into_seconds(minutes=25, seconds=100)
        ##### SAME AS:
        # actual_seconds = convert_into_seconds(0, 100, 25)
        self.assertEqual(6025, actual_seconds)

    def test_positive_combination(self):
        actual_seconds = self.convert_into_seconds(1, 34, 12)
        self.assertEqual(5652, actual_seconds)

    def test_negative_input(self):
        actual_seconds = self.convert_into_seconds(1, 1, -12)
        self.assertEqual(None, actual_seconds)

    def test_negative_input_minutes(self):
        actual_seconds = self.convert_into_seconds(1, -1, 0)
        self.assertEqual(None, actual_seconds)

    def convert_into_seconds(hours=0, minutes=0, seconds=0):
        if seconds < 0 or minutes < 0 or hours < 0:
            print("Negative input for time units is not allowed, please use a positive number")
        else:
            return ((hours * 60) + minutes) * 60 + seconds

    # This is just to show how to "test" a function that is outside the module
    def test_find_sum_from_another_file(self):
        self.assertEqual(104.3, find_sum(60.3, 44))





# def convert_into_seconds(hours, minutes, seconds):
#     if seconds < 0:
#         print("Negative input for seconds is not allowed, please use a positive number")
#     elif minutes < 0:
#         print("Negative minutes are invalid input. Please try again")
#     elif hours < 0:
#         print("Negative hours are also a bad idea. Please choose another number")
#     else:
#         return ((hours * 60) + minutes) * 60 + seconds
#
#     ### return hours * 3600 + minutes * 60 + seconds


# Using only IF BLOCKS:
# def convert_into_seconds(hours, minutes, seconds):
#     if seconds < 0:
#         print("Negative input for seconds is not allowed, please use a positive number")
#         return
#
#     if minutes < 0:
#         print("Negative minutes are invalid input. Please try again")
#         return
#
#     if hours < 0:
#         print("Negative hours are also a bad idea. Please choose another number")
#         return
#
#     return ((hours * 60) + minutes) * 60 + seconds



if __name__ == '__main__':
    unittest.main()
