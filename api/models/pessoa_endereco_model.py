from api import db


class PessoaEnderecoModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "pessoa_endereco"

    identificador_pessoa = db.Column(db.Integer, nullable=False, primary_key=True)
    identificador_endereco = db.Column(db.Integer, nullable=False)
    identificador_tipo_uso_endereco = db.Column(db.String, nullable=False)
    ativa = db.Column(db.Boolean, nullable=False)