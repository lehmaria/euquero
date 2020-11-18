from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json

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
        user = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'cpf': self.cpf,
        }
        return json.dumps({'user':user})
        

