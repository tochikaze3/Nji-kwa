from flask import Flask, render_template,request,redirect
from .models import Tasks
from .index import db

app = Flask(__name__)

@app.route('/', methods=['POST','GET','PUT'])
def task():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Tasks(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return "there was an issue with adding your tasks, please review your tasks"
    else:
        tasks = Tasks.query.order_by(Tasks.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/(int:id)')
def delete(id):
    task_to_delete = Tasks.query.get_or_48(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting the task "