## **🧠 1\. Flask – Fundamentos**

### **📄 Estrutura básica de um app Flask:**

`from flask import Flask, render_template`

`app = Flask(__name__)`

`@app.route('/')`  
`def index():`  
    `return 'Olá, mundo!'`

`if __name__ == '__main__':`  
    `app.run(debug=True)`

### **💡 Conceitos:**

* `@app.route('/')`: define uma rota (endereço)

* `render_template('arquivo.html')`: renderiza arquivos HTML com Jinja2

* `debug=True`: atualiza o app automaticamente a cada mudança

---

## **🔐 2\. Flask-Login – Autenticação**

### **📦 Instalação:**

`pip install flask-login`

### **⚙️ Configuração:**

`from flask_login import LoginManager`

`login_manager = LoginManager()`  
`login_manager.init_app(app)`  
`login_manager.login_view = 'login'`

### **🧑 Classe `User`:**

`from flask_login import UserMixin`

`class User(UserMixin):`  
    `def __init__(self, id, nome, senha):`  
        `self.id = id`  
        `self.nome = nome`  
        `self.senha = senha`

### **📌 Métodos principais:**

* `login_user(user)`

* `logout_user()`

* `current_user`

* `@login_required`

---

## **🧱 3\. Schema e Banco de Dados (SQLite)**

### **📄 Exemplo de `schema.sql`**

`CREATE TABLE IF NOT EXISTS users (`  
    `id INTEGER PRIMARY KEY AUTOINCREMENT,`  
    `nome TEXT NOT NULL,`  
    `senha TEXT NOT NULL`  
`);`

### **🧪 Inserindo usuário:**

`import sqlite3`

`def adicionar_usuario(nome, senha_hash):`  
    `conn = sqlite3.connect('meubanco.sqlite')`  
    `cursor = conn.cursor()`  
    `cursor.execute("INSERT INTO users (nome, senha) VALUES (?, ?)", (nome, senha_hash))`  
    `conn.commit()`  
    `conn.close()`

### **🔐 Hash de senha com `werkzeug.security`:**

`from werkzeug.security import generate_password_hash, check_password_hash`

`hash = generate_password_hash("senha123")`  
`check = check_password_hash(hash, "senha123")  # True`

---

## **🔁 4\. Integração Completa: Cadastro \+ Login**

### **🔓 Registro:**

`@app.route('/register', methods=['GET', 'POST'])`  
`def register():`  
    `if request.method == 'POST':`  
        `nome = request.form['nome']`  
        `senha = generate_password_hash(request.form['senha'])`  
        `adicionar_usuario(nome, senha)`  
        `flash('Cadastro realizado!')`  
        `return redirect('/login')`  
    `return render_template('register.html')`

### **🔐 Login:**

`@app.route('/login', methods=['GET', 'POST'])`  
`def login():`  
    `if request.method == 'POST':`  
        `nome = request.form['nome']`  
        `senha = request.form['senha']`  
        `user = buscar_usuario(nome)`  
        `if user and check_password_hash(user['senha'], senha):`  
            `login_user(User(user['id'], user['nome'], user['senha']))`  
            `return redirect('/dashboard')`  
        `else:`  
            `flash('Login inválido!')`  
    `return render_template('login.html')`  
---

## **🧠 1\. FLASK – FUNDAMENTOS**

### **✅ O que é o Flask?**

* É um **framework web em Python**.

* Serve para **criar sites, sistemas, APIs** e outras aplicações web.

* É **leve e flexível**, ótimo para aprender e também para projetos reais.

### **📦 Como instalar:**

`pip install flask`

### **🗂️ Estrutura mínima de um projeto Flask:**

`meu_app/`  
`│`  
`├── app.py                # Arquivo principal da aplicação`  
`├── templates/            # Pasta com arquivos HTML`  
`│   └── index.html`

### **📄 Exemplo básico de `app.py`:**

`from flask import Flask, render_template`

`app = Flask(__name__)`

`@app.route('/')`  
`def index():`  
    `return render_template('index.html')`

`if __name__ == '__main__':`  
    `app.run(debug=True)`

### **🔍 Explicação:**

* `Flask(__name__)`: cria a aplicação.

* `@app.route('/')`: define a **rota** raiz do site (página inicial).

* `render_template('index.html')`: carrega um arquivo HTML dentro da pasta `templates`.

