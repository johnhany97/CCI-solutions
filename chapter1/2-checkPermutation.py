import unittest


def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_chars = {}

    for char in s1:
        if not char in s1_chars:
            s1_chars[char] = 1
        else:
            s1_chars[char] += 1

    for char in s2:
        if not char in s1_chars:
            return False
        else:
            s1_chars[char] -= 1
            if s1_chars[char] == 0:
                del s1_chars[char]

    return True


class Test(unittest.TestCase):
    true_values = [
        ('abc', 'cba'),
        ('123', '321'),
        ('abs2', 'bs2a'),
        ('abc', 'abc'),
        ('', '')
    ]
    false_values = [
        ('a', 'ab'),
        ('abbc', ''),
        ('12490', '0924a')
    ]

    def test_check_permutation(self):
        for pair in self.true_values:
            self.assertTrue(check_permutation(*pair))
        for pair in self.false_values:
            self.assertFalse(check_permutation(*pair))


if __name__ == "__main__":
    unittest.main()
