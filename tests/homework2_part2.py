import unittest

'''
Part 2

A: Create the following functionality:

A school has following rules for grading system:
a. Below 45 - F
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A

Create a function which takes a student's test score as input.
The function should determine the student's grade based on the score.
The function should respond with the letter which represents the student's grade.
'''

class StudentGradeTestCase(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual('A', get_grade(100))
        self.assertEqual('A', get_grade(80.01))
        self.assertEqual('B', get_grade(80))
        self.assertEqual('B', get_grade(60))
        self.assertEqual('C', get_grade(59.9))
        self.assertEqual('C', get_grade(50.0))
        self.assertEqual('D', get_grade(49.00))
        self.assertEqual('D', get_grade(45.00))
        self.assertEqual('F', get_grade(44))
        self.assertEqual('F', get_grade(1))
        self.assertEqual('F', get_grade(-11))

        self.assertEqual('A', get_grade('100'))
        self.assertEqual('A', get_grade('99.0'))
        self.assertEqual('A', get_grade('99.99'))

        self.assertRaises(TypeError, lambda: get_grade('SS.00'))
        self.assertRaises(TypeError, lambda: get_grade('Ninety'))


def get_grade(test_score):
    if type(test_score) == str:
        test_score = test_score.split('.')[0]
        if test_score.isdigit():
            test_score = float(test_score)
        else:
            raise TypeError("test_score must be numerical")
    elif type(test_score) != int and type(test_score) != float:
        raise TypeError("test_score must be numerical")

    if test_score < 45:
        return 'F'
    elif test_score > 80:
        return 'A'
    elif 50 > test_score >= 45:
        return 'D'
    elif 60 > test_score >= 50:
        return 'C'
    else:
        return 'B'

if __name__ == '__main__':
    unittest.main()
