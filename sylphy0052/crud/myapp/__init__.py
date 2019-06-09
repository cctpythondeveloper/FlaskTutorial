from flask import Flask

app = Flask(__name__)
app.config.from_object('myapp.config')

from myapp.views import view
