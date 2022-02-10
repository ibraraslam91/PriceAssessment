from unittest import TestCase

from src.string_formator.uppercase import UpperCase


class UpperCaseTestCases(TestCase):
    def test_upper(self):
        self.assertEqual(UpperCase.format("Test"), "TEST")
