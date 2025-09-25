#
from flask import Flask ,request

app = Flask(__name__)    # it is object to create a Flask application
#  decorator it is  used to add functionality to an existing function
@app.route('/') # decorator to tell Flask what URL should call the function    //// @app.route =  it use to specific web  connect to a specific finction 
# flask object 
def home():
    return 'Hello user ! this is my first Flask app'
                                                              # output is the comunication protoco

@app.route('/about')
def about():
    return 'this is about page'

@app.route('/contact')
def contact():
    return 'this is contact us page'

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        return 'you send only data'
    else: return 'you are only viewing the a page'
    
    
    
