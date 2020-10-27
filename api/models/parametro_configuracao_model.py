from api import db


class ParametroConfiguracaoModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "parametro_configuracao"

    identificador_estabelecimento_saude = db.Column(db.Integer, primary_key=True)
    chave = db.Column(db.String, nullable=False)
    valor = db.Column(db.String, nullable=False)