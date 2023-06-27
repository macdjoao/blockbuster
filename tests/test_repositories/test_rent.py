import datetime

from faker import Faker

from src.infra.repositories.customer import CustomerRepository
from src.infra.repositories.movie import MovieRepository
from src.infra.repositories.rent import RentRepository
from src.infra.repositories.user import UserRepository

rent_repository = RentRepository()
user_repository = UserRepository()
customer_repository = CustomerRepository()
movie_repository = MovieRepository()
fake = Faker()


def test_insert():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Checking equalities
    assert rent_query[0].user_id == user_query[0].id
    assert rent_query[0].customer_id == customer_query[0].id
    assert rent_query[0].movie_id == movie_query[0].id
    assert (
        str(rent_query[0].devolution_date) == f'{fake_devolution_date}+00:00'
    )

    # Cleaning DB
    rent_repository.delete(id=rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_insert_ParamIsNotIntegerError():
    # Setting a valid inputs values
    fake_user_id = fake.random_digit()
    fake_customer_id = fake.random_digit()
    fake_movie_id = fake.random_digit()
    fake_devolution_date = datetime.datetime(2025, 1, 15)

    # Setting a not integer id
    fake_not_int = fake.word()

    # Trying to insert a rent by passing a not integer as id
    wrong_user_id = rent_repository.insert(
        user_id=fake_not_int,
        customer_id=fake_customer_id,
        movie_id=fake_movie_id,
        devolution_date=fake_devolution_date,
    )
    wrong_customer_id = rent_repository.insert(
        user_id=fake_user_id,
        customer_id=fake_not_int,
        movie_id=fake_movie_id,
        devolution_date=fake_devolution_date,
    )
    wrong_movie_id = rent_repository.insert(
        user_id=fake_user_id,
        customer_id=fake_not_int,
        movie_id=fake_not_int,
        devolution_date=fake_devolution_date,
    )

    # Checking error
    assert wrong_user_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert (
        wrong_customer_id == f'Error: Param "{fake_not_int}" must be a integer'
    )
    assert wrong_movie_id == f'Error: Param "{fake_not_int}" must be a integer'


def test_insert_ParamIsNotDateError():
    # Setting a valid inputs values
    fake_user_id = fake.random_digit()
    fake_customer_id = fake.random_digit()
    fake_movie_id = fake.random_digit()

    # Setting a not date devolution date
    fake_devolution_date = fake.word()

    # Trying to insert a rent by passing a not date as devolution date
    wrong_date = rent_repository.insert(
        user_id=fake_user_id,
        customer_id=fake_customer_id,
        movie_id=fake_movie_id,
        devolution_date=fake_devolution_date,
    )

    # Checking error
    assert (
        wrong_date == f'Error: Param "{fake_devolution_date}" must be a date'
    )


def test_insert_IdNotFoundError():
    # Setting a valid inputs values
    fake_user_id = 0
    fake_customer_id = 0
    fake_movie_id = 0
    fake_devolution_date = datetime.datetime(2025, 1, 15)

    # Trying to insert a rent by passing a inexistent user_id
    wrong_user_id = rent_repository.insert(
        user_id=fake_user_id,
        customer_id=fake_customer_id,
        movie_id=fake_movie_id,
        devolution_date=fake_devolution_date,
    )

    # Checking error
    assert wrong_user_id == f'Error: Id "{fake_user_id}" not found'


def test_select():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Checking select query
    assert rent_query[0].user_id == user_query[0].id
    assert rent_query[0].customer_id == customer_query[0].id
    assert rent_query[0].movie_id == movie_query[0].id
    assert (
        str(rent_query[0].devolution_date) == f'{fake_devolution_date}+00:00'
    )
    assert rent_query[0].finished == False

    # Cleaning DB
    rent_repository.delete(id=rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_select_ParamIsNotIntegerError():
    # Setting a not integer value
    fake_not_int = fake.word()
    # Trying to select fake rent registry by passing a not integer values
    wrong_id = rent_repository.select(id=fake_not_int)
    wrong_user_id = rent_repository.select(user_id=fake_not_int)
    wrong_customer_id = rent_repository.select(customer_id=fake_not_int)
    wrong_movie_id = rent_repository.select(movie_id=fake_not_int)

    # Checking errors
    assert wrong_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert wrong_user_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert (
        wrong_customer_id == f'Error: Param "{fake_not_int}" must be a integer'
    )
    assert wrong_movie_id == f'Error: Param "{fake_not_int}" must be a integer'


def test_select_ParamIsNotDateError():
    # Setting a not date value
    fake_not_date = fake.random_digit()
    # Trying to select fake rent registry by passing a not date values
    wrong_rent_date = rent_repository.select(rent_date=fake_not_date)
    wrong_devolution_date = rent_repository.select(
        devolution_date=fake_not_date
    )

    # Checking errors
    assert wrong_rent_date == f'Error: Param "{fake_not_date}" must be a date'
    assert (
        wrong_devolution_date
        == f'Error: Param "{fake_not_date}" must be a date'
    )


def test_select_ParamIsNotBoolError():
    # Setting a not boolean value
    fake_not_bool = fake.word()
    # Trying to select fake rent registry by passing a not bool value
    wrong_finished = rent_repository.select(finished=fake_not_bool)

    # Checking error
    assert (
        wrong_finished == f'Error: Param "{fake_not_bool}" must be a boolean'
    )


def test_update():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Second fake payload to movie
    second_movie_fake_name = fake.word()
    # Inserting second fake movie registry
    movie_repository.insert(name=second_movie_fake_name)
    # Selecting second fake movie registry
    second_movie_query = movie_repository.select(
        name=second_movie_fake_name, available=True
    )

    # Update rent with second_movie_fake
    rent_repository.update(
        id=rent_query[0].id, movie_id=second_movie_query[0].id
    )
    # Updated query
    updated_rent_query = rent_repository.select(id=rent_query[0].id)

    # Checking equalities
    assert updated_rent_query[0].movie_id == second_movie_query[0].id

    # Cleaning DB
    rent_repository.delete(id=updated_rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    movie_repository.delete(id=second_movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_update_ParamIsNotIntegerError():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Setting a not integer value
    fake_not_int = fake.word()
    # Trying update rent with not integer values
    wrong_id = rent_repository.update(id=fake_not_int)
    wrong_user_id = rent_repository.update(
        id=rent_query[0].id, user_id=fake_not_int
    )
    wrong_movie_id = rent_repository.update(
        id=rent_query[0].id, movie_id=fake_not_int
    )
    wrong_customer_id = rent_repository.update(
        id=rent_query[0].id, customer_id=fake_not_int
    )

    # Checking errors
    assert wrong_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert wrong_user_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert wrong_movie_id == f'Error: Param "{fake_not_int}" must be a integer'
    assert (
        wrong_customer_id == f'Error: Param "{fake_not_int}" must be a integer'
    )

    # Cleaning DB
    rent_repository.delete(id=rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_update_ParamIsNotDateError():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Setting a not date value
    fake_not_date = fake.random_digit()
    # Trying update rent with not date values
    wrong_rent_date = rent_repository.update(
        id=rent_query[0].id, rent_date=fake_not_date
    )
    wrong_devolution_date = rent_repository.update(
        id=rent_query[0].id, devolution_date=fake_not_date
    )

    # Checking errors
    assert wrong_rent_date == f'Error: Param "{fake_not_date}" must be a date'
    assert (
        wrong_devolution_date
        == f'Error: Param "{fake_not_date}" must be a date'
    )

    # Cleaning DB
    rent_repository.delete(id=rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_update_ParamIsNotBoolError():
    # Fake payload to user
    user_fake_email = fake.email()
    user_fake_first_name = fake.first_name()
    user_fake_last_name = fake.last_name()
    user_fake_password = fake.word()
    # Inserting fake user registry
    user_repository.insert(
        email=user_fake_email,
        first_name=user_fake_first_name,
        last_name=user_fake_last_name,
        password=user_fake_password,
    )
    # Selecting fake user registry
    user_query = user_repository.select(email=user_fake_email)

    # Fake payload to customer
    customer_fake_email = fake.email()
    customer_fake_first_name = fake.first_name()
    customer_fake_last_name = fake.last_name()
    # Inserting fake registry
    customer_repository.insert(
        email=customer_fake_email,
        first_name=customer_fake_first_name,
        last_name=customer_fake_last_name,
    )
    # Selecting fake customer registry
    customer_query = customer_repository.select(email=customer_fake_email)

    # Fake payload to movie
    movie_fake_name = fake.word()
    # Inserting fake movie registry
    movie_repository.insert(name=movie_fake_name)
    # Selecting fake movie registry
    movie_query = movie_repository.select(name=movie_fake_name, available=True)

    # Fake payload to rent
    fake_devolution_date = datetime.datetime(2025, 1, 15)
    # Inserting fake rent registry
    rent_repository.insert(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=customer_query[0].id,
        movie_id=movie_query[0].id,
        devolution_date=fake_devolution_date,
    )

    # Setting a not boolean value
    fake_not_bool = fake.word()
    # Trying update rent with not boolean value
    wrong_finished = rent_repository.update(
        id=rent_query[0].id, finished=fake_not_bool
    )

    # Checking errors
    assert (
        wrong_finished == f'Error: Param "{fake_not_bool}" must be a boolean'
    )

    # Cleaning DB
    rent_repository.delete(id=rent_query[0].id)
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)


def test_delete_ParamIsNotIntegerError():
    # Setting a not integer value
    fake_not_int = fake.word()
    # Trying to delete fake rent registry by passing a not integer values
    wrong_id = rent_repository.delete(id=fake_not_int)

    # Checking error
    assert wrong_id == f'Error: Param "{fake_not_int}" must be a integer'


def test_delete_IdNotFoundError():
    # Setting a not existent id
    fake_not_existent_id = 0
    # Trying to delete fake rent registry by passing a not existent id
    not_existent_id = rent_repository.delete(id=fake_not_existent_id)

    # Checking error
    assert not_existent_id == f'Error: Id "{fake_not_existent_id}" not found'
