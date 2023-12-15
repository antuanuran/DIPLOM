from unittest import TestCase


class MultiTest(TestCase):
    def test_1(self):
        res = 3 * 2
        self.assertEqual(res, 6)




# assertEqual(a, b)	            Проверяет, что a == b
# assertNotEqual(a, b)	        Проверяет, что a != b
# assertTrue(x)	                Проверяет, что значение x истинно
# assertFalse(x)	                Проверяет, что значение x ложно
# assertIn(элемент, список)	    Проверяет, что элемент входит в список
# assertNotIn(элемент, список)    Проверяет, что элемент не входит в спис
