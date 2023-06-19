from src.infra.configs.session import session
from src.infra.entities.customer import Customer as CustomerEntity
from src.infra.repositories.errors.general import (IdNotFoundError,
                                                   IncompleteParamsError,
                                                   ParamAreNotRecognizedError)
from src.infra.repositories.utils.general import (
    id_not_found, param_is_not_a_recognized_attribute, params_is_none)


class Customer:
    def insert(self, id: str, email: str, name: str):
        # Trechos comentados devem ser implementados em services
        try:
            # data_insert = CustomerEntity(
            #     id=str(uuid.uuid1()),
            #     email=email.lower(),
            #     name=name.capitalize(),
            # )
            data_insert = CustomerEntity(
                id=id,
                email=email,
                name=name,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except Exception as err:
            session.rollback()
            return err
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
            custom_filter = session.query(CustomerEntity)
            if id is not None:
                custom_filter = custom_filter.filter(CustomerEntity.id == id)
            if email is not None:
                custom_filter = custom_filter.filter(
                    CustomerEntity.email == email
                )
            if name is not None:
                custom_filter = custom_filter.filter(
                    CustomerEntity.name == name
                )
            if is_active is not None:
                custom_filter = custom_filter.filter(
                    CustomerEntity.is_active == is_active
                )

            data_select = custom_filter.all()

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()

    def update(self, id: str = None, **kwargs):

        customer_entity = CustomerEntity()
        try:
            if params_is_none(id):
                raise IncompleteParamsError
            if id_not_found(session=session, object=CustomerEntity, arg=id):
                raise IdNotFoundError(id=id)
            for kwarg in kwargs:
                if param_is_not_a_recognized_attribute(
                    object=customer_entity, arg=kwarg
                ):
                    raise ParamAreNotRecognizedError(error_param=kwarg)
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({f'{kwarg}': kwargs[f'{kwarg}']})
            data_update = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == id)
                .first()
            )
            return data_update

        except IncompleteParamsError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        except ParamAreNotRecognizedError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, id: str):
        try:

            data_delete = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == id)
                .first()
            )

            session.query(CustomerEntity).filter(
                CustomerEntity.id == id
            ).delete()
            session.commit()

            return data_delete

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()
