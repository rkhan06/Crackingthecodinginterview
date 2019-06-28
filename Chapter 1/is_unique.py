import unittest
from collections import Counter


def is_unique(s):
    c = Counter()
    for i in s:
        c[i] += 1
        if c[i] > 1:
            return False
    return True

#### Without using additional datastructure


def is_unique_2(s):
    if len(s) > 128:
        return False
    check = [False]*128
    for i in range(len(s)):
        if check[ord(s[i])]:
            return False
        else:
            check[ord(s[i])] = True
    return True

class Test(unittest.TestCase):
    data = [("ramen", True),
            ("asdaffa", False),
            ("abcdefgh", True),
            ("isthunqe", True),
            ("piuytreqw", True),
            ("lkjhgfdsa", True),
            ("asdjahkajshkjaakfabasdhaskd",False)]

    def test_unique(self):
        for [str, output] in self.data:
            result = is_unique_2(str)
            self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
