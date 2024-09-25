import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

import unittest
from package1 import module1 as m1


class TestModule1(unittest.TestCase):
    def test_self_test(self):
        self.assertIsNone(m1.self_test())

    def test_func1(self):
        self.assertIsNone(m1.func1())

    def test_func2(self):
        self.assertIsNone(m1.func2())

    def test_greet(self):
        self.assertIsNot(m1.greet(), "Hello! Welcome to Module 1. Anonymous user.")

    def test_author(self):
        self.assertIsNone(m1.author())


if __name__ == "__main__":
    unittest.main()
