import pytest
from website.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User('softwaretest@gmail.com', 'TestingIsEasy')
    return user

