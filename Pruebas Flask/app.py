from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'doctores'

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/registro')
def registro():
    return render_template('formularioMedicos.html')

@app.route('/guardarMedico', methods=['POST'])
def guardar_medico():
    if request.method == 'POST':
        Frfc = request.form['txtRFC']
        Fnombre = request.form['txtNombre']
        Fapp = request.form['txtApp']
        Fapm = request.form['txtApm']
        Fcedula = request.form['txtCedula']
        Fcorreo = request.form['txtCorreo']
        Fcontra = request.form['txtContra']
        Frol = request.form['txtRol']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO tbmedicos (rfc, nombre, app, apm, cedula, correo, password, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (Frfc, Fnombre, Fapp, Fapm, Fcedula, Fcorreo, Fcontra, Frol))
        mysql.connection.commit()

        flash('Médico registrado correctamente')
        return redirect(url_for('consultar_medicos'))

@app.route('/consultar_medicos')
def consultar_medicos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbmedicos')
    medicos = cursor.fetchall()
    return render_template('consultarMedicos.html', medicos=medicos)

# Manejo de excepciones para rutas
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
