import unittest
from collections import Counter


def is_unique(s):
    c = Counter()
    for i in s:
        c[i] += 1
        if c[i] > 1:
            return False
    return True


class Test(unittest.TestCase):
    data = [("ramen", True),
            ("asdaffa", False),
            ("abcdefgh", True),
            ("isthunqe", True),
            ("piuytreqw", True),
            ("lkjhgfdsa", True)]

    def test_unique(self):
        for [str, output] in self.data:
            result = is_unique(str)
            self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
