from flask import Flask, render_template, request
import mysql.connector

def get_db():
    return  mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'didar09k',
    database = 'test'
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')

        if not name or not email or not password:
            return "NO!!!"
        
        if len(password)<6:
            return "Min 6!"
        
        chek = "SELECT * FROM user WHERE email = %s"
        
        conn = get_db
        cursor = conn.cursor()
        query = 'INSERT INTO user (name, email, password) VALUES (%s, %s, %s)'
        v = (name, email, password)
        cursor.execute(query, v)
        conn.commit()

        cursor.close()
        conn.close()

        return f"So good!"
    return render_template('regis.html')

if __name__ == ('__main__'):
    app.run(debug=True)
