from api import db


class TipoConselhoTrabalhoModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "tipo_conselho_trabalho"

    identificador = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)