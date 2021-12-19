from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Lista de productos"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": 'producto no encontrado'})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "cant": request.json['cant']
    }
    products.append(new_product)
    return jsonify({"message":'recibido', "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['cant'] = request.json['cant']
        return jsonify({"message":'actualizado', "products": productsFound[0]})
    return jsonify({"message": 'producto no encontrado'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"message": 'producto eliminado', "products": products})
    return jsonify({"message": 'producto no encontrado'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

