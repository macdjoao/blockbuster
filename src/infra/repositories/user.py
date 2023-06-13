# import uuid

# from passlib.context import CryptContext

from src.infra.configs.session import session
from src.infra.entities.user import User as UserEntity
from src.infra.repositories.errors.general import (IncompleteParamsError,
                                                   ParamIsNotStringError)
from src.infra.repositories.utils.general import (param_is_not_a_string,
                                                  params_is_none)


class User:
    def insert(
        self,
        id: str = None,
        email: str = None,
        name: str = None,
        password: str = None,
    ):
        # Trechos comentados devem ser implementados em services
        # pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        try:
            # data_insert = UserEntity(
            #     id=str(uuid.uuid1()),
            #     email=email.lower(),
            #     name=name.capitalize(),
            #     password=pwd_context.hash(password),
            # )
            if params_is_none(id, email, name, password):
                raise IncompleteParamsError
            if param_is_not_a_string(id, email, name, password):
                raise ParamIsNotStringError

            data_insert = UserEntity(
                id=id,
                email=email,
                name=name,
                password=password,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except IncompleteParamsError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

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

    def update(
        self,
        id: str,
        email: str = None,
        name: str = None,
        password: str = None,
        is_active: bool = None,
    ):
        try:
            if email is not None:
                # user.update({'email': email.lower()})
                session.query(UserEntity).filter(UserEntity.id == id).update(
                    {'email': email}
                )
            if name is not None:
                # user.update({'name': name.capitalize()})
                session.query(UserEntity).filter(UserEntity.id == id).update(
                    {'name': name}
                )
            if password is not None:
                # user.update({'password': pwd_context.hash(password)})
                session.query(UserEntity).filter(UserEntity.id == id).update(
                    {'password': password}
                )
            if is_active is not None:
                session.query(UserEntity).filter(UserEntity.id == id).update(
                    {'is_active': is_active}
                )
            session.commit()

            data_update = (
                session.query(UserEntity).filter(UserEntity.id == id).first()
            )

            return data_update

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()

    def delete(self, id: str):
        try:

            data_delete = (
                session.query(UserEntity).filter(UserEntity.id == id).first()
            )

            session.query(UserEntity).filter(UserEntity.id == id).delete()
            session.commit()

            return data_delete

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()