---

## **🔐 2\. FLASK-LOGIN – Autenticação de Usuário**

### **🔐 Objetivo:**

* Gerenciar **login**, **logout** e **sessões** de usuários.

* Permite proteger páginas com `@login_required`.

---

### **👤 Criando classe de usuário:**

`from flask_login import UserMixin`

`class User(UserMixin):`  
    `def __init__(self, id, nome, senha):`  
        `self.id = id`  
        `self.nome = nome`  
        `self.senha = senha`

**`UserMixin`** fornece:

* `is_authenticated`: verifica se o usuário está logado

* `is_active`, `is_anonymous`, `get_id()`

---

### **🔐 Funções importantes:**

`from flask_login import login_user, logout_user, current_user, login_required`

* `login_user(user)`: faz login de um usuário.

* `logout_user()`: faz logout.

* `current_user`: acessa o usuário logado.

* `@login_required`: protege rotas (só quem estiver logado acessa).

---

## **🧱 3\. SCHEMA E BANCO DE DADOS (SQLite)**

### **✅ O que é schema?**

* É um **modelo da estrutura do banco de dados**.

* Define as tabelas, colunas, tipos de dados e chaves.

### **🧪 Exemplo de arquivo `schema.sql`:**

`CREATE TABLE IF NOT EXISTS users (`  
    `id INTEGER PRIMARY KEY AUTOINCREMENT,`  
    `nome TEXT NOT NULL,`  
    `senha TEXT NOT NULL`  
`);`

**Explicação:**

* `id`: identificador único de cada usuário.

* `AUTOINCREMENT`: aumenta o ID automaticamente.

* `NOT NULL`: campo obrigatório.

---

### **📌 Inserir dados via Python:**

`import sqlite3`

`def adicionar_usuario(nome, senha_hash):`  
    `conn = sqlite3.connect('meubanco.sqlite')`  
    `cursor = conn.cursor()`  
    `cursor.execute("INSERT INTO users (nome, senha) VALUES (?, ?)", (nome, senha_hash))`  
    `conn.commit()`  
    `conn.close()`

---

### **🔐 Senhas seguras com hash:**

`from werkzeug.security import generate_password_hash, check_password_hash`

`hash = generate_password_hash("senha123")`  
`check = check_password_hash(hash, "senha123")  # Retorna True`

* Nunca salve senhas puras no banco\!

* Use hash para proteger os dados do usuário.

---

## **🔁 4\. INTEGRAÇÃO COMPLETA: Cadastro e Login**

### **📝 Formulário de Registro:**

`@app.route('/register', methods=['GET', 'POST'])`  
`def register():`  
    `if request.method == 'POST':`  
        `nome = request.form['nome']`  
        `senha = request.form['senha']`  
        `senha_hash = generate_password_hash(senha)`  
        `adicionar_usuario(nome, senha_hash)`  
        `flash('Cadastro realizado com sucesso!')`  
        `return redirect('/login')`  
    `return render_template('register.html')`

### **🔐 Login do usuário:**

`@app.route('/login', methods=['GET', 'POST'])`  
`def login():`  
    `if request.method == 'POST':`  
        `nome = request.form['nome']`  
        `senha = request.form['senha']`  
        `user = buscar_usuario(nome)  # Função que pega o usuário do banco`  
        `if user and check_password_hash(user['senha'], senha):`  
            `login_user(User(user['id'], user['nome'], user['senha']))`  
            `return redirect('/dashboard')`  
        `else:`  
            `flash('Login inválido')`  
    `return render_template('login.html')`

---

### **🔒 Protegendo uma rota:**

`@app.route('/dashboard')`  
`@login_required`  
`def dashboard():`  
    `return f'Olá, {current_user.nome}!'`

---

## **💡 Resumindo:**

| Conceito | Serve para... |
| ----- | ----- |
| Flask | Criar páginas e rotas |
| Flask-Login | Fazer login/logout e proteger páginas |
| Schema (SQL) | Estrutura do banco: tabelas, colunas, tipos de dados |
| SQLite | Banco de dados leve usado com Python |
| Senha com hash | Segurança\! Protege senhas com criptografia |

### **🧩 CÓDIGO COMPLETO:**

import sqlite3

