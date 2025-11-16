# app.py
from flask import Flask, request, jsonify
from grover_lib import grover_2qubit   # Import the function from the library

app = Flask(__name__)

@app.route('/grover', methods=['POST'])
def grover_api():
    data = request.json
    idx = int(data['marked_index'])
    results = grover_2qubit(idx)      # Call the imported function
    return jsonify(results)

# Optionally, add:
if __name__ == '__main__':
    app.run()