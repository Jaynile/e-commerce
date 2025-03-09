from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'
PRODUCTS_FILE = 'products.json'

def load_products():
    with open(PRODUCTS_FILE, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    products = load_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    products = load_products()
    product = products[product_id]
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    products = load_products()
    cart_items = [products[product_id] for product_id in session.get('cart', [])]
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
