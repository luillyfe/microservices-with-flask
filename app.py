from flask import Flask, request, Response
import json

app = Flask(__name__)


def get_data(file='data/customers.json'):
    with open(file, 'r') as json_file:
        return json.load(json_file)


def get_customer_by_id(id):
    customers = get_data()
    if bool(customers):
        for index, customer in enumerate(customers):
            if customer.get('customerID') == id:
                return [index, customer]
    return {}


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


@app.route("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = get_customer_by_id(customer_id)[1]
    if bool(customer):
        return Response(json.dumps(customer), mimetype="application/json")
    return Response(json.dumps({}), mimetype="application/json", status=404)


@app.route("/customers", methods=["POST"])
def add_customer():
    return Response(json.dumps(request.get_json()), mimetype="application/json", status=201)


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def replace_customer(customer_id):
    customers = get_data()
    [index, customer] = get_customer_by_id(customer_id)
    if bool(customer):
        customers[index] = request.get_data()
        return Response(mimetype="application/json", status=204)
    return Response(mimetype="application/json", status=404)


app.run(port=5000)
