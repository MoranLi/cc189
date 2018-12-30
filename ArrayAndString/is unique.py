import unittest
'''
implement a function to check if a string have all unique characters
'''


class UniqueString:

    def is_unique_with_set(self, s):
        char_set = set([])
        for i in s:
            if i in char_set:
                return False
            char_set.add(i)
        return True

    def is_unique(self, s):
        chars = []
        for i in s:
            if i in chars:
                return False
            chars.append(i)
        return True


class UniqueStringTest(unittest.TestCase):

    def test_is_unique_with_set(self):
        unique_string = UniqueString()
        self.assertTrue(unique_string.is_unique_with_set("asdfg"))
        self.assertFalse(unique_string.is_unique_with_set("asdff"))
        self.assertFalse(unique_string.is_unique_with_set("aasdf"))
        self.assertFalse(unique_string.is_unique_with_set("asddf"))
        self.assertFalse(unique_string.is_unique_with_set("asdfa"))

    def test_is_unique(self):
        unique_string = UniqueString()
        self.assertTrue(unique_string.is_unique("asdfg"))
        self.assertFalse(unique_string.is_unique("asdff"))
        self.assertFalse(unique_string.is_unique("aasdf"))
        self.assertFalse(unique_string.is_unique("asddf"))
        self.assertFalse(unique_string.is_unique("asdfa"))


if __name__ == '__main__':
    unittest.main()
