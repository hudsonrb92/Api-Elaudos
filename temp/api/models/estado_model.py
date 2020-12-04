from api import db
from .profissional_saude_model import ProfissionalSaudeModel


class EstadoModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'estado'

    identificador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    codigo_ibge = db.Column(db.Integer, nullable=False)
    identificador_pais = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    sigla = db.Column(db.String, nullable=False)
    estado_conselho_trabalho = db.relationship(ProfissionalSaudeModel,
                                               foreign_keys='ProfissionalSaudeModel\
                                               .identificador_estado_conselho_trabalho',
                                               backref='estado_conselho_trabalho', lazy='dynamic')
