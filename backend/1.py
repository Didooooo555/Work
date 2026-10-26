from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1.html')

@app.route('/dido')
def dido():
    return 'hello'

if __name__ == ('__main__'):
    app.run(debug=True)