#importar a classe Flask
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

#instanciar o servidor Flask
app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        print(f'Nome: {nome}, Email: {email}, Senha: {senha}')
        return render_template('sucesso.html', nome=nome)
    
    return render_template('cadastro.html')

# Rota para a página para remover usuário
@app.route('/remover_usuario', methods=['GET', 'POST'])
def remover_usuario():
    if request.method == 'POST':
# Obter os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        
        print(f'Usuário removido: Nome: {nome}, Email: {email}')
        return render_template('sucesso.html', nome=nome)
    
    return render_template('remover_usuario.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obter os dados do formulário
        email = request.form['email']
        senha = request.form['senha']
        
        print(f'Login: Email: {email}, Senha: {senha}')
        return render_template('sucesso.html', nome=email)
    
    return render_template('login.html')

