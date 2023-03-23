import pytest

from app import crud
from app.models import User
from app.schemas import UserCreate


@pytest.fixture()
def create_user(db) -> User:
    email = "email@example.com"
    password = "password"
    user_in = UserCreate(email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    return user
