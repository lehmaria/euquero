from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# base é tipo uma planilha vazia no Excel. Essa função declara essa "planilha vazia"
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    cpf = Column(String)

    def __repr__(self):
        return f'User {self.id}, name:{self.name}, email:{self.email}, cpf:{self.cpf}'

