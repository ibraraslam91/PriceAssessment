from unittest import TestCase

from src.file_generator.csv_generator import CSVGenerator


class CSVUtilsTestCases(TestCase):
    def test_string_transformer(self):
        self.assertEqual(CSVGenerator().transformer("Test"), ["T", "e", "s", "t"])