def adicionar\_usuario(nome, senha\_hash):  
    conn \= sqlite3.connect('meubanco.sqlite')  
    cursor \= conn.cursor()  
    cursor.execute("INSERT INTO users (nome, senha) VALUES (?, ?)", (nome, senha\_hash))  
    conn.commit()  
    conn.close()

---

## **💬 EXPLICAÇÃO LINHA A LINHA:**

---

### **🔹 `import sqlite3`**

* Importa a **biblioteca SQLite do Python**, que permite trabalhar com banco de dados diretamente, **sem precisar instalar nada**.

* Ela serve para criar, consultar, inserir e alterar dados em arquivos `.sqlite`.

---

### **🔹 `def adicionar_usuario(nome, senha_hash):`**

* Define uma função chamada `adicionar_usuario`.

* Essa função espera **dois parâmetros**:

  * `nome`: o nome do usuário (string)

  * `senha_hash`: a senha já criptografada com `generate_password_hash()`.

---

### **🔹 `conn = sqlite3.connect('meubanco.sqlite')`**

* Conecta com o **arquivo de banco de dados SQLite** chamado `meubanco.sqlite`.

* Se esse arquivo **não existir**, ele será criado automaticamente.

* A variável `conn` representa a **conexão ativa** com o banco.

---

### **🔹 `cursor = conn.cursor()`**

* Cria um **cursor**, que é o objeto responsável por **executar comandos SQL** (tipo `INSERT`, `SELECT`, etc).

* Com ele, conseguimos interagir com o banco de dados.

---

### **🔹 `cursor.execute("INSERT INTO users (nome, senha) VALUES (?, ?)", (nome, senha_hash))`**

* Esse comando **insere** um novo registro na tabela `users`.

* `"INSERT INTO users (nome, senha) VALUES (?, ?)"` é a instrução SQL.

* Os `?` são **placeholders**: eles serão substituídos pelos valores das variáveis `(nome, senha_hash)`.

* Isso é importante para **evitar SQL Injection** (ataques de hackers).

🧠 Exemplo:  
 Se `nome = "tamiris"` e `senha_hash = "abc123xyz"`, o comando vai inserir:

INSERT INTO users (nome, senha) VALUES ('tamiris', 'abc123xyz');

---

### **🔹 `conn.commit()`**

* Salva (**confirma**) a transação no banco.

* Sem esse comando, os dados não são realmente gravados.

---

### **🔹 `conn.close()`**

* Fecha a conexão com o banco.

* É importante liberar o recurso para evitar erros ou travamentos no app.

---

## **🧪 Resumo visual:**

| Linha | Função |
| ----- | ----- |
| `import sqlite3` | Usa a biblioteca para mexer no banco de dados SQLite |
| `connect(...)` | Abre conexão com o banco (cria se não existir) |
| `cursor = conn.cursor()` | Permite executar comandos SQL |
| `cursor.execute(...)` | Insere os dados no banco com segurança |
| `conn.commit()` | Confirma a gravação dos dados |
| `conn.close()` | Fecha a conexão com o banco |

---

## **🔐 Objetivo:**

Esse código serve para **proteger senhas dos usuários** usando **criptografia (hash)**, evitando que fiquem visíveis no banco de dados.

---

## **🧩 Código:**

from werkzeug.security import generate\_password\_hash, check\_password\_hash

hash \= generate\_password\_hash("senha123")  
check \= check\_password\_hash(hash, "senha123")  \# Retorna True

---

### **📌 LINHA 1**

from werkzeug.security import generate\_password\_hash, check\_password\_hash

* Está **importando duas funções** da biblioteca `werkzeug.security`:

| Função | Serve para... |
| ----- | ----- |
| `generate_password_hash` | **Criptografar** a senha antes de salvar no banco |
| `check_password_hash` | Verificar se a senha digitada **bate com o hash** |

---

### **🔹 `hash = generate_password_hash("senha123")`**

* Essa linha **transforma a senha "senha123" em um hash criptografado**.

Exemplo de como fica (não é reversível\!):

 pbkdf2:sha256:260000$Bt3GEx6EGI3KsLkN$4d6e1e9a...

* 

✅ Esse **hash é salvo no banco**, **nunca a senha original**.

---

### **🔹 `check = check_password_hash(hash, "senha123")`**

* Aqui, estamos verificando se a senha digitada pelo usuário (`"senha123"`) **corresponde** ao hash salvo no banco.

