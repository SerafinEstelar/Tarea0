from unicodedata import name
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/form')
def Formulario():
    return render_template('form.html')

@app.route('/Resuldatos', methods=['POST'] )
def Resuldatos():
    Nombres=request.form['Nombres']
    Apellidopaterno=request.form['Apellidopaterno']
    ApellidoMaterno=request.form['ApellidoMaterno']
    genero=request.form['genero']
    Pais=request.form['Pais']
    date=request.form['date']
    Email=request.form['Email']
    password=request.form['password']

    return  "<h1>Nombres : " + Nombres + "</h1>"
    return  "<h2>Nombres : " + Apellidopaterno + "</h2>"
    return  "<h3>Nombres : " + ApellidoMaterno + "</h3>"
    return  "<h4>Nombres : " + genero + "</h4>"
    return  "<h5>Nombres : " + Pais + "</h5>"
    return  "<h6>Nombres : " + date + "</h6>"
    return  "<h7>Nombres : " + Email + "</h7>"
    return  "<h8>Nombres : " + password + "</h8>"



if __name__ == "__main__":
    app.run(debug=True)



#Por algun motivo dice Not Found Pero no se porque y es dificil programar sin poder visualizar, no importa lo que hago simplemente no responde