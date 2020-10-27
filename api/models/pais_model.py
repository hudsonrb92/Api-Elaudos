from api import db


class PaisModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "pais"
    identificador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
