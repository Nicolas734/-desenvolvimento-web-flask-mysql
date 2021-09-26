from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def hellow_wolrd():
    return "<h1>Judy Alvarez</h1>"

@app.route("/Home/")
def Home():
    return render_template("Home.html")

@app.route("/Quem_Somos/")
def Quem_Somos():
    return render_template("Quem_Somos.html")

@app.route("/Contato/")
def Contato():
    return render_template("/Contato.html")

@app.route("/Quem_Somos")
def Quem_Somos2():
    return render_template("Quem_Somos.html");

@app.route("/Contato")
def Contato2():
    return render_template("Contato.html");

@app.route("/Home")
def Home2():
    return render_template("Home.html")
