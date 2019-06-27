from collections import Counter
import unittest


def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    c = Counter()
    for i in s1:
        c[i] += 1
    for i in s2:
        if c[i] == 0:
            return False
        else:
            c[i] -= 1
    return True


class Test(unittest.TestCase):
    data = [("ramen", "nemar", True),
            ("abcderf", "abcdgre", False),
            ("qwerttty", "tttqwery", True),
            ("aaaaaaaaaa", "aaaaaaaaaaaaaaa", False),
            ("lkjhg", "ghjkl", True),
            ("zxcvbnm", "mnbvcxx", False),
            ("asdfghjkl", "kljhgdfas", True),
            ("poiuyt", "rtyuiop", False),
            ("ccccccccccccvcv", "cvcvvcvcvcvcvc", False),
            ("abc", "cba", True),
            ("cat", "cta", True),
            ("adc", "a", False)]

    def test_permutation(self):
        for [test_str1, test_str2, output] in self.data:
            res = check_permutation(test_str1, test_str2)
            self.assertEqual(res, output)


if __name__ == '__main__':
    unittest.main()