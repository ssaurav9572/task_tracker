from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []


@app.route('/')
def index():
    """
    Render the homepage with the list of tasks.

    Returns:
        HTML: Rendered template with tasks.
    """
    return render_template('index.html', tasks=tasks)


@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    """
    Add a new task to the list.

    Returns:
        HTML: Rendered template for adding a new task.
    """
    if request.method == 'POST':
        # Retrieve task details from form submission
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        # Append the new task to the list
        tasks.append({'title': title, 'description': description, 'due_date': due_date, 'completed': False})
        
        # Redirect to the homepage after adding the task
        return redirect(url_for('index'))

    # Render the template for adding a new task
    return render_template('add_task.html')


@app.route('/task/<int:task_id>')
def task_details(task_id):
    """
    Render the details of a specific task.

    Args:
        task_id (int): Index of the task in the list.

    Returns:
        HTML: Rendered template with task details.
    """
    # Retrieve the task details based on the task_id
    task = tasks[task_id]
    return render_template('task_details.html', task=task, task_id=task_id)


@app.route('/task/<int:task_id>/update', methods=['GET', 'POST'])
def update_task(task_id):
    """
    Update the details of a specific task.

    Args:
        task_id (int): Index of the task in the list.

    Returns:
        HTML: Rendered template for updating a task.
    """
    task = tasks[task_id]

    if request.method == 'POST':
        # Update task details from form submission
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['due_date'] = request.form['due_date']
        task['completed'] = 'completed' in request.form
        
        # Redirect to the homepage after updating the task
        return redirect(url_for('index'))

    # Render the template for updating a task
    return render_template('update_task.html', task=task, task_id=task_id)


@app.route('/task/<int:task_id>/delete')
def delete_task(task_id):
    """
    Delete a specific task from the list.

    Args:
        task_id (int): Index of the task in the list.

    Returns:
        Redirect: Redirects to the homepage after deleting the task.
    """
    # Remove the task from the list
    tasks.pop(task_id)
    
    # Redirect to the homepage after deleting the task
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

