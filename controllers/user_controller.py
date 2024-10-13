from flask import jsonify, request
from models.user_model import User
from database.db import db

class UserController:

    # LIST
    @staticmethod
    def list_users():
        try:
            users = User.query.all()
            user_list = [{
                "id": user.id,
                "username": user.username,
                "email": user.email,  
                "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S"), 
            } for user in users]
            return jsonify(user_list), 200
        except Exception as e:
            return jsonify({"message": "Error fetching users", "error": str(e)}), 500

    # CREATE
    @staticmethod
    def add_user(data):
        if 'username' in data and 'password' in data and 'email' in data:
            try:
                user = User(username=data["username"], email=data["email"])
                user.set_password(data["password"])
                db.session.add(user)
                db.session.commit()
                return jsonify({"message": "User added successfully!", "user": {"username": user.username, "email": user.email}}), 201
            except Exception as e:
                return jsonify({"message": "Error adding user!", "error": str(e)}), 500
        return jsonify({"message": "Invalid user data!", "user": data}), 400

    # READ
    @staticmethod
    def get_user_details(user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }), 200
        return jsonify({"message": "User not found!"}), 404

    # UPDATE
    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found!"}), 404
        
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            user.set_password(data['password'])
        if 'email' in data:
            user.email = data['email']
        
        db.session.commit()
        return jsonify({"message": "User updated successfully!"}), 200

    # DELETE
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully!"}), 200
        return jsonify({"message": "User not found!"}), 404
