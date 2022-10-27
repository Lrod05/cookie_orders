from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.models_order import Order
from flask_app.config.mysqlconnection import connectToMySQL



@app.route('/')
def index():
    orders=Order.get_all()
    return render_template('index.html', orders = orders)


@app.route('/new_order')
def new_order():
    return render_template('new_order.html')


@app.route('/create_order', methods=['POST'])
def create_order():
    if not Order.validate_order(request.form):
        return render_template('new_order.html')
    data = {
        'name' : request.form['name'],
        'cookie_type' : request.form['cookie_type'],
        'number_of_orders' : request.form['number_of_orders']
    }
    Order.save(request.form)
    Order.create_order(data)
    return redirect('/')

#update orders
@app.route('/edit/<int:order_id>', methods=['POST'])
def update_user(order_id):
    data = {
        'id' : order_id,
        'name' : request.form['name'],
        'cookie_type' : request.form['cookie_type'],
        'number_of_orders' : request.form['number_of_orders']
    }
    Order.update(data)
    return redirect('/')


#display order
@app.route('/edit/<int:order_id>')
def edit_order(order_id):
    data = {
        'id': order_id
    }
    order = Order.get_one(data)
    return render_template('edit_order.html', order = order)