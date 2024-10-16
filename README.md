Aplicação de Lista de Tarefas (To-do List)

Este projeto é uma aplicação web de Lista de Tarefas (To-do List), que permite aos usuários criar, ler, atualizar e excluir (CRUD) tarefas. O backend é construído com Node.js, usando o framework Express para lidar com requisições HTTP, e um banco de dados SQL (como SQLite ou MySQL) para armazenar as tarefas. O frontend é desenvolvido com HTML, CSS e JavaScript, proporcionando uma interface de usuário simples e responsiva.

Funcionalidades

Adicionar tarefas: Permite que os usuários criem novas tarefas e as adicionem à lista.
Visualizar tarefas: Exibe uma lista de todas as tarefas salvas no banco de dados.
Atualizar tarefas: Os usuários podem editar a descrição das tarefas.
Excluir tarefas: Permite que os usuários removam tarefas da lista.
Armazenamento persistente de dados: As tarefas são salvas em um banco de dados SQL, garantindo que os dados permaneçam mesmo após a atualização da página.
Design responsivo: A interface adapta-se a diferentes tamanhos de tela, proporcionando uma boa experiência tanto em desktops quanto em dispositivos móveis.


Tecnologias Utilizadas


Frontend:
HTML5 & CSS3
JavaScript (ES6+)
Backend:
Node.js
Express.js
Banco de dados SQL (SQLite, MySQL ou PostgreSQL)
Outras ferramentas:
API Fetch para lidar com requisições HTTP
Como Executar Localmente


Clone o repositório:


git clone https://github.com/seuusuario/todo-list-app.git
cd todo-list-app


Instale as dependências:


npm install
Configure o banco de dados:

Se estiver utilizando SQLite, certifique-se de que o banco de dados esteja corretamente inicializado no projeto.
Para MySQL ou PostgreSQL, configure as credenciais do banco de dados em um arquivo .env ou diretamente no código.


Inicie o servidor:


npm start
Abra a aplicação no navegador:

Acesse http://localhost:5000 para usar a aplicação de To-do List.
