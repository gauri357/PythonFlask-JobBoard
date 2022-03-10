import sqlite3
from flask import Flask, render_template
PATH ='db/jobs.sqlite'
app = Flask(__name__)
def open_connection():
    connection = getattr(g, '_connection', None)
    if  connection == None:
         conection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.row
    return  connection

def  execute_sql(sql, values=(), commit=false, single=false):
    conection = open_connection()
    cursor = conection.execute (sql,vaules)
    if commit == True:
        results = conection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception)
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')