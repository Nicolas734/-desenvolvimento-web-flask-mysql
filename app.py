from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fatec2021",
  database="unes"
)
mysql = MySQL(app)


@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Home/")
def Home3():
    return render_template("Home.html")

@app.route("/Quem_Somos/")
def Quem_Somos():
    return render_template("Quem_Somos.html")

@app.route("/Contato/")
def Contato():
    return render_template("/Contato.html")

@app.route("/Quem_Somos")
def Quem_Somos2():
    return render_template("Quem_Somos.html")

@app.route("/Contato")
def Contato2():
    return render_template("Contato.html")

@app.route("/Home")
def Home2():
    return render_template("Home.html")



@app.route("/enviar",methods=["POST"])
def post_arquivo():
    if request.method == 'POST':
        cursor = connection.cursor()
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        querry = 'INSERT INTO usuario (email, assunto, descricao) VALUES (%s, %s, %s)'
        insert = (email, assunto, descricao)
        
        if not request.form['email']:
            return render_template("Contato.html")
        else:
            cursor.execute(querry, insert) 
            connection.commit()

            cursor.close()
            connection.close()
        return redirect(url_for('Contato'))



if __name__=="__main__":
    app.run(debug=True,port=5000)
