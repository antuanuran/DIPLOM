# import pytest
#
# from apps.users.models import User
#
#
# @pytest.mark.django_db
# def test_getbasket():
#     user = User.objects.create_user("qwerqreweq@gmail.com")
#     assert user.is_vendor is False


from unittest import TestCase


class MultiTest(TestCase):
    def test_1(self):
        res = 3 * 3
        self.assertEqual(res, 9)
