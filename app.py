from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Global list to store tasks
tasks = []

# Home page
template = """
<!doctype html>
<html>
<head>
    <title>Simple To-Do App</title>
</head>
<body>
    <h1>To-Do List</h1>
    <ul>
    {% for task in tasks %}
        <li>{{ task }}</li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('add_task') }}" method="post">
        <input type="text" name="task" placeholder="Enter a new task" required>
        <input type="submit" value="Add Task">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(template, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
