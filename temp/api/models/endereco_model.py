from api import db


class EnderecoModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'endereco'

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_tipo_endereco = db.Column(db.Integer, nullable=False)
    logradouro = db.Column(db.String, nullable=False)
    complemento = db.Column(db.Text, nullable=True)
    bairro = db.Column(db.String, nullable=True)
    cep = db.Column(db.Integer, nullable=False)
    identificador_cidade = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
