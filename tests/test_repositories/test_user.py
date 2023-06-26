from faker import Faker

from src.infra.repositories.user import UserRepository

user_repository = UserRepository()
fake = Faker()


def test_insert():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(email=fake_email)

    # Checking equalities
    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_insert_EmailAlreadyRegisteredError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Second fake Payload
    second_fake_first_name = fake.first_name()
    second_fake_last_name = fake.last_name()

    # Trying insert second fake registry with same email of first fake registry
    fail_insert = user_repository.insert(
        email=fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
        password=fake_password,
    )

    # Checking error
    assert fail_insert == f'Error: Email "{fake_email}" is already registered'

    # Selecting fake registry for delete
    query = user_repository.select(email=fake_email)

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_insert_ParamIsNotStringError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Setting a not string value
    fake_not_string = fake.random_digit()

    # Trying to insert by passing a not string value as email
    wrong_email_insert = user_repository.insert(
        email=fake_not_string,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as first_name
    wrong_first_name_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_not_string,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as last_name
    wrong_last_name_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_not_string,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as password
    wrong_password_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_not_string,
    )

    # Checking errors
    assert (
        wrong_email_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_first_name_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_last_name_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_password_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )


def test_select():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Checking equalities
    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name
    assert query[0].is_active == True

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_select_ParamIsNotIntegerError():
    # Setting a not integer id
    fake_not_int_id = fake.word()

    # Trying to select a customer by passing a not integer as id
    query = user_repository.select(id=fake_not_int_id)

    # Checking error
    assert query == f'Error: Param "{fake_not_int_id}" must be a integer'


def test_select_ParamIsNotStringError():
    # Setting a not string email
    fake_not_string_email = fake.random_digit()
    # Trying to select a customer by passing a not string as email
    wrong_email_query = user_repository.select(email=fake_not_string_email)

    # Setting a not string first_name
    fake_not_string_first_name = fake.random_digit()
    # Trying to select a customer by passing a not string as first_name
    wrong_first_name_query = user_repository.select(
        first_name=fake_not_string_first_name
    )

    # Setting a not string last_name
    fake_not_string_last_name = fake.random_digit()
    # Trying to select a customer by passing a not string as last_name
    wrong_last_name_query = user_repository.select(
        last_name=fake_not_string_last_name
    )

    # Checking errors
    assert (
        wrong_email_query
        == f'Error: Param "{fake_not_string_email}" must be a string'
    )
    assert (
        wrong_first_name_query
        == f'Error: Param "{fake_not_string_first_name}" must be a string'
    )
    assert (
        wrong_last_name_query
        == f'Error: Param "{fake_not_string_last_name}" must be a string'
    )
