from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        tasks.append({'title': title, 'description': description, 'due_date': due_date, 'completed': False})
        return redirect(url_for('index'))

    return render_template('add_task.html')


@app.route('/task/<int:task_id>')
def task_details(task_id):
    task = tasks[task_id]
    return render_template('task_details.html', task=task)


@app.route('/task/<int:task_id>/update', methods=['GET', 'POST'])
def update_task(task_id):
    task = tasks[task_id]

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['due_date'] = request.form['due_date']
        task['completed'] = 'completed' in request.form
        return redirect(url_for('index'))

    return render_template('update_task.html', task=task)


@app.route('/task/<int:task_id>/delete')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
