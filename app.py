from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample task for users
tasks = [
    {"task_id": 1, "task_type": "image_classification", "data": "image_url"},
    {"task_id": 2, "task_type": "speech_to_text", "data": "audio_url"}
]

# Route to fetch an AI task
@app.route("/get_task", methods=["GET"])
def get_task():
    return jsonify({"task": tasks[0]})  # Returns a sample task

# Route to submit processed results
@app.route("/submit_result", methods=["POST"])
def submit_result():
    data = request.get_json()
    task_id = data.get("task_id")
    result = data.get("result")

    if not task_id or not result:
        return jsonify({"error": "Missing task_id or result"}), 400
    
    return jsonify({"message": f"Task {task_id} completed!", "status": "success"})

# Home route
@app.route("/")
def home():
    return "AI Task Processing API is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
