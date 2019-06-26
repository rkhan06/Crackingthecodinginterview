from collections import Counter
import unittest


def permutation(s):
    c = Counter()
    set_s = set(s)
    if len(set_s) == 1:
        return True
    check = 0
    for i in s:
        c[i] += 1
    for i in set_s:
        if c[i] % 2 != 0:
            check += 1
    if check < 2:
        return True
    else:
        return False


class Test(unittest.TestCase):
    """Test Cases to check permutations of palindrome"""
    data = [("taco cat", True),
            ("abbba", True),
            ("abbb bbba", True),
            ("aaaaaaaaa", True),
            ("club house esuoh bluc", True),
            ("this should be false", False),
            ("taco bat", False)
            ]

    def test_palindrome(self):
        for [test_str, returned] in self.data:
            result = permutation(test_str.replace(" ", ""))

        self.assertEqual(result,returned)


if __name__ == "__main__":
    unittest.main()





