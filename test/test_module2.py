import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

import unittest
from package2 import module2 as m2


class TestModule2(unittest.TestCase):
    def test_self_test(self):
        self.assertIsNone(m2.self_test())

    def test_func1(self):
        self.assertIsNone(m2.func1())

    def test_func2(self):
        self.assertIsNone(m2.func2())

    def test_farwell(self):
        self.assertIsNot(
            m2.farewell(), "Goodbye! Sayonara from Module 2. Anonymous user."
        )


if __name__ == "__main__":
    unittest.main()
