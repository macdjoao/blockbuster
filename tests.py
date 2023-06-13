import uuid

from faker import Faker

from src.infra.configs.session import session
# from src.infra.entities.models import User as UserEntity
from src.infra.repositories.user import User as UserRepository

fake = Faker()

# for _ in range(20):
#     id = str(uuid.uuid1())
#     email = fake.email()
#     name = fake.first_name()
#     is_active = False
#     password = fake.word()

#     data_insert = UserEntity(
#         id=id, email=email, name=name, is_active=is_active, password=password)
#     session.add(data_insert)
#     session.commit()

repository = UserRepository()
# print(repository.select(is_active=False))

id = str(uuid.uuid1())
email = fake.email()
name = fake.first_name()
password = fake.word()
# repository.insert(id=id, email=email, name=name, password=password)
print(
    repository.update(
        id='2ddb8d6e-0a10-11ee-9cad-00155db012cc', email='gilberto@mail'
    )
)
