from unittest import TestCase


class MultiTest(TestCase):
    def test_proverka(self):
        res = 3 * 2
        self.assertEqual(res, 7)


