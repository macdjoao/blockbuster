from src.infra.configs.session import session
from src.infra.entities.user import User as UserEntity
from src.infra.repositories.errors.general import (EmailAlreadyRegisteredError,
                                                   IdNotFoundError,
                                                   ParamIsNotBoolError,
                                                   ParamIsNotIntegerError,
                                                   ParamIsNotStringError)


class UserRepository:
    def insert(
        self, email: str, first_name: str, last_name: str, password: str
    ):
        try:
            if type(email) is not str:
                raise ParamIsNotStringError(arg=email)
            if type(first_name) is not str:
                raise ParamIsNotStringError(arg=first_name)
            if type(last_name) is not str:
                raise ParamIsNotStringError(arg=last_name)
            if type(password) is not str:
                raise ParamIsNotStringError(arg=password)

            data_email = (
                session.query(UserEntity)
                .filter(UserEntity.email == email)
                .first()
            )
            if data_email is not None:
                raise EmailAlreadyRegisteredError(email=email)

            data_insert = UserEntity(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except EmailAlreadyRegisteredError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def select(
        self,
        id: int = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        is_active: bool = None,
    ):
        try:
            custom_filter = session.query(UserEntity)

            if id is not None:
                if type(id) is not int:
                    raise ParamIsNotIntegerError(arg=id)
                custom_filter = custom_filter.filter(UserEntity.id == id)

            if email is not None:
                if type(email) is not str:
                    raise ParamIsNotStringError(arg=email)
                custom_filter = custom_filter.filter(UserEntity.email == email)

            if first_name is not None:
                if type(first_name) is not str:
                    raise ParamIsNotStringError(arg=first_name)
                custom_filter = custom_filter.filter(
                    UserEntity.first_name == first_name
                )

            if last_name is not None:
                if type(last_name) is not str:
                    raise ParamIsNotStringError(arg=last_name)
                custom_filter = custom_filter.filter(
                    UserEntity.last_name == last_name
                )

            if is_active is not None:
                if type(is_active) is not bool:
                    raise ParamIsNotBoolError(arg=is_active)
                custom_filter = custom_filter.filter(
                    UserEntity.is_active == is_active
                )

            data_select = custom_filter.all()

            return data_select

        except ParamIsNotIntegerError as err:
            return err.message
        except ParamIsNotStringError as err:
            return err.message
        except ParamIsNotBoolError as err:
            return err.message
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
