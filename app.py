from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS vagas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            empresa TEXT NOT NULL,
                            descricao TEXT NOT NULL
                        )''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vagas')
def listar_vagas():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vagas")
        vagas = cursor.fetchall()
    return render_template('vagas.html', vagas=vagas)

@app.route('/nova', methods=['GET', 'POST'])
def nova_vaga():
    if request.method == 'POST':
        titulo = request.form['titulo']
        empresa = request.form['empresa']
        descricao = request.form['descricao']

        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vagas (titulo, empresa, descricao) VALUES (?, ?, ?)",
                           (titulo, empresa, descricao))
            conn.commit()
        return redirect('/vagas')

    return render_template('nova_vaga.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)