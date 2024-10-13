from flask import request
from flask_login import login_required
from controllers.product_controller import ProductController
from controllers.user_controller import UserController
from controllers.login_controller import LoginController

def init_routes(app):
    """ LOGIN """
    @app.route('/login', methods=["POST"])
    def login():
        return LoginController.login()
    
    """ LOGOUT """
    @app.route('/logout', methods=["POST"])
    @login_required 
    def logout():
        return LoginController.logout()

    """ USERS """
    @app.route('/api/users', methods=["GET"])
    def list_users():
        return UserController.list_users()

    @app.route('/api/users', methods=["POST"])
    @login_required 
    def add_user():
        data = request.json
        return UserController.add_user(data)

    @app.route('/api/users/<int:user_id>', methods=["GET"])
    def get_user_details(user_id):
        return UserController.get_user_details(user_id)

    @app.route('/api/users/update/<int:user_id>', methods=["PUT"])
    @login_required 
    def update_user(user_id):
        data = request.json
        return UserController.update_user(user_id, data)

    @app.route('/api/users/delete/<int:user_id>', methods=["DELETE"])
    @login_required 
    def delete_user(user_id):
        return UserController.delete_user(user_id)

    """ PRODUCTS """
    @app.route('/api/products', methods=["GET"])
    def list_products():
        return ProductController.list_products()

    @app.route('/api/products/add', methods=["POST"])
    @login_required 
    def add_product():
        data = request.json
        return ProductController.add_product(data)

    @app.route('/api/products/<int:product_id>', methods=["GET"])
    def get_product_details(product_id):
        return ProductController.product_details(product_id)

    @app.route('/api/products/update/<int:product_id>', methods=["PUT"])
    @login_required 
    def update_product(product_id):
        data = request.json
        return ProductController.update_product(product_id, data)

    @app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
    @login_required 
    def delete_product(product_id):
        return ProductController.delete_product(product_id)
