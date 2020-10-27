from api import db


class PerfilModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "perfil"

    identificador = db.Column(db.String, nullable=False, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
