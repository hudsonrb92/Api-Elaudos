from api import db


class PessoaModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'pessoa'

    identificador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    identificador_sexo = db.Column(db.Integer, nullable=True)
    identificador_raca = db.Column(db.Integer, nullable=True)
    ativa = db.Column(db.Boolean, nullable=False)
