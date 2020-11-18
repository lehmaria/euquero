from flask import Flask, Response, jsonify, json
from flask_restful import Resource, Api, fields, marshal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import models

# inicia o projeto flask
app = Flask(__name__)
api = Api(app)

# declara a conexao com o banco 
engine = create_engine('sqlite:///euquero.db', echo=True)

# executa todas as configurações no Base
models.Base.metadata.create_all(engine)
# SQLAlchemy precisa de uma sessão para funcionar. 
# Essa variável informa que a sessao corresponde a variável engine declarada anteriormente.
Session = sessionmaker(bind=engine)
session = Session()

usuario = models.User(email='a@a.a', name='ana', password='123', cpf='123')

session.add(usuario)
session.commit()

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'cpf': fields.String,
}

# classe que define recurso a ser adicionado
class HelloWorld(Resource):
    def get(self):
        inicio = session.query(models.User).all()
        all_users = [marshal(user, resource_fields) for user in inicio]
        return {'data': all_users}

# define a rota
api.add_resource(HelloWorld, '/')

# define a porta e inicializa a aplicação
app.run(port=5000)

