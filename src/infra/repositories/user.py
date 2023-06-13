import uuid

from passlib.context import CryptContext

from src.infra.configs.session import session
from src.infra.entities.user import User as UserEntity


class User:
    def select(
        self,
        id: str = None,
        email: str = None,
        name: str = None,
        is_active: bool = None,
    ):
        try:
            custom_filter = session.query(UserEntity)
            if id is not None:
                custom_filter = custom_filter.filter(UserEntity.id == id)
            if email is not None:
                custom_filter = custom_filter.filter(UserEntity.email == email)
            if name is not None:
                custom_filter = custom_filter.filter(UserEntity.name == name)
            if is_active is not None:
                custom_filter = custom_filter.filter(
                    UserEntity.is_active == is_active
                )

            data_select = custom_filter.all()

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()

    def insert(self, email: str, name: str, password: str):
        pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        try:
            data_insert = UserEntity(
                id=str(uuid.uuid1()),
                email=email.lower(),
                name=name.capitalize(),
                password=pwd_context.hash(password),
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except Exception as err:
            return err
        finally:
            session.close()
