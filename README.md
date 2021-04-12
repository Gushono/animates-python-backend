# Teste Conta Simples

 
Boa tarde, tudo bem?

Meu nome é Gustavo e eu estou fazendo o desafio para o BACKEND



# Requerimentos para o projeto?
<!-- blank line -->
    1. Certifique-se de ter o python instalado.
<!-- blank line -->
    2. Certifique-se de ter um banco postgres que possa ser acessado dessa forma postgresql://postgres:@postgres@localhost:5432/postgres

# Como criar todas as tabelas do banco (Rodar as migrations)?
<!-- blank line -->
    1. Dentro do projeto execute o comando alembic upgrade head
    
# Como executar o projeto?
<!-- blank line -->
    1. Dentro da pasta do projeto, gere uma venv pelo comando virtualenv venv
<!-- blank line -->
    2. Ainda dentro da pasta utilize o comando pip install -r requirements.txt para instalar todas as bibliotecas necessárias
<!-- blank line -->
    3. Vá dentro da pasta server e no arquivo __main__ execute o projeto


# Facilitando o teste dos endpoints:

    Como padrão, ao gerar o banco ele cria dois usuários com as seguintes credênciais: 
    
    Usuário: empresa1
    Senha: 123 
    
    Usuário: empresa2
    Senha: 123
<!-- blank line -->      
    
<!-- blank line -->
    Para facilitar os testes do endpoints, gerei um arquivo que pode ser importado no 
    postman com o nome (entrevista.postman_collection.json)
    com todas as chamadas separadas por pasta e seu body
    
<!-- blank line -->
    
    Caso queiram acessar a documentação dos endpoints você pode acessar esse [link](http://127.0.0.1:8080/v1/ui)
    que terá acessa a documentação de cada um deles
    
# Autenticacao:
    Para a autenticação, gere o token e passe no HEADER x-auth-token e o token jwt

# Desafios cumpridos:
<!-- blank line -->
    1. Criar uma API de login [x]

    A api de login geraum token jwt e salva no banco. Em cada chamada ele valida o token vindo no header
<!-- blank line -->
    2. Criar uma API que retornar o saldo da conta [x]
<!-- blank line -->
    3. Cria API de extrato da conta -> filtrar por Data de Transação e flag de "Crédito" e "Débito" [x]
<!-- blank line -->
    4. Criar API pra retornar o última transação realizada da empresa logada [x]
<!-- blank line -->
    5. Endpoint para retornar transações agrupadas por cartão []
    
    Não consegui realizar.
    
# Agradecimentos
    Gostaria de agradecer pela oportunidade de demonstrar meus conhecimentos.
    Foi ótimo passar esse fim de semana fazendo o que amo! 
    
    
    

    
    