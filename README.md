# API de Pedidos, Produtos e Clientes

Esta API permite gerenciar pedidos, produtos e clientes em um sistema de vendas.

## Como usar

1. Clone o repositório:

  - https://github.com/alessandravgs/pythonDb.git

2. Instale as dependências:

   - pip install -r requirements.txt

3. Configure o banco de dados:

   - Certifique-se de ter um servidor MySQL e um servidor mongoDb em execução
   - Edite o arquivo `config.py` com as credenciais do seu banco de dados

4. Execute o aplicativo:

  - python app.py

A API estará acessível em `http://localhost:5000`.

## Endpoints

### Produtos

- `GET /produtos`: Retorna todos os produtos
- `POST /produtos`: Cria um novo produto
- `PUT /produtos/{id}`: Atualiza um produto existente
- `DELETE /produtos/{id}`: Deleta um produto existente

### Clientes

- `GET /clientes`: Retorna todos os clientes
- `POST /clientes`: Cria um novo cliente
- `PUT /clientes/{id}`: Atualiza um cliente existente
- `DELETE /clientes/{id}`: Deleta um cliente existente

### Pedidos

- `GET /pedidos`: Retorna todos os pedidos
- `POST /pedidos`: Cria um novo pedido
- `PUT /pedidos/{id}`: Atualiza um pedido existente
- `DELETE /pedidos/{id}`: Deleta um pedido existente

Para mais detalhes sobre como usar cada endpoint, consulte a documentação Swagger da API.

## Documentação Swagger

A documentação Swagger da API está disponível em `http://localhost:5000/` ou  `http://localhost:5000/swagger`.

## Arquivos extras inseridos no projeto

- Na pasta `banco_de_dados` estão os dados .sql do banco Mysql e os dados json do banco mongoDb.
- Na pasta `postman` está inserido o arquivo postman exportado com todas as consultas.
- Na pasta `static` está o arquivo do Swagger.json.
- Na pasta `templates` está o arquivo index.html que é exibido na página inicial do projeto.

