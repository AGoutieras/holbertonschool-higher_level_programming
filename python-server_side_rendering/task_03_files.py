from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():

    with open('items.json', 'r') as f:
        data = json.load(f)

    return render_template('items.html', items=data["items"])


@app.route('/products')
def products_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        with open('products.json', 'r') as f:
            products = json.load(f)

    elif source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)

    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        found = None
        for product in products:
            if product["id"] == int(product_id):
                found = product
        if found is None:
            return render_template('product_display.html', error="Product not found")
        else:
            return render_template('product_display.html', products=[found])

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