A função faz a **comparação de forma segura**:

 check\_password\_hash(hash, "senha123")  \# Retorna True se estiver correta

* 

---

## **🧪 Exemplo prático no contexto de login:**

senha\_digitada \= "senha123"  
senha\_no\_banco \= "pbkdf2:sha256:260000$Bt3G..."  \# hash salvo no banco

if check\_password\_hash(senha\_no\_banco, senha\_digitada):  
    print("Senha correta\!")  
else:  
    print("Senha incorreta\!")

---

## **🚨 Por que usar isso?**

🔒 **Segurança**: se alguém invadir seu banco, não consegue ver as senhas.

💣 **Evita ataques**: não usar `hash` é um erro de segurança gravíssimo.

---

## **🔁 Resumo final:**

| Função | Explicação |
| ----- | ----- |
| `generate_password_hash(s)` | Transforma a senha em um hash seguro |
| `check_password_hash(h, s)` | Compara o hash com a senha digitada; retorna `True` ou `False` |

---

## **✅ Parte 1 – Questões Objetivas de Múltipla Escolha**

---

### **1\. Para que serve a função `generate_password_hash()` no Flask?**

A) Criptografar dados do banco de dados  
B) Gerar uma senha aleatória para o usuário  
C) Converter a senha em um hash seguro antes de salvar no banco  
D) Verificar se a senha está correta

✅ **Resposta correta: C)**

**C) Converter a senha em um hash seguro antes de salvar no banco**

🧠 Explicação:  
 Essa função transforma a senha digitada pelo usuário em um hash criptografado. Assim, ela **não fica visível nem decodificável** no banco de dados.

---

### **2\. Qual das alternativas permite proteger uma rota para que só usuários logados possam acessá-la usando Flask-Login?**

A) `@secure_route()`  
B) `@authenticated()`  
C) `@login_required`  
D) `@only_users`

`✅ Resposta correta: C)`

**`C) @login_required`**

`🧠 Explicação:`  
 `Esse decorador (@login_required) só permite acessar a rota se o usuário estiver autenticado com Flask-Login.`

---

### **3\. O que a função `check_password_hash(hash, senha_digitada)` faz?**

A) Comparar dois textos simples  
B) Gera um novo hash de senha  
C) Verifica se a senha digitada corresponde ao hash armazenado  
D) Cria uma sessão para o usuário

✅ **Resposta correta: C)**

**C) Verifica se a senha digitada corresponde ao hash armazenado**

🧠 Explicação:  
 Ela compara a senha digitada com o hash salvo no banco. Se forem equivalentes, retorna `True`.

---

### **4\. O que acontece se você esquecer de usar `conn.commit()` ao salvar um novo usuário no banco SQLite?**

A) O banco será apagado  
B) Os dados não serão gravados de verdade  
C) O Flask exibirá um erro  
D) A senha será salva em texto puro

✅ **Resposta correta: B)**

**B) Os dados não serão gravados de verdade**

🧠 Explicação:  
 Sem o `commit()`, o Python **não grava definitivamente as alterações** no banco. Os dados somem após fechar a conexão.

---

### **5\. Qual comando SQL cria uma tabela chamada `users` com `id`, `nome` e `senha`?**

1) CREATE users TABLE (id INT, nome TEXT, senha TEXT);

2) CREATE TABLE users (id TEXT, nome TEXT, senha TEXT);  
     
3) CREATE TABLE IF NOT EXISTS users (  
       id INTEGER PRIMARY KEY AUTOINCREMENT,  
       nome TEXT NOT NULL,  
       senha TEXT NOT NULL  
   );  
   

🧠 Explicação:  
Essa sintaxe cria uma tabela segura e bem estruturada, com ID automático, nome e senha obrigatórios.

---

## **🧪 Parte 2 – Prática (Desafio para Você Fazer Sozinha)**

Crie um pequeno app Flask com:

### **🎯 Desafio:**

* Um formulário de **cadastro** (`/register`) que:

  * Recebe nome e senha

  * Criptografa a senha

  * Salva no banco de dados SQLite

* Um formulário de **login** (`/login`) que:

  * Pega o nome e senha digitados

  * Verifica se a senha digitada **bate com o hash salvo**

  * Mostra "Login realizado\!" ou "Credenciais inválidas"

* Um botão que leva para a **página inicial** com link para cadastro e login.

---

