from flask import Flask, jsonify, request
from scrape.scrape import run_scraping

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def run_function():
    return "hello"

@app.route('/scrape', methods=['POST'])
def start_scraping():
    run_scraping()
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)