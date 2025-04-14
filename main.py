# app/main.py
from flask import Flask, render_template, jsonify, request
from modules.db import init_db, get_all_units, add_unit, update_unit, delete_unit
from modules.accounting import calculate_total
import os

app = Flask(__name__)

# Initialize the database when the application starts
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/units', methods=['GET', 'POST', 'PUT', 'DELETE'])
def units():
    if request.method == 'GET':
        units_data = get_all_units()
        return jsonify(units_data)
    elif request.method == 'POST':
        data = request.json
        add_unit(data)
        return jsonify({'status': 'Unit added'})
    elif request.method == 'PUT':
        data = request.json
        update_unit(data)
        return jsonify({'status': 'Unit updated'})
    elif request.method == 'DELETE':
        unit_id = request.args.get('id')
        delete_unit(unit_id)
        return jsonify({'status': 'Unit deleted'})

@app.route('/api/calculate_total', methods=['POST'])
def calc_total():
    data = request.json
    prices = data.get('prices', [])
    total = calculate_total(prices)
    return jsonify({'total': total})

if __name__ == '__main__':
    # For production, consider using Gunicorn or a similar server.
    app.run(debug=True)
