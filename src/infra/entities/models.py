from sqlalchemy import Boolean, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'players'

    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f'User (id = {self.id}, email = {self.email}, name = {self.name}, is_active = {self.is_active})'
