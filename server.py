from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        session['ubicacion'] = request.form['ubicacion']
        session['lenguaje'] = request.form['lenguaje']
        session['comentarios'] = request.form['comentarios']
        return redirect('/result')
    return render_template('formulario.html')

@app.route('/result')
def result():
    nombre = session['nombre']
    ubicacion = session['ubicacion']
    lenguaje = session['lenguaje']
    comentarios =  session['comentarios']
    return render_template('resultado.html', nombre=nombre, ubicacion=ubicacion, lenguaje=lenguaje, comentarios=comentarios)

if __name__ == '__main__':
    app.run(debug=True)
