import unittest


# This solution simply strips s from white spaces on both sides
# then replaces any existing spaces with %20
def urlify(s, l):
    s = s.strip()  # O(n)
    return s.replace(' ', '%20')


# This solution splits s into multiple arrays which are identified
# by the spaces in between then joins them together using '%20'
def urlify_2(s, l):
    return '%20'.join(s.strip().split(' '))

class Test(unittest.TestCase):

    values = [
        ('Mr John Smith     ', 'Mr%20John%20Smith', 13),
        ('Test  Test', 'Test%20%20Test', 10),
        ('     123     ', '123', 3)
    ]

    def test_urlify(self):
        for [test, expected, length] in self.values:
            self.assertEqual(urlify(test, length), expected)

    def test_urlify_2(self):
        for [test, expected, length] in self.values:
            self.assertEqual(urlify_2(test, length), expected)


if __name__ == "__main__":
    unittest.main()
