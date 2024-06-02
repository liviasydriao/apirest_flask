# API RESTful / Flask
 Este é um projeto simples em Python usando o framework Flask e a extensão Flask-Restx para criar uma API RESTful para operações básicas de usuário.

## Definição do modelo de usuário:
Define um modelo de usuário com campos como 'id', 'name' e 'email'.

## Criação da API:

Utiliza o Flask para criar uma aplicação web.
Usa o Flask-Restx para criar uma API RESTful.
Define um namespace 'users' para agrupar as operações relacionadas aos usuários.

## Rotas da API:

Define rotas para manipular operações CRUD (Create, Read, Update, Delete) em usuários.
Para acessar um usuário específico, utiliza-se o método GET com o ID do usuário na URL, que retorna o usuário correspondente.
Para atualizar um usuário, utiliza-se o método PUT com o ID do usuário na URL e os dados do usuário a serem atualizados no corpo da requisição.
Para excluir um usuário, utiliza-se o método DELETE com o ID do usuário na URL.
Para acessar todos os usuários, utiliza-se o método GET na rota principal.

## Manipulação de dados de usuário:

Armazena os usuários em uma lista chamada users_list.
Ao receber uma requisição, manipula os dados de usuário conforme a operação solicitada (criar, ler, atualizar, excluir).
Retorna respostas HTTP adequadas para indicar o sucesso ou falha das operações.

## Execução da aplicação:

Inicia a aplicação Flask em modo de depuração (debug=True), permitindo ver mensagens de erro detalhadas durante o desenvolvimento.

✔️ Em resumo, este projeto cria uma API RESTful simples para gerenciar usuários, permitindo operações como criar, ler, atualizar e excluir usuários, usando Flask e Flask-Restx em Python.
