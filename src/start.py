from flask import Flask
from sqlalchemy import create_engine 

# inicia o projeto flask
app = Flask(__name__)

# declara a conexao com o banco 
engine = create_engine('sqlite:///:memory:', echo=True)


# define a rota
@app.route('/')
# funçao que responde a rota
def home_handler():
    return 'Hello World'

# define a porta e inicializa a aplicação
app.run(port=5000)

