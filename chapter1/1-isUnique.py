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


class Test(unittest.TestCase):
    true_values = [(''), ('abc'), ('123'), ('ab cd'), ('ab12')]
    false_values = [('abab'), ('aa'), ('1238db1'), ('abc abc'),
                    ('rhsnzpbyzsdxhboxoqubjfqahhkcuaoigeynrwkctxorhxgbflzdfiytafufwzlyzuhorjcikrjwzwsemtetoxfcuzyjohbnmpqgihdumnmbpkwdnkhdodsnysdhgdhaf')]

    def test_unique(self):
        for str in self.true_values:
            self.assertTrue(is_unique(str))
        for str in self.false_values:
            self.assertFalse(is_unique(str))


if __name__ == "__main__":
    unittest.main()
