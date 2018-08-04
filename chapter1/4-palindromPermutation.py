import unittest


def palindrom_permutation(s):
    # Remove spaces
    s.replace(' ', '')

    # Get count of all characters in given string
    chars = {}
    for char in s:
        if not char in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    # Palindroms consist of either an even number of pairs with zero odd pairs.
    # Or, even number of pairs and just one odd pair
    # In this step, we find how many odd number of characters we have
    odd = 0
    for key, value in chars.items():
        if value % 2 != 0:
            odd += 1
    # If none or just one, it's a palindrome permutation
    if odd == 0 or odd == 1:
        return True
    # Otherwise, It's not
    return False


class Test(unittest.TestCase):

    true_values = [
        ('123321'),
        ('aco t cat'),
        ('abab'),
        ('')
    ]

    false_values = [
        ('123322'),
        ('aco cat'),
        ('ababbx')
    ]

    def test_palindrome_permutation(self):
        for s in self.true_values:
            self.assertTrue(palindrom_permutation(s))
        for s in self.false_values:
            self.assertFalse(palindrom_permutation(s))


if __name__ == '__main__':
    unittest.main()
