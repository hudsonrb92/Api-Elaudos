from api import db


class Sexo(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "Sexo"

    identificador = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)