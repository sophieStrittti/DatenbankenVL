from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
# map mehrere URLs, eine funktion
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/floor')
def floor():
    return '<h2>Routines with music</h2>'

@app.route('/beam')
def beam():
    return '10 cm width'

# request Methoden
@app.route('/methodsTest', methods=['GET', 'POST'])
def methodsTest():
    if request.method == 'POST':
        return 'you are using POST'
    else:
        return 'you are probably using GET'

# Variablennutzung
@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username

#Variablennutzung Int (ist anders als normal mit string)
@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post id is %s" % post_id


if __name__ == "__main__":
    app.run()