import unittest


def one_away(s1, s2):
  if abs(len(s1) - len(s2)) > 1:
    return False
  s1_len = len(s1)
  s2_len = len(s2)
  changeOccured = False
  s1_pointer = 0
  s2_pointer = 0
  while s1_pointer < s1_len and s2_pointer < s2_len:
    if s1[s1_pointer] != s2[s2_pointer]:
      if changeOccured:
        return False
      if s1_len > s2_len:
        s2_pointer = s2_pointer - 1
      elif s1_len < s2_len:
        s1_pointer = s1_pointer - 1
      changeOccured = True
    s1_pointer += 1
    s2_pointer += 1
  return True


class Test(unittest.TestCase):

    true_pairs = [
      ("bake", "cake"),
      ("hello", "hello"),
      ("", "")
    ]
    false_pairs = [
      ("abc", "cde"),
      ("", "asoib"),
      ("bakes", "baka"),
      ("asdb", "adsb")
    ]

    def test_one_away(self):
        for s1, s2 in self.true_pairs:
            self.assertTrue(one_away(s1, s2))
        for s1, s2 in self.false_pairs:
            self.assertFalse(one_away(s1, s2))


if __name__ == '__main__':
    unittest.main()
