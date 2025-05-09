from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de usuários: cada usuário é um dicionário
listaUsuarios = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")

@app.route("/paginaLogin")
def paginaLogin():
    return render_template("login.html")

@app.route("/paginaLista")
def paginaLista():
    return render_template("listar.html", usuarios=listaUsuarios)

@app.route("/cadastrarUsuario", methods=["POST"])
def cadastrarUsuario():
    nome = request.form.get("nomeUsuario")
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")

    # Verifica se o login já existe
    for u in listaUsuarios:
        if u["login"] == login:
            return render_template("resultado.html", mensagem="Login já cadastrado!")

    usuario = {"nome": nome, "login": login, "senha": senha}
    listaUsuarios.append(usuario)
    return render_template("resultado.html", mensagem="Usuário cadastrado com sucesso!")

@app.route("/loginUsuario", methods=["POST"])
def loginUsuario():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")

    for u in listaUsuarios:
        if u["login"] == login and u["senha"] == senha:
            return render_template("resultado.html", mensagem=f"Bem-vindo, {u['nome']}!")

    return render_template("resultado.html", mensagem="Login ou senha inválidos.")

@app.route("/excluirUsuario/<login>")
def excluirUsuario(login):
    global listaUsuarios
    listaUsuarios = [u for u in listaUsuarios if u["login"] != login]
    return redirect(url_for("paginaLista"))

if __name__ == "__main__":
    app.run(debug=True)


