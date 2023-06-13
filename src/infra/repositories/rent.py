from datetime import datetime

from src.infra.configs.session import session
from src.infra.entities.rent import Rent as RentEntity


class Rent:
    def insert(
        self,
        id: str,
        user: str,
        customer: str,
        movie: str,
        devolution_date: datetime,
    ):
        # Trechos comentados devem ser implementados em services
        try:
            # data_insert = RentEntity(
            #     id=str(uuid.uuid1()),
            #     user=user.capitalize(),
            #     customer=customer.capitalize(),
            #     movie=movie.capitalize(),
            #     devolution_date=devolution_date
            # )
            data_insert = RentEntity(
                id=id,
                user=user,
                customer=customer,
                movie=movie,
                devolution_date=devolution_date,
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
        user: str = None,
        customer: str = None,
        movie: str = None,
        rent_date: datetime = None,
        devolution_date: datetime = None,
        finished: bool = None,
    ):
        try:
            custom_filter = session.query(RentEntity)
            if id is not None:
                custom_filter = custom_filter.filter(RentEntity.id == id)
            if user is not None:
                custom_filter = custom_filter.filter(RentEntity.user == user)
            if customer is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.customer == customer
                )
            if movie is not None:
                custom_filter = custom_filter.filter(RentEntity.movie == movie)
            if rent_date is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.rent_date == rent_date
                )
            if devolution_date is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.devolution_date == devolution_date
                )
            if finished is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.finished == finished
                )

            data_select = custom_filter.all()

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()
