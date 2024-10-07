from flask import request
from product_controller import ProductController 

def init_routes(app):
    
    @app.route('/')
    def helloworld():
        return 'Hello World!'
    
    @app.route('/api/products/add', methods=["POST"])
    def add_product():
        data = request.json
              
        # Chama o método do controlador para adicionar o produto
        return ProductController.add_product(data)
    
    @app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
    def delete_product(product_id):
        # Chama o método do controlador para adicionar o produto
        return ProductController.remove_product(product_id)
        