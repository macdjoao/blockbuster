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
        customer_id=int(customer_query[0].id),
        movie_id=int(movie_query[0].id),
        devolution_date=fake_devolution_date,
    )
    # Selecting fake rent registry
    rent_query = rent_repository.select(
        user_id=user_query[0].id,
        customer_id=int(customer_query[0].id),
        movie_id=int(movie_query[0].id),
        devolution_date=fake_devolution_date,
    )

    print(f'query[0]: {rent_query[0].devolution_date}')
    print(f'novo: {fake_devolution_date}')

    # Checking equalities
    assert rent_query[0].user_id == user_query[0].id
    assert rent_query[0].customer_id == customer_query[0].id
    assert rent_query[0].movie_id == movie_query[0].id
    assert (
        str(rent_query[0].devolution_date) == f'{fake_devolution_date}+00:00'
    )

    # Cleaning DB
    rent_repository.delete(id=(rent_query[0].id))
    movie_repository.delete(id=movie_query[0].id)
    user_repository.delete(id=user_query[0].id)
    customer_repository.delete(id=customer_query[0].id)
