"""A minimal Flask app demonstrating routes, URL parameters, templates,
and both GET and POST handling."""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# in-memory "database" for this demo - resets every restart
tasks = []

@app.route("/")
def home():
    return render_template("index.html", task_count=len(tasks))

@app.route("/greet/<name>")
def greet(name):
    # <name> is a URL parameter, captured as a function argument
    return render_template("greet.html", name=name)

@app.route("/tasks", methods=["GET", "POST"])
def handle_tasks():
    if request.method == "POST":
        # request.form holds submitted form data; request.json holds JSON bodies
        title = request.form.get("title") or (request.json or {}).get("title")
        if not title:
            return jsonify({"error": "title is required"}), 400
        tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
        return jsonify(tasks[-1]), 201
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)
    return jsonify({"error": "task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
