import email
from website.models import User

def test_new_user():
    user = User(email='softwaretest@gmail.com', first_name='Software', password='TestingIsEasy')
    assert user.email == 'softwaretest@gmail.com'
    assert user.password == 'TestingIsEasy'