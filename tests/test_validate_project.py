import tempfile
import unittest
from pathlib import Path

from scripts.validate_project import REQUIRED, validate


class ValidateProjectTests(unittest.TestCase):
    def test_current_project(self):
        self.assertEqual(validate(), len(REQUIRED))

    def test_missing_files_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Missing required files"):
                validate(Path(directory))


if __name__ == "__main__":
    unittest.main()
