from flask import Flask, jsonify, render_template
from utils import load_data
from analysis import perform_analysis
import os

# app = Flask(__name__)

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET'])
def analyze():
    # Load data from CSV
    data_path = os.path.join('data', 'data.csv')
    data = load_data(data_path)

    # Perform analysis
    results = perform_analysis(data)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
