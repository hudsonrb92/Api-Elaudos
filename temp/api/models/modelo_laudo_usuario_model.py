from api import db


class ModeloLaudoUsuarioModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "modelo_laudo_usuario"

    identificador_modelo_laudo = db.Column(db.Integer, nullable=False, primary_key=True)
    identificador_usuario = db.Column(db.Integer, nullable=False)