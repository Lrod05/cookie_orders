from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Order:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_orders = data['number_of_orders']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_order(cls, data):
        query = """
                INSERT INTO cookie_order ( name, cookie_type, number_of_orders )
                VALUES ( %(name)s, %(cookie_type)s, %(number_of_orders)s )
                """
        return connectToMySQL('cookie_orders').query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_order;"
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders


    @classmethod
    def update(cls, form_data):
        query = """
                UPDATE cookie_order SET name = %(name)s, cookie_type = %(cookie_type)s, number_of_orders = %(number_of_orders)s
                WHERE id = %(id)s
                """
        return connectToMySQL('cookie_orders').query_db(query, form_data)


    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM cookie_order
                WHERE id = %(id)s
                """
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(order['cookie_type']) < 3:
            flash("Cookie type must be at least 3 characters.")
            is_valid = False
        if len(order['number_of_orders']) < 1:
            flash("Number of orders must be 1 or greater.")
            is_valid = False
        return is_valid