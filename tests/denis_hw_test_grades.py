import unittest


class GradingSystem(unittest.TestCase):
    def test_student_grade(self):
        # Follow the "grade" method below to test (ex.: enter 78 to pass the test with the B grade)
        actual_grade = grade(score)
        self.assertEqual("B", actual_grade)

        # Follow the "grade" method below to test (ex.: enter 78 to pass the test with the F grade)
    def test_reverse_student_grade(self):
        actual_grade = grade(score)
        self.assertNotEqual("F", actual_grade)


def grade(scr):
    if scr < 45:
        return "F"
    if 45 <= scr <= 50:
        return "D"
    if 50 <= scr <= 60:
        return "C"
    if 60 <= scr <= 80:
        return "B"
    else:
        return "A"


score = int(input("Please enter a score: "))

while score < 0:
    print("Score can not be negative number!")
    score = int(input("Please enter a score: "))

    if score > 100:
        print("Score can not be more than 100!")
        score = int(input("Please enter a score: "))


print("Your grade is: " + grade(score))

if __name__ == '__main__':
    unittest.main()