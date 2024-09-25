"""Test the main_app module."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

import unittest
import main_app


class TestMainApp(unittest.TestCase):
    """Test the main_app module."""

    def test_main(self):
        """Test the main function."""
        self.assertIsNone(main_app.main())


if __name__ == "__main__":
    unittest.main()
