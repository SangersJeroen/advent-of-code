import unittest
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Tester(unittest.TestCase):
    def pass(self):
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
