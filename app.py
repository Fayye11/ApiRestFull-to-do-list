from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello')
def hello():
    return 'Hello world!'
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
if __name__ == '__main__':
    app.debug = True
    app.run()