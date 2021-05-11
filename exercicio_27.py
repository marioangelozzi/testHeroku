from flask import Flask, jsonify, request 
import numpy as np
import pandas as pd
import pickle
import numpy as np
from exercicio_14_main import *


# instancia o objeto do Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing_page():
	return "hello world"

@app.route('/html', methods=['GET'])
def landing_page_html():
	return '<html><h1 style="color:red">hello world<h1></html>'

@app.route('/array', methods=['GET'])
def array():
    response = np.random.randint(0,100, 10)
    return np.array_str(response)

@app.route('/ndarray', methods=['GET'])
def ndarray():
    response = np.random.randint(0,100, 10).reshape(5,-1)
    return np.array_str(response)

@app.route('/table', methods=['GET'])
def table():
    response = np.random.randint(0,100, 10).reshape(5,-1)
    response = pd.DataFrame(response, columns=['col1','col2'])
    return response.to_html()

@app.route('/dynamic/<int:nrows>', methods=['GET'])
def dynamic(nrows):
    response = np.random.randint(0,100, 2*nrows).reshape(nrows,-1)
    response = pd.DataFrame(response, columns=['col1','col2'])
    return response.to_html()

@app.route('/json/<int:nrows>', methods=['GET'])
def json(nrows):
    response = np.random.randint(0,100, 2*nrows).reshape(nrows,-1)
    response = pd.DataFrame(response, columns=['col1','col2'])
    return response.to_json()

@app.route('/req/', methods=['GET'])
def req():
    method = request.method
    path = request.path
    accept_encodings = request.accept_encodings
    response = {'method':method,'path':path, 'content_encoding':accept_encodings}
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post():
    method = request.method
    user = request.headers['user']
    pwd = request.headers['pwd']
    response = {'method':method,'user':user,'pwd':pwd}
    return jsonify(response)

@app.route('/params/', methods=['GET'])
def params():
    method = request.method
    params = request.args
    print(params)
    response = params
    return jsonify(response)


@app.route('/predict/', methods=['GET'])
def predict(path = './serialized_model.pkl'):
    params = request.args.to_dict()
    print(params)
    file = open(path, 'rb')
    model_predictor = pickle.load(file)
    file.close

    # data: [size_house, size_lot, size_basement, latitude, longitude, avg_size_neighbor_houses, avg_size_neightbor_lot]
    values = [float(i) for i in params.values()]
    print(values)
    model_predictor.data = [values]
    response = model_predictor.predict()
    print(response)
    return jsonify(str(np.round(response,2)))

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')