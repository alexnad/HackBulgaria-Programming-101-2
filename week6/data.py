from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import relationship, Session


Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    projection_type = Column(String)
    date = Column(String)
    time = Column(String)
    movie = relationship("Movie", backref="projections")


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    row = Column(Integer)
    column = Column(Integer)
    projection = relationship("Projection", backref="reservations")


engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
