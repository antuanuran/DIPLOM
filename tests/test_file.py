from unittest import TestCase


class MultiTest(TestCase):
    def test_1(self):
        res = 3 * 2
        self.assertEqual(res, 6)
