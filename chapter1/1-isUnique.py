import unittest


def is_unique(s):
    # Assuming ASCII
    if len(s) > 128:
        return False  # Pigeonhole principle

    # Set of characters found
    chars = set()

    # Loop through all characters in word
    for char in s:
        # If not found, add to set
        if not char in chars:
            chars.add(char)
        else:
            # We found it, therefore, not unique
            return False

    # If we finished the loop without returning, then it's unique
    return True


def is_unique_2(s):
    # This method will work without using any extra data structures
    # Assuming ASCII
    if len(s) > 128:
        return False  # Pigeonhole principle

    # Loop through all characters in the word
    for count_i, char_a in enumerate(s):
        for count_j, char_b in enumerate(s):
            if count_i != count_j and char_a == char_b:
                return False

    return True


class Test(unittest.TestCase):
    true_values = [
        (''),
        ('abc'),
        ('123'),
        ('ab cd'),
        ('ab12')
    ]
    false_values = [
        ('abab'),
        ('aa'),
        ('1238db1'),
        ('abc abc'),
        ('rhsnzpbyzsdxhboxoqubjfqahhkcuaoigeynrwkctxorhxgbflzdfiytafufwzlyzuhorjcikrjwzwsemtetoxfcuzyjohbnmpqgihdumnmbpkwdnkhdodsnysdhgdhaf')
    ]

    def test_unique(self):
        for str in self.true_values:
            self.assertTrue(is_unique(str))
        for str in self.false_values:
            self.assertFalse(is_unique(str))

    def test_unique_2(self):
        for str in self.true_values:
            self.assertTrue(is_unique_2(str))
        for str in self.false_values:
            self.assertFalse(is_unique_2(str))


if __name__ == "__main__":
    unittest.main()
