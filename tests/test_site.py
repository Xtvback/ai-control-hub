import tempfile
import unittest
from pathlib import Path
from scripts.check_site import check

class SiteTests(unittest.TestCase):
    def test_demo_site(self):
        self.assertTrue(check())

    def test_missing_index(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Missing index"):
                check(Path(directory))

if __name__ == "__main__":
    unittest.main()
