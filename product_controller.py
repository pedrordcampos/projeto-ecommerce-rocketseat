from flask import jsonify
from models import Product
from db import db

class ProductController:
    @staticmethod
    def add_product(data):
        if 'name' in data and 'price' in data:
            try:
                # Cria uma nova instância do produto
                product = Product(name=data["name"], price=float(data["price"]), description=data.get("description", ""))

                # Adiciona o produto à sessão do banco de dados
                db.session.add(product)
                db.session.commit()

                return jsonify({
                    "message": "Product added successfully!",
                    "product": {
                        "name": product.name,
                        "price": product.price,
                        "description": product.description
                    }
                }), 201
                
            except Exception as e:
                return jsonify({"message": "Error adding product!", "error": str(e)}), 500
        
        return jsonify({"message": "Invalid product data!", "product": data}), 400
    
    def remove_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully!"}), 200
        return jsonify({"message": "Product not found!"}), 404
       
