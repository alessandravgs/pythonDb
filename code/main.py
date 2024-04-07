from bson import ObjectId

from config import SQLALCHEMY_DATABASE_URI, pedidos_collection
from flask import Flask, jsonify, render_template, request
from sqlalchemy import String, Float, Integer, Date
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
mysql = SQLAlchemy(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de pedidos, produtos e clientes"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Produtos(mysql.Model):
    id_produtos = mysql.Column(Integer, primary_key=True)
    nome = mysql.Column(String, nullable=False)
    descricao = mysql.Column(String, nullable=False)
    preco = mysql.Column(Float, nullable=False)
    categoria = mysql.Column(Date, nullable=False)

    def serialize(self):
        return {
            'id_produtos': self.id_produtos,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'categoria': self.categoria,
        }


class Clientes(mysql.Model):
    id_clientes = mysql.Column(Integer, primary_key=True)
    nome = mysql.Column(String, nullable=False)
    email = mysql.Column(String, nullable=False)
    cpf = mysql.Column(String, nullable=False)
    data_nascimento = mysql.Column(Date, nullable=False)

    def serialize(self):
        return {
            "id_clientes": self.id_clientes,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento
        }

class Pedido():
    def __init__(self, id_cliente, id_produto, data_pedido, valor_pedido):
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.data_pedido = data_pedido
        self.valor_pedido = valor_pedido

    def serialize(self):
        return {
            "id_cliente": self.id_cliente,
            "id_produto": self.id_produto,
            "data_pedido": self.data_pedido,
            "valor_pedido": self.valor_pedido,
        }

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/produtos", methods=['GET'])
def get_produtos():
    produtos = Produtos.query.all()
    return jsonify([produto.serialize() for produto in produtos])

@app.route("/produtos", methods=['POST'])
def set_produtos():
    try:
        dados = request.get_json()
        produto = Produtos(
            nome=dados['nome'],
            descricao=dados['descricao'],
            preco=dados['preco'],
            categoria=dados['categoria'],
        )
        mysql.session.add(produto)
        mysql.session.commit()
        return jsonify(produto.serialize()), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route("/produtos/<int:id>", methods=['PUT'])
def update_produtos(id):
    try:
        dados = request.get_json()
        produto = mysql.session.query(Produtos).filter_by(id_produtos=id).first()
        produto.nome = dados['nome']
        produto.descricao = dados['descricao']
        produto.preco = dados['preco']
        produto.categoria = dados['categoria']

        mysql.session.commit()
        return jsonify(produto.serialize()), 201
    except Exception as e:
        print(e)
        return jsonify({'Erro ao alterar dados de produtos: ': str(e)}), 400

@app.route("/produtos/<int:id>", methods=['DELETE'])
def delete_produtos(id):
    try:
        produto = mysql.session.query(Produtos).filter_by(id_produtos=id).first()
        mysql.session.delete(produto)
        mysql.session.commit()
        return jsonify("Produto deletado com sucesso!"), 204
    except Exception as e:
        print(e)
        return jsonify("Erro ao deletar dados de produtos: " + str(e)), 400

@app.route("/clientes", methods=['GET'])
def get_clientes():
    clientes = Clientes.query.all()
    return jsonify([cliente.serialize() for cliente in clientes])

@app.route("/clientes", methods=['POST'])
def set_clientes():
    try:
        dados = request.get_json()
        cliente = Clientes(
            nome=dados['nome'],
            email=dados['email'],
            cpf=dados['cpf'],
            data_nascimento=dados['data_nascimento']
        )
        mysql.session.add(cliente)
        mysql.session.commit()
        return jsonify(cliente.serialize()), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

@app.route("/clientes/<int:id>", methods=['PUT'])
def update_clientes(id):
    try:
        dados = request.get_json()
        cliente = mysql.session.query(Clientes).filter_by(id_clientes=id).first()
        cliente.nome = dados['nome']
        cliente.email = dados['email']
        cliente.cpf = dados['cpf']
        cliente.data_nascimento = dados['data_nascimento']

        mysql.session.commit()
        return jsonify(cliente.serialize()), 201
    except Exception as e:
        print(e)
        return jsonify({'Erro ao alterar dados de clientes: ': str(e)}), 400

@app.route("/clientes/<int:id>", methods=['DELETE'])
def delete_clientes(id):
    try:
        cliente = mysql.session.query(Clientes).filter_by(id_clientes=id).first()
        mysql.session.delete(cliente)
        mysql.session.commit()
        return jsonify("Cliente deletado com sucesso!"), 204
    except Exception as e:
        print(e)
        return jsonify("Erro ao deletar dados de Clientes: " + str(e)), 400

@app.route("/pedidos", methods=['POST'])
def set_pedido():
    dados = request.get_json()
    novo_pedido = Pedido(
        id_produto=dados["id_produto"],
        id_cliente=dados['id_cliente'],
        data_pedido=dados["data_pedido"],
        valor_pedido=dados["valor_pedido"]
    )
    resultado = pedidos_collection.insert_one(novo_pedido.serialize())
    if resultado.inserted_id:
        # Retorna o pedido recém-criado e o status 201
        novo_pedido.id_pedido = str(resultado.inserted_id)
        return jsonify(novo_pedido.serialize()), 201
    else:
        return "Erro ao inserir pedido.", 500

@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    try:
        pedidos = pedidos_collection.find()

        # Convertendo ObjectId em strings para serialização
        pedidos_serializaveis = []
        for pedido in pedidos:
            pedido['_id'] = str(pedido['_id'])
            pedidos_serializaveis.append(pedido)

        return jsonify(pedidos_serializaveis), 200
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao listar pedidos.", 500

@app.route("/pedidos/<id>", methods=["PUT"])
def update_pedido(id):
    try:
        if not (ObjectId.is_valid(id)):
            return "Id informado não é válido.", 400

        dados = request.get_json()
        pedido = pedidos_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": {
                "id_produto": dados["id_produto"],
                "id_cliente": dados['id_cliente'],
                "data_pedido": dados["data_pedido"],
                "valor_pedido": dados["valor_pedido"]
            }},
            return_document=True
        )
        if pedido:
            pedido['_id'] = str(pedido['_id'])
            return jsonify(pedido), 200
        else:
            return "Pedido não encontrado.", 404
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao atualizar pedido.", 500

@app.route("/pedidos/<id>", methods=["DELETE"])
def delete_pedido(id):
    try:
        if not (ObjectId.is_valid(id)):
            return "Id informado não é válido.", 400

        resultado = pedidos_collection.delete_one({"_id": ObjectId(id)})
        if resultado.deleted_count > 0:
            return "Pedido deletado com sucesso.", 204
        else:
            return "Pedido não encontrado.", 404
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao deletar pedido.", 500

if __name__ == "__main__":
    app.run(debug=True)