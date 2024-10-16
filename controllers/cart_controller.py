from flask import jsonify, request
from flask_login import current_user
from models.product_model import Product
from models.cart_model import CartItem
from database.db import db

class CartController:
    @staticmethod
    def add_to_cart(product_id):
        # Pegando a quantidade da requisição JSON (com valor padrão de 1)
        data = request.get_json()
        quantity = data.get('quantity', 1)

        # Buscando o produto no banco de dados
        product = Product.query.get(product_id)
        
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Criar o item do carrinho e associar ao usuário logado (current_user)
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
        
        # Salvar no banco de dados
        db.session.add(cart_item)
        db.session.commit()

        return jsonify({"message": "Product added to cart successfully!"}), 200
    
    @staticmethod
    def remove_cart_item(item_id):
        # Busca o item no carrinho pelo item_id e garante que pertence ao usuário logado
        cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()

        # Se o item não for encontrado, retorna um erro 404
        if not cart_item:
            return jsonify({"message": "Item não encontrado no carrinho"}), 404

        # Tenta remover o item do banco de dados
        try:
            db.session.delete(cart_item)
            db.session.commit()
            return jsonify({"message": "Item removido do carrinho com sucesso"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Falha ao remover o item do carrinho", "error": str(e)}), 400

        
    @staticmethod
    def view_cart():
        # Obter todos os itens do carrinho do usuário atual
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        
        if not cart_items:
            return jsonify({"message": "Empty cart"}), 200
        
        # Montar a lista de produtos no carrinho
        cart_data = []
        for item in cart_items:
            product = Product.query.get(item.product_id)
            cart_data.append({
                "product_id": product.id,
                "product_name": product.name,
                "price": product.price,
                "quantity": item.quantity  # Se você tiver um campo de quantidade no carrinho
            })
        
        return jsonify({"cart": cart_data}), 200

    @staticmethod
    def checkout():
        # Obter todos os itens do carrinho do usuário atual
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        
        # Verificar se o carrinho está vazio
        if not cart_items:
            return jsonify({"message": "Carrinho vazio"}), 200
        
        # Remover cada item do carrinho
        for item in cart_items:
            db.session.delete(item)
        
        # Salvar mudanças no banco de dados
        db.session.commit()
        
        # Retornar mensagem de sucesso
        return jsonify({"message": "Checkout successfull. Cart has been cleared"})