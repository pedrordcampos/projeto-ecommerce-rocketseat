from flask import Flask
from config import Config
from db import db
from route import init_routes
from models import Product 

# Inicializa a aplicação
app = Flask(__name__)

# Carrega as configurações
app.config.from_object(Config)

# Inicializa o banco de dados com a aplicação
db.init_app(app)

# Inicializa as rotas
init_routes(app)

if __name__ == "__main__":
    with app.app_context():
        # Cria as tabelas no banco de dados, se não existirem
        db.create_all()

    app.run(debug=True)