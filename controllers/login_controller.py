from flask import jsonify, request
from flask_login import login_user, logout_user
from models.user_model import User

class LoginController:

    @staticmethod
    def login():
        data = request.json
        
        # Busca o usuário pelo nome de usuário
        user = User.query.filter_by(username=data.get('username')).first()
        
        if not user:
            return jsonify({"message": "Invalid username or password!"}), 401

        # Verifica a senha
        if not user.check_password(data.get('password')):
            return jsonify({"message": "Invalid username or password!"}), 401

        # Loga o usuário
        login_user(user)
        return jsonify({"message": "Logged in successfully!"}), 200

    @staticmethod
    def logout():
        logout_user()
        return jsonify({"message": "Loggout in successfully!"}), 200