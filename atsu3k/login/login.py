

app = Flask(__name__)

# Definition of User Information
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

# If GET methods, transit to Login window.
@app.route('/', methods=['GET'])
def form():
    return render_template('login.html')

# Error check
@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('index.html'))
