from flask import Flask, render_template, request, redirect, url_for

import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database connection function
def connect_db():
    connection = None
    try:
        connection = sqlite3.connect("./database/pokeDb.sqlite")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    return connection

# Home route (displays data and form)
@app.route('/')
def index():
    return render_template('index.html')

# # Insert data route
# @app.route('/insert', methods=['POST'])
# def insert():
#     if request.method == 'POST':
#         name = request.form['name']
#         value = request.form['value']
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO your_table (name, value) VALUES (?, ?)", (name, value))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))

# # Delete data route
# @app.route('/delete/<string:name>/<string:value>', methods=['GET'])
# def delete(name, value):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM your_table WHERE name=? AND value=?", (name, value))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))

@app.route('/pokedex')
def pokedex():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokedex")
    rows = cursor.fetchall()
    conn.close()
    return render_template('pokedex.html', rows=rows)

@app.route('/playnow')
def pokerogue_ai():
    return render_template('playnow.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
