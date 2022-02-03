# from django.test import TestCase
# import pytest
# from django.contrib.auth import authenticate

# from .models import User


# # @pytest.fixture
# # def user(db) -> User:
# #     return User.objects.create("vera")


# # def test_user_password(db, user: User) -> bool:
# #     user.set_password(1234)
# #     assert user.check_password(1234) is True

# # def test_create_category(db):
# #     category = User.objects.create(username="vera")
# #     assert category.username == "vera"


# class RegistrTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         #Set up non-modified objects used by all test methods
#         User.objects.create(username='vera', password='1234')

#     def test_create_user(self):
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().username, 'vera')
#         self.assertEqual(User.objects.get().password, '1234')


# class LoginTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create(username='vera', password='1234')
#         self.user.save()

#     def test_correct(self):
#         user = authenticate(username='vera', password='1234')
#         self.assertTrue(user is not None and user.is_authenticated)
