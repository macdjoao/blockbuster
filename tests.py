import datetime
import uuid

from faker import Faker

from src.infra.configs.session import session
from src.infra.repositories.customer import Customer as CustomerRepository
from src.infra.repositories.movie import Movie as MovieRepository
from src.infra.repositories.rent import Rent as RentRepository
from src.infra.repositories.user import User as UserRepository

fake = Faker()

# USER

# repository = UserRepository()

# for _ in range(20):
#     id = str(uuid.uuid1())
#     email = fake.email()
#     name = fake.first_name()
#     password = fake.word()
#     data_insert = user.insert(id=id, email=email, name=name, password=password)

# id = str(uuid.uuid1())
# email = fake.email()
# name = fake.first_name()
# password = fake.word()
# print(repository.insert(id=id, email=email, name=name, password=password))
# print(repository.select(id='', email='', name='', is_active=True))
# print(repository.update(id='', email='', name='', password='', is_active=False))
# print(repository.delete(id=''))

# CUSTOMER

# customer = CustomerRepository()

# for _ in range(20):
#     id = str(uuid.uuid1())
#     email = fake.email()
#     name = fake.first_name()

#     data_insert = customer.insert(id=id, name=name, email=email)

# id = str(uuid.uuid1())
# email = fake.email()
# name = fake.first_name()
# customer.insert(id=id, email=email, name=name)
# print(customer.select(id='', email='', name='', is_active=True))
# customer.update(id='', email='', name='', is_active=False)
# print(customer.delete(id=''))

# MOVIE

# movie = MovieRepository()

# for _ in range(20):
#     id = str(uuid.uuid1())
#     name = fake.word()

#     data_insert = movie.insert(id=id, name=name)

# id = str(uuid.uuid1())
# name = fake.word()
# movie.insert(id=id, name=name)
# print(movie.select(id='', name='', available=True))
# movie.update(id='', name='', available=False)
# print(movie.delete(id=''))

# RENT

rent = RentRepository()

# for _ in range(3):
#     id = str(uuid.uuid1())
#     user = '769efeec-096a-11ee-8650-00155db01706'
#     customer = '4b5a3fe2-0a20-11ee-8a48-00155db012cc'
#     movie = '520d6a70-0a21-11ee-91f3-00155db012cc'
#     devolution_date = datetime.datetime(2023, 8, 8)

#     data_insert = rent.insert(
#         id=id, user=user, customer=customer, movie=movie, devolution_date=devolution_date)

# id = str(uuid.uuid1())
# user = '8883dc50-0969-11ee-b7ae-00155db01706'
# customer = '4b59be78-0a20-11ee-8a48-00155db012cc'
# movie = '520fdc6a-0a21-11ee-91f3-00155db012cc'
# devolution_date = datetime.datetime(2023, 7, 11)
# rent.insert(id=id, user=user, customer=customer,
#             movie=movie, devolution_date=devolution_date)
# print(rent.select())
print(
    rent.update(
        id='d521efd4-0a22-11ee-b5a3-00155db012cc',
        devolution_date=datetime.datetime(2023, 7, 20),
    )
)
# print(rent.delete(id=''))
