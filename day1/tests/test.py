import unittest

class EmptyTest(unittest.TestCase):
    def empty_test(self):
        self.assertEqual('test', 'test')


if __name__ == '__main__':
    unittest.main()
