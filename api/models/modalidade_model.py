from api import db


class ModalidadeModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "modalidade"

    identificador = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String, nullable=False)
    descricao_original = db.Column(db.String, nullable=False)
    descricao_traduzida = db.Column(db.String, nullable=False)
    ativa = db.Column(db.Boolean, nullable=False)