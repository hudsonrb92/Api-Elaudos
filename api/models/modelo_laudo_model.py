from api import db


class ModeloLaudoModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "modelo_laudo"

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_estabelecimento_saude = db.Column(db.Integer, nullable=True)
    identificador_modalidade = db.Column(db.Integer, nullable=True)
    identificador_profissional_saude = db.Column(db.Integer, nullable=True)
    texto = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)