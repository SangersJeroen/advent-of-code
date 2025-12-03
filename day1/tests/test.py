import unittest
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.datastructures import Dial
from lib.fileio import read_and_sanitize


class DialTester(unittest.TestCase):
    def initialisation(self):
        dial = Dial(starting_position=50, highest_number=99)
        assert dial.current_number == 50
        assert dial.roll_over == 99
        assert dial.history == list()

    def test_right(self):
        dial = Dial(starting_position=0, highest_number=10)
        dial.right(2)

        assert dial.current_number == 2
        assert dial.history == [2]

    def test_left(self):
        dial = Dial(starting_position=2, highest_number=10)
        dial.left(2)

        assert dial.current_number == 0
        assert dial.history == [0]

    def test_associativity(self):
        dial = Dial(starting_position=50)
        dial.left(2)
        dial.right(2)

        assert dial.history == [48, 50]
        assert dial.current_number == 50

    def test_rollover(self):
        dial = Dial(starting_position=5, highest_number=9)

        dial.right(4)
        assert dial.current_number == 9

        dial.right(1)
        assert dial.current_number == 0

    def test_extra_zeros(self):
        dial = Dial(starting_position=5, highest_number=9)

        dial.right(10)
        assert dial.current_number == 5
        assert dial.exact_history.count(0) == 1

    def test_case(self):
        dial = Dial()
        input = read_and_sanitize(1)
        for line in input:
            dir, number = line[0], int(line[1:])
            if dir == 'L':
                dial.left(number)
            else:
                dial.right(number)
            print(dial.current_number)
            print(dial.exact_history)

        assert dial.current_number == 32
        assert dial.history == [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
        assert dial.history.count(0) == 3
        assert dial.exact_history.count(0) == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
