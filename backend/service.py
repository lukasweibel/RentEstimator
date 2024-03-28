from flask import Flask, jsonify, request
from scrape.scrape import run_scraping
from model.forest import predict, optimize_model
from flask import Flask, send_from_directory
from flask import Flask
from db.db_accessor import get_all_models
from bson import ObjectId

app = Flask(__name__, static_folder='./../frontend/public', static_url_path='')

@app.route('/predict', methods=['POST'])
def run_function():

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    area = data.get('area')
    rooms = data.get('rooms')
    zip = data.get('zip')
    model = data.get('model')

    return predict(area, rooms, zip, model)

@app.route('/scrape', methods=['POST'])
def scrape():
    run_scraping()
    return "Done with scraping"

@app.route('/optimize', methods=['POST'])
def optimize():
    optimize_model()
    return "Done with scraping"

@app.route('/model', methods=['GET'])
def get_models():
    models = get_all_models()
    models_serializable = []
    for model in models:
        model['_id'] = str(model['_id'])
        models_serializable.append(model)
    return jsonify(models_serializable)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)