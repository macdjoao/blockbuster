from faker import Faker

from src.infra.repositories.customer import CustomerRepository

customer_repository = CustomerRepository()
fake = Faker()


def test_insert():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()

    # Inserting fake registry
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    # Selecting fake registry
    query = customer_repository.select(email=fake_email)

    # Checking equalities
    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name

    # Cleaning DB
    customer_repository.delete(id=(query[0].id))


def test_insert_EmailAlreadyRegisteredError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    # Second fake Payload
    second_fake_first_name = fake.first_name()
    second_fake_last_name = fake.last_name()
    # Trying insert second fake registry with same email of first fake registry
    fail_insert = customer_repository.insert(
        email=fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
    )

    # Checking error
    assert fail_insert == f'Error: Email "{fake_email}" is already registered'

    # Selecting fake registry for delete
    query = customer_repository.select(email=fake_email)
    # Cleaning DB
    customer_repository.delete(id=(query[0].id))


def test_insert_ParamIsNotStringError():
    # Fake valid values
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()

    # Setting a not string value
    fake_not_string = fake.random_digit()

    # Trying to insert by passing a not string value as email
    wrong_email_insert = customer_repository.insert(
        email=fake_not_string,
        first_name=fake_first_name,
        last_name=fake_last_name,
    )

    # Trying to insert by passing a not string value as first_name
    wrong_first_name_insert = customer_repository.insert(
        email=fake_email, first_name=fake_not_string, last_name=fake_last_name
    )

    # Trying to insert by passing a not string value as last_name
    wrong_last_name_insert = customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_not_string
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


def test_select():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    # Inserting fake
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    # Selecting fake registry
    query = customer_repository.select(
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
    customer_repository.delete(id=(query[0].id))


def test_select_ParamIsNotIntegerError():
    # Setting a not integer id
    fake_not_int_id = fake.word()
    # Trying to select a customer by passing a not integer as id
    query = customer_repository.select(id=fake_not_int_id)

    # Checking error
    assert query == f'Error: Param "{fake_not_int_id}" must be a integer'


def test_select_ParamIsNotStringError():
    # Setting a not string email
    fake_not_string_email = fake.random_digit()
    # Trying to select a customer by passing a not string as email
    wrong_email_query = customer_repository.select(email=fake_not_string_email)

    # Setting a not string first_name
    fake_not_string_first_name = fake.random_digit()
    # Trying to select a customer by passing a not string as first_name
    wrong_first_name_query = customer_repository.select(
        email=fake_not_string_first_name
    )

    # Setting a not string last_name
    fake_not_string_last_name = fake.random_digit()
    # Trying to select a customer by passing a not string as last_name
    wrong_last_name_query = customer_repository.select(
        email=fake_not_string_last_name
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


def test_select_ParamIsNotBoolError():
    # Setting a not boolean is_active
    fake_not_bool_is_active = fake.word()
    # Trying to select a customer by passing a not boolean as is_active
    query = customer_repository.select(is_active=fake_not_bool_is_active)

    # Checking errors
    assert query == f'Error: Param {fake_not_bool_is_active} must be a boolean'


def test_update():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    # Selecting fake registry
    query = customer_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Second fake payload
    new_fake_first_name = fake.first_name()
    new_fake_last_name = fake.last_name()
    # Update fake registry with second fake payload parameters
    customer_repository.update(
        id=query[0].id,
        first_name=new_fake_first_name,
        last_name=new_fake_last_name,
    )

    # Selecting updated fake registry
    updated_query = customer_repository.select(id=query[0].id)

    # Check equalities
    assert updated_query[0].first_name == new_fake_first_name
    assert updated_query[0].last_name == new_fake_last_name

    # Cleaning DB
    customer_repository.delete(id=(updated_query[0].id))


# TODO: update errors


def test_update_ParamIsNotIntegerError():
    # Fake wrong type id
    fake_wrong_id = fake.word()
    # Trying to update a registry by passing a not integer id
    update = customer_repository.update(id=fake_wrong_id)

    assert update == f'Error: Param "{fake_wrong_id}" must be a integer'


def test_update_IdNotFoundError():
    # Fake payload
    fake_id = 0
    fake_last_name = fake.last_name()
    # Trying to update a registry passing an id that does not exist
    update = customer_repository.update(id=fake_id, last_name=fake_last_name)

    assert update == f'Error: Id "{fake_id}" not found'


# TODO: remove and remove errors
