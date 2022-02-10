from unittest import TestCase

from src.string_formator.altercase import AlterCase


class AlterCaseTestCases(TestCase):
    def test_upper(self):
        self.assertEqual(AlterCase.format("Test"), "tEsT")
