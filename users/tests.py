import pytest
from django.contrib.auth import authenticate
from .models import User


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user("vera", "1234")


def test_user_password(db, user):
    assert(User.objects.get().password, '1234')


def test_create_user(db, user):
    print(user, 123454)
    assert user.get_username() == "vera"


@pytest.fixture
def is_admin(db) -> User:
    return User.objects.create_superuser("vera", "1234")


def test_is_admin(db, is_admin):
    assert is_admin.is_superuser == True


@pytest.mark.django_db(True)
class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='vera', password='1234')
        self.user.save()

    def test_correct(self):
        user = authenticate(username='vera', password='1234')
        print(user)
        self.assertTrue(user is not None and user.is_authenticated)
