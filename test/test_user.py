from models import (
    User,
    DataStore,
)

user = User('email@anonmail.com', 'weakpass')
ds = DataStore()


def test_default_attributes():
    assert user.id is not None
    assert user.created is not None
    assert user.modified is not None


def test_user_create():
    """ It should create a new user """
    email = 'lym@lym.com'
    passw = 'lympass'
    users = ds.storage.get('users')
    if users is None:
        len_before = 0
    else:
        len_before = len(users)

    ds.create_user(first_name='Tom', last_name='Riddle', email=email,
                   password=passw)

    len_after = ds.storage.get('users').__len__()
    assert len_after != 0
    assert len_before != len_after


def test_retrieve_user():
    ds.create_user(first_name='Harry', last_name='Potter')
    ds.create_user(first_name='Tom', last_name='Riddle')

    # Retrieve random user from database
    record_id = ds.storage.get('users')[0].get('id')
    assert record_id is not None
    searched_item = ds.find_user(record_id)
    assert searched_item is not None


def test_update_user():
    ds.create_user(first_name='Harry', last_name='Potter')
    ds.create_user(first_name='Tom', last_name='Riddle')

    record_id = ds.storage.get('users')[0].get('id')
    assert record_id is not None
    ds.update_user(user_id=record_id, first_name='Lord', last_name='Voldermort')
    updated_user = ds.find_user(record_id)
    assert updated_user.get('data').get('first_name') == 'Lord'

def test_delete_user():
    """ It should delete a User instance from the database """
    email = 'lym@lym.com'
    passw = 'lympass'
    ds.create_user(first_name='Harry', last_name='Potter')

    len_before = ds.storage.get('users').__len__()
    users = ds.storage.get('users')
    record_id = ds.storage.get('users')[0].get('id')
    ds.delete_user(record_id)

    len_after = ds.storage.get('users').__len__()
    found = ds.find_user(record_id)
    assert found is None
    assert len_before != len_after
