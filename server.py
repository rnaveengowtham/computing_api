from flask import Flask, request, jsonify
import os

app = Flask(__name__)

tasks = [
    {"task_id": 1, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/320px-Cat03.jpg"}
]

results = []

@app.route('/get_task', methods=['GET'])
def get_task():
    if tasks:
        return jsonify(tasks.pop(0))
    else:
        return jsonify({"message": "No tasks available"}), 404

@app.route('/submit_result', methods=['POST'])
def submit_result():
    data = request.json
    results.append(data)
    return jsonify({"message": "Result received", "data": data})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
