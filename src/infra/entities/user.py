from sqlalchemy import Boolean, Column, Integer, String

from src.infra.configs.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f'User (id = {self.id}, email = {self.email}, name = {self.name}, is_active = {self.is_active})'
