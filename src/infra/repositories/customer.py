from src.infra.configs.session import session
from src.infra.entities.customer import Customer as CustomerEntity
from src.infra.repositories.errors.general import (EmailAlreadyRegisteredError,
                                                   IdNotFoundError,
                                                   IncompleteParamError,
                                                   ParamIsNotBoolError,
                                                   ParamIsNotIntegerError,
                                                   ParamIsNotStringError)
from src.infra.repositories.utils.general import (email_already_registered,
                                                  id_not_found, param_is_none,
                                                  param_is_not_a_bool,
                                                  param_is_not_a_int,
                                                  param_is_not_a_string)

customer_entity = CustomerEntity()


class CustomerRepository:
    def insert(self, email: str, first_name: str, last_name: str):
        try:
            data_email = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.email == email)
                .first()
            )
            if data_email is not None:
                raise EmailAlreadyRegisteredError(email=email)
            data_insert = CustomerEntity(
                email=email.lower(),
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
            )
            session.add(data_insert)
            session.commit()

            return data_insert

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
            custom_filter = session.query(CustomerEntity)
            if id is not None:
                if param_is_not_a_int(id):
                    raise ParamIsNotIntegerError(arg=id)
                custom_filter = custom_filter.filter(CustomerEntity.id == id)
            if email is not None:
                if param_is_not_a_string(email):
                    raise ParamIsNotStringError(arg=email)
                custom_filter = custom_filter.filter(
                    CustomerEntity.email == email
                )
            if first_name is not None:
                if param_is_not_a_string(first_name):
                    raise ParamIsNotStringError(arg=first_name)
                custom_filter = custom_filter.filter(
                    CustomerEntity.first_name == first_name
                )
            if last_name is not None:
                if param_is_not_a_string(last_name):
                    raise ParamIsNotStringError(arg=last_name)
                custom_filter = custom_filter.filter(
                    CustomerEntity.last_name == last_name
                )
            if is_active is not None:
                if param_is_not_a_bool(is_active):
                    raise ParamIsNotBoolError(error_param=is_active)
                custom_filter = custom_filter.filter(
                    CustomerEntity.is_active == is_active
                )

            data_select = custom_filter.all()

            return data_select

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except ParamIsNotBoolError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def update(
        self,
        id: int = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        is_active: bool = None,
    ):

        try:
            if param_is_none(id):
                raise IncompleteParamError(arg=id)
            if param_is_not_a_int(id):
                raise ParamIsNotIntegerError(arg=id)
            if id_not_found(session=session, object=customer_entity, arg=id):
                raise IdNotFoundError(id=id)
            if email is not None:
                if param_is_not_a_string(email):
                    raise ParamIsNotStringError(arg=email)
                if email_already_registered(
                    session=session, object=customer_entity, email=email
                ):
                    raise EmailAlreadyRegisteredError(email=email)
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'email': email})
            if first_name is not None:
                if param_is_not_a_string(first_name):
                    raise ParamIsNotStringError(arg=first_name)
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'first_name': first_name})
            if last_name is not None:
                if param_is_not_a_string(last_name):
                    raise ParamIsNotStringError(arg=last_name)
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'last_name': last_name})
            if is_active is not None:
                if param_is_not_a_bool(is_active):
                    raise ParamIsNotBoolError(arg=is_active)
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'is_active': is_active})

            data_update = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == id)
                .first()
            )
            return data_update

        except IncompleteParamError as err:
            session.rollback()
            return err.message
        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except EmailAlreadyRegisteredError as err:
            session.rollback()
            return err.message
        except ParamIsNotBoolError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, id: int):
        try:
            if param_is_none(id):
                raise IncompleteParamError(arg=id)
            if param_is_not_a_int(id):
                raise ParamIsNotIntegerError(arg=id)
            data_id = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == id)
                .first()
            )
            if data_id is not None:
                raise IdNotFoundError(id=id)

            session.query(CustomerEntity).filter(
                CustomerEntity.id == id
            ).delete()
            session.commit()

            return data_id

        except IncompleteParamError as err:
            session.rollback()
            return err.message
        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
