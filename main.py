import bs4
import requests as req
from IPython.display import IFrame
import cgi,os
import codecs
import mysql.connector as m
from flask import Flask, render_template, request

mydb = m.connect(host = "localhost",user = "root",password="",database="busdb")

mycursor = mydb.cursor()

mycursor.execute("select * from users")
result = mycursor.fetchall()





app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html')

@app.route('/handle_data', methods=['GET','POST'])
def handle_data():
    
    return render_template('products.html', say=request.form['link'])


if __name__ == "__main__":
    app.run()

