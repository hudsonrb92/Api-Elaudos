from api import db


class CidadeModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "cidade"

    identificador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    codigo_ibge = db.Column(db.Integer, nullable=False)
    identificador_estado = db.Column(
        db.Integer, db.ForeignKey("public.estado.identificador"), nullable=False
    )
    ativa = db.Column(db.Boolean, nullable=False)