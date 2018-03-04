## PROBLEM:
# Write a program which takes an input an array of digits encoding an decimal number D and then updates the array to represent the number D + 1. For example, if the input is [1,2,9] then you should update the array to [1,3,0]. Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

# source - EPI - page 62

import unittest


def add_1(arr):
    last_digit = (arr[-1] + 1) % 10
    carry = False if arr[-1] + 1 <= 9 else True
    arr = arr[:-1]
    ans = []
    ans.append(last_digit)
    for i in reversed(arr):
        if carry:
            ans.append((i + 1) % 10)
            if i + 1 >= 10:
                carry = True
            else:
                carry = False
        else:
            ans.append(i)
    if carry:
        ans.append(1)
    ans.reverse()
    return ans


class add_1_tests(unittest.TestCase):

    def test_onetwonnine(self):
        self.assertEqual(add_1([1,2,9]), [1,3,0])

    def test_zero(self):
        self.assertEqual(add_1([0]),[1])

    def test_ninety_nine(self):
        self.assertEqual(add_1([9,9]), [1,0,0])

    def test_very_large_number(self):
        self.assertEqual(add_1([9,9,9,9,9,9,9,9,9,9,9,9,9,9]),[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
