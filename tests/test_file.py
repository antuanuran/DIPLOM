from unittest import TestCase


class MultiTest(TestCase):
    def test_proverka(self):
        res = 3 * 2
        self.assertEqual(res, 6)


# def test_Multi():
#     res = 3 * 2
#     assert res == 6
