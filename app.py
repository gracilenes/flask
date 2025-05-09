from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de usuários (cada usuário é um dicionário)
listaUsuarios = []

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")

@app.route("/paginaLista")
def paginaLista():
    return render_template("listar.html", usuarios=listaUsuarios)

@app.route("/cadastrarUsuario", methods=["POST"])
def cadastrar():
    nome = request.form.get("nomeUsuario")
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    
    usuario = {"nome": nome, "login": login, "senha": senha}
    listaUsuarios.append(usuario)
    
    mensagem = "Usuário cadastrado com sucesso!"
    return render_template("resultado.html", mensagem=mensagem)

@app.route("/verificarUsuario", methods=["POST"])
def verificar():
    nome = request.form.get("nomeUsuario")
    encontrado = any(u["nome"] == nome for u in listaUsuarios)
    
    if encontrado:
        mensagem = "Você está cadastrado."
    else:
        mensagem = "Você NÃO está cadastrado."
    
    return render_template("resultado.html", mensagem=mensagem)

@app.route("/listarUsuarios")
def listarUsuarios():
    return render_template("listar.html", usuarios=listaUsuarios)

# Executar servidor
if __name__ == "__main__":
    app.run(debug=True)

