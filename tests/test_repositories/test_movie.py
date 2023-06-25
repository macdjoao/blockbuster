from faker import Faker

from src.infra.repositories.movie import MovieRepository

movie_repository = MovieRepository()
fake = Faker()


def test_insert():
    # Fake payload
    fake_name = fake.word()

    # Inserting fake registry
    movie_repository.insert(name=fake_name)

    # Selecting fake registry
    query = movie_repository.select(name=fake_name, available=True)

    # Checking equalities
    assert query[0].name == fake_name
    assert query[0].available == True

    # Cleaning DB
    movie_repository.delete(id=(query[0].id))


def test_insert_ParamIsNotStringError():
    # Setting a not string value
    fake_not_string = fake.random_digit()

    # Trying to insert by passing a not string value as name
    wrong_name_insert = movie_repository.insert(name=fake_not_string)

    # Checking errors
    assert (
        wrong_name_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )


def test_select():
    # Fake payload
    fake_name = fake.word()
    # Inserting fake
    movie_repository.insert(name=fake_name)

    # Selecting fake registry
    query = movie_repository.select(name=fake_name, available=True)

    # Checking equalities
    assert query[0].name == fake_name
    assert query[0].available == True

    # Cleaning DB
    movie_repository.delete(id=(query[0].id))


def test_select_ParamIsNotIntegerError():
    # Setting a not integer id
    fake_not_int_id = fake.word()
    # Trying to select a customer by passing a not integer as id
    query = movie_repository.select(id=fake_not_int_id)

    # Checking error
    assert query == f'Error: Param "{fake_not_int_id}" must be a integer'


def test_select_ParamIsNotStringError():
    # Setting a not string name
    fake_not_string_name = fake.random_digit()
    # Trying to select a customer by passing a not string as name
    wrong_name_query = movie_repository.select(name=fake_not_string_name)

    # Checking errors
    assert (
        wrong_name_query
        == f'Error: Param "{fake_not_string_name}" must be a string'
    )


def test_select_ParamIsNotBoolError():
    # Setting a not boolean is_active
    fake_not_bool_available = fake.word()
    # Trying to select a customer by passing a not boolean as available
    query = movie_repository.select(available=fake_not_bool_available)

    # Checking errors
    assert query == f'Error: Param {fake_not_bool_available} must be a boolean'


def test_update():
    # Fake payload
    fake_name = fake.word()
    # Inserting fake registry
    movie_repository.insert(name=fake_name)

    # Selecting fake registry
    query = movie_repository.select(name=fake_name)

    # Second fake payload
    new_fake_name = fake.word()
    # Update fake registry with second fake payload parameters
    movie_repository.update(id=query[0].id, name=new_fake_name)

    # Selecting updated fake registry
    updated_query = movie_repository.select(id=query[0].id)

    # Check equalities
    assert updated_query[0].name == new_fake_name

    # Cleaning DB
    movie_repository.delete(id=(updated_query[0].id))


def test_update_ParamIsNotIntegerError():
    # Fake wrong type id
    fake_wrong_id = fake.word()
    # Trying to update a registry by passing a not integer id
    update = movie_repository.update(id=fake_wrong_id)

    # Checking error
    assert update == f'Error: Param "{fake_wrong_id}" must be a integer'


def test_update_ParamIsNotStringError():
    # Fake payload
    fake_name = fake.word()
    # Inserting fake registry
    movie_repository.insert(name=fake_name)

    # Selecting fake registry
    query = movie_repository.select(name=fake_name)

    # Not string value
    not_string_value = fake.random_digit()

    # Trying update fake registry with not string value
    wrong_name = movie_repository.update(id=query[0].id, name=not_string_value)

    # Checking errors
    assert wrong_name == f'Error: Param "{not_string_value}" must be a string'

    # Cleaning DB
    movie_repository.delete(id=(query[0].id))
