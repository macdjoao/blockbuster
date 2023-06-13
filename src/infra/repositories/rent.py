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
