from flask import Flask
app = Flask(__name__)


# define a rota
@app.route('/')
# funçao que responde a rota
def home_handler():
    return 'Hello World'

# define a porta e inicializa a aplicação
app.run(port=5000)

