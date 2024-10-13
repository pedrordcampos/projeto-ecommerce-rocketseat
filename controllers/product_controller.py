from flask import jsonify, request
from models.product_model import Product
from database.db import db

class ProductController:

    # LIST
    @staticmethod
    def list_products():
        try:
            # Recupera todos os produtos do banco de dados
            products = Product.query.all()

            # Converte cada produto em um dicionário para retornar em JSON
            product_list = [{
                "id": product.id,
                "name": product.name,
                "price": product.price,
            } for product in products]

            # Retorna a lista de produtos em formato JSON
            return jsonify(product_list), 200

        except Exception as e:
            return jsonify({"message": "Error fetching products", "error": str(e)}), 500

    # CREATE
    @staticmethod
    def add_product(data):
        if 'name' in data and 'price' in data:
            try:
                product = Product(name=data["name"], price=float(data["price"]), description=data.get("description", ""))
                db.session.add(product)
                db.session.commit()
                return jsonify({"message": "Product added successfully!", "product": {"name": product.name, "price": product.price, "description": product.description}}), 201
            except Exception as e:
                return jsonify({"message": "Error adding product!", "error": str(e)}), 500
        return jsonify({"message": "Invalid product data!", "product": data}), 400
    
    # READ
    @staticmethod
    def product_details(product_id):
        product = Product.query.get(product_id)
        if product:
            return jsonify({"id": product.id, "name": product.name, "price": product.price, "description": product.description}), 200
        return jsonify({"message": "Product not found!"}), 404

    # UPDATE
    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"message": "Product not found!"}), 404
        
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            product.price = data['price']
        if 'description' in data:
            product.description = data['description']
        
        # Persistir as mudanças
        db.session.commit()
        return jsonify({"message": "Product updated successfully!"}), 200

    # DELETE
    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully!"}), 200
        return jsonify({"message": "Product not found!"}), 404
