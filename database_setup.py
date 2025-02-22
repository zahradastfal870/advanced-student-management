from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Initialize ORM base
Base = declarative_base()

# Define User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Define Student table
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)
    phone = Column(String, nullable=False)

# Define Score table
class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    cs1030 = Column(Integer, default=0)
    cs1100 = Column(Integer, default=0)
    cs2030 = Column(Integer, default=0)

# Create SQLite database
engine = create_engine('sqlite:///sms.db')  # Creates 'sms.db' file in the same directory
Base.metadata.create_all(engine)  # Creates the tables
Session = sessionmaker(bind=engine)
session = Session()
