from myapp import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    content = db.Column(db.Text)
    todo_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title=None, content=None, todo_date=None, user_id=None):
        self.title = title
        self.content = content
        self.todo_date = todo_date
        self.user_id = user_id

    def get_date_str(self):
        return self.todo_date.strftime('%Y-%m-%d')

