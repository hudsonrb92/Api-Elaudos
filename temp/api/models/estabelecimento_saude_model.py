from api import db
from .endereco_model import EnderecoModel


class EstabelecimentoSaudeModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'estabelecimento_saude'

    identificador = db.Column(db.Integer, primary_key=True)
    numero_cnes = db.Column(db.Integer, nullable=True)
    numero_cnpj = db.Column(db.Integer, nullable=True)
    razao_social = db.Column(db.String, nullable=False)
    nome_fantasia = db.Column(db.String, nullable=False)
    identificador_endereco = db.Column(db.Integer, db.ForeignKey('public.endereco.identificador'), nullable=False)
    endereco = db.relationship(EnderecoModel, backref=db.backref("estabelecimento_saude", lazy="dynamic"))
    ativo = db.Column(db.Boolean, nullable=False)
    logotipo = db.Column(db.String, nullable=True)
    url_resultado_exames = db.Column(db.String, nullable=True)
