from sqlalchemy import Boolean, Column, Integer, String

from src.infra.configs.base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'Customer (id = {self.id}, email = {self.email}, first_name = {self.first_name}, last_name = {self.last_name}, is_active = {self.is_active})'
