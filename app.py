from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import db
from flask_login import LoginManager
from models.user_model import User
from routes.route import init_routes

# Inicializa a aplicação Flask
app = Flask(__name__)

# Habilita CORS para a aplicação Flask
CORS(app)

# Carrega as configurações da aplicação
app.config.from_object(Config)

# Defina a secret_key
app.secret_key = 'minicursopython'  # Use algo único e secreto

# Inicializa o banco de dados com a aplicação
db.init_app(app)

# Inicializa o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Define a rota de login para redirecionar quando o usuário não estiver autenticado
login_manager.login_view = "login"

# Adiciona o user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Inicializa as rotas da aplicação
init_routes(app)

# Função principal para rodar a aplicação
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se ainda não existirem
    app.run(debug=True)
