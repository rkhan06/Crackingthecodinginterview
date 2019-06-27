import unittest


def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        edited = False
        for i in range(len(s1)):
            if s1[i] != s2[i] and edited:
                return False
            if s1[i] != s2[i] and not edited:
                edited = True

    if len(s2) > len(s1):
        s1, s2 = s2, s1

    if len(s1) > len(s2):
        i = 0
        j = 0
        edited = False
        while i < len(s1) and j < len(s2):

            if s1[i] != s2[j] and edited:
                return False
            if s1[i] != s2[j] and not edited:
                edited = True
                i += 1
            else:
                i += 1
                j += 1

    return True


class Test(unittest.TestCase):
    """Test Cases"""
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bake', False),
        ('pales', 'bakes', False),
        ('pale', 'ple', True),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, returned] in self.data:
            result = one_away(test_s1, test_s2)
            self.assertEqual(result, returned)


if __name__ == "__main__":
    unittest.main()



