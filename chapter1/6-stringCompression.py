import unittest


def string_compression(s):
  chars = dict()
  for c in s:
    if c in chars.keys():
      chars[c] += 1
    else:
      chars[c] = 1
  length = 0
  for _, v in chars.items():
    length = length + 1 + len(str(v))
  return s if len(s) <= length else ''.join("%s%s" % (k, str(v)) for (k, v) in chars.items())


class Test(unittest.TestCase):

  pairs = [
    ('aabb', 'aabb'),
    ('abab', 'abab'),
    ('aaabb', 'a3b2'),
    ('aaab', 'aaab'),
    ('aoibaoiba', 'a3o2i2b2')
  ]

  def test_string_compressions(self):
    for inp, out in self.pairs:
      self.assertEqual(string_compression(inp), out)

if __name__ == '__main__':
  unittest.main()
