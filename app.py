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

# Rota para Lista de Usuários Cadastrados
@app.route('/lista_usuarios', methods=['GET'])
def lista_usuarios():
    usuarios = [
        {'nome': 'João', 'email': 'joao@email.com'},
        {'nome': 'Maria', 'email': 'maria@email.com'}
    ]
    return render_template('listar.html', usuarios=usuarios)

# Rota Buscar usuário(pelo nome)
@app.route('/buscar_usuario', methods=['GET', 'POST'])
def buscar_usuario():
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.form['nome']
        
        print(f'Usuário buscado: Nome: {nome}')
        return render_template('sucesso.html', nome=nome)
    
    return render_template('buscar.html')

# Rota Alterar senha
@app.route('/alterar_senha', methods=['GET', 'POST'])
def alterar_senha():
    if request.method == 'POST':
        # Obter os dados do formulário
        email = request.form['email']
        nova_senha = request.form['nova_senha']
        
        print(f'Senha alterada: Email: {email}, Nova Senha: {nova_senha}')
        return render_template('sucesso.html', nome=email)
    
    return render_template('alterar_senha.html')

# Rota para recurar senha
@app.route('/recuperar_senha', methods=['GET', 'POST'])
def recuperar_senha():
    if request.method == 'POST':
        # Obter os dados do formulário
        email = request.form['email']
        
        print(f'Senha recuperada: Email: {email}')
        return render_template('sucesso.html', nome=email)
    
    return render_template('recuperar_senha.html')

# Rota para  função extra definida pelo aluno
@app.route('/funcao_extra', methods=['GET', 'POST'])
def funcao_extra():
    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        
        print(f'Função extra: Nome: {nome}, Email: {email}')
        return render_template('sucesso.html', nome=nome)
    
    return render_template('funcao_extra.html')