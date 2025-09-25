from flask import Flask, request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key = "mysecretkey"  # secret key for session management
#home page
@app.route('/',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form('username')
        password = request.form('password')
        
        if username == 'admin' and password == '123':
            session[username] = username
            return redirect(url_for('welcome'))
        else:                                         #just raw type data
            return Response('Invalid credentials',mimetype="text/plain", status=401)
    return '''
            <h2>Login Page</h2>
            <form method="POST">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <button type="submit">Login</button>
                </form>
            '''
@app.route('/welcome')
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome {session["user"]}!</h2>
            <a href={url_for('logout')}>Logout</a>
            <p>You are logged in.</p>
            <a href="/logout">Logout</a>
        '''
    return redirect(url_for('login'))