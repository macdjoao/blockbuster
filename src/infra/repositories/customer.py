from src.infra.configs.session import session
from src.infra.entities.customer import Customer as CustomerEntity


class Customer:
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

    def update(
        self,
        id: str,
        email: str = None,
        name: str = None,
        is_active: bool = None,
    ):
        try:
            if email is not None:
                # user.update({'email': email.lower()})
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'email': email})
            if name is not None:
                # user.update({'name': name.capitalize()})
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'name': name})
            if is_active is not None:
                session.query(CustomerEntity).filter(
                    CustomerEntity.id == id
                ).update({'is_active': is_active})
            session.commit()

            data_update = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == id)
                .first()
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
