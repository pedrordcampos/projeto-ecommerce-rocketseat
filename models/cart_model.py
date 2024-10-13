from database.db import db

class CartItem(db.Model):
    __tablename__ = 'cart_item'  #
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)  

    def __repr__(self):
        return f'<CartItem {self.id}, User {self.user_id}, Product {self.product_id}>'
