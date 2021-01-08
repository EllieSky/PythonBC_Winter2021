import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(self.find_pair([3, 5, 2, 12], 8))
        self.assertTrue(self.find_pair([3, 5, 2, 12], 5))
        self.assertTrue(self.find_pair([3, 5, 2, 12], 14))
        self.assertTrue(self.find_pair([2, 2, 2, 2], 4))
        self.assertFalse(self.find_pair([3, 5, 2, 12], 6))
        self.assertFalse(self.find_pair([3, 5, 2, 12], 12))
        self.assertFalse(self.find_pair([3, 5, 2, 12], 10))

        self.assertTrue(self.find_pair_efficient([3, 5, 2, 12], 8))
        self.assertTrue(self.find_pair_efficient([3, 5, 2, 12], 5))
        self.assertTrue(self.find_pair_efficient([3, 5, 2, 12], 14))
        self.assertTrue(self.find_pair_efficient([2, 2, 2, 2], 4))
        self.assertFalse(self.find_pair_efficient([3, 5, 2, 12], 6))
        self.assertFalse(self.find_pair_efficient([3, 5, 2, 12], 12))
        self.assertFalse(self.find_pair_efficient([3, 5, 2, 12], 10))

    def find_pair(self, alist, sum):
        # return True when 2 items in alist can be added to equal the sum

        for index, num1 in enumerate(alist):
            pair = sum - num1
            for index2 in range(index+1, len(alist)):
                num2 = alist[index2]
                if num2 == pair:
                    print("True")
                    return True
        print("False")
        return False

    def find_pair_efficient(self, alist, sum):
        nice_to_have = []

        for item in alist:
            if nice_to_have.count(item) > 0:
                return True

            pair = sum - item
            nice_to_have.append(pair)
        return False



if __name__ == '__main__':
    unittest.main()

#example interview question