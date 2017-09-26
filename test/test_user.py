from tinydb import where

from models import (
    User
)

user = User('email@anonmail.com', 'weakpass')


def test_default_attributes():
    assert user.id is not None
    assert user.created is not None
    assert user.modified is not None
    assert user.table_name is not None


def test_user_create():
    """ It should create a new user """
    email = 'lym@lym.com'
    passw = 'lympass'
    table = user.db.table('users')
    len_before = len(table.all())

    User.create(email=email, password=passw)
    len_after = len(table.all())
    assert len(user.db.table(user.table_name).all()) != 0
    assert len_before != len_after


def test_delete_user():
    """ It should delete a User instance from the database """
    email = 'lym@lym.com'
    passw = 'lympass'
    table = user.db.table('users')
    User.create(email=email, password=passw)

    len_before = len(table.all())
    rec_id = table.all()[-1].get('id')  # Get last-saved item
    User.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after
