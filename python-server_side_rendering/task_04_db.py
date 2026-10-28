#!/usr/bin/python3
"""Flask app displaying products from JSON, CSV or a SQLite database."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items.json and render the list of items."""
    try:
        with open('items.json', 'r') as f:
            items_list = json.load(f).get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


def read_json(filename='products.json'):
    """Return the list of products stored in a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)


def read_csv(filename='products.csv'):
    """Return the list of products stored in a CSV file."""
    products = []
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename='products.db'):
    """Return the list of products stored in the SQLite database."""
    conn = sqlite3.connect(filename)
    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from ?source=json|csv|sql, optionally by ?id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Choix de la source
    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html',
                                   error='Wrong source')
    except sqlite3.Error:
        return render_template('product_display.html',
                               error='Database error')
    except (OSError, ValueError, KeyError):
        return render_template('product_display.html',
                               error='Error reading data')

    # 2. Filtre optionnel par id
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Product not found')
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    # 3. Affichage
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)