from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_film_association = Table(
    'user_film_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('film_id', Integer, ForeignKey('films.id'))
)

user_company_association = Table(
    'user_company_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('company_id', Integer, ForeignKey('companies.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    minimum_fee = Column(Integer)

    films = relationship('Film', secondary=user_film_association, backref='users')
    companies = relationship('Company', secondary=user_company_association, backref='users')

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    budget = Column(Integer)
    release_year = Column(Integer)
    genres = Column(String)

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='films')

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email_address = Column(String)
    phone_number = Column(String)

    films = relationship('Film', back_populates='company')
