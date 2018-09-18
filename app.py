import json
from flask import request, Response
from db.settings import *


def get_data(file='data/customers.json'):
    with open(file, 'r') as json_file:
        return json.load(json_file)


def get_customer_by_id(id):
    customers = get_data()
    if bool(customers):
        for index, customer in enumerate(customers):
            if customer.get('customerID') == id:
                return [index, customer, customers]
    return {}


# GET /landing page
@app.route("/")
def welcome():
    return "Landing page"


# GET /customers
@app.route("/customers")
def get_customers():
    customers = get_data()
    if bool(customers):
        return Response(json.dumps(customers), mimetype="application/json")
    return Response(
        json.dumps({"message": "somenthing was wrong getting the data"}),
        mimetype="application/json", status=500
    )


# GET /customers/:customer_id
@app.route("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = get_customer_by_id(customer_id)[1]
    if bool(customer):
        response = Response(json.dumps(customer), mimetype="application/json", status=204)
        response.headers["Location"] = "/customers/" + customer_id
        return response
    return Response(json.dumps({}), mimetype="application/json", status=404)


# POST /customers
@app.route("/customers", methods=["POST"])
def add_customer():
    customers = get_data()
    customer = request.get_json()
    customers.insert(customer)
    response = Response(mimetype="application/json", status=201)
    response.headers["Location"] = "/customers/" + customer.customerID
    return response


# PUT /customers/:customer_id
@app.route("/customers/<int:customer_id>", methods=["PUT"])
def replace_customer(customer_id):
    customers = get_data()
    [index, customer] = get_customer_by_id(customer_id)
    if bool(customer):
        customers[index] = request.get_data()
        response = Response(mimetype="application/json", status=204)
        response.headers["Location"] = "/customers/" + customer_id
        return response
    return Response(mimetype="application/json", status=404)


# DELETE /customers/:customer_id
@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    [index, customer, customers] = get_customer_by_id(customer_id)
    if bool(customer):
        customers.pop(index)
        response = Response(mimetype="application/json", status=204)
        response.headers["Location"] = "/customers/" + customer_id
        return response
    return Response(mimetype="application/json", status=404)


app.run(port=5000)
