from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import models

# inicia o projeto flask
app = Flask(__name__)

# declara a conexao com o banco 
engine = create_engine('sqlite:///euquero.db', echo=True)

# executa todas as configurações no Base
models.Base.metadata.create_all(engine)
# SQLAlchemy precisa de uma sessão para funcionar. 
# Essa variável informa que a sessao corresponde a variável engine declarada anteriormente.
Session = sessionmaker(bind=engine)
session = Session()

session.add(models.User(email='a@a.a', name='ana', password='123', cpf='123'))
session.commit()

# define a rota
@app.route('/')
# funçao que responde a rota
def home_handler():
    print(session.query(models.User).all())
    return ''

# define a porta e inicializa a aplicação
app.run(port=5000)

