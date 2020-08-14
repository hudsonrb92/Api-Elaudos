from api import db
from .pessoa_model import PessoaModel


class ProfissionalSaudeModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'profissional_saude'

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_pessoa = db.Column(db.Integer, db.ForeignKey('public.pessoa.identificador'), nullable=False)
    pessoa = db.relationship(PessoaModel, backref=db.backref("public.profissional_saude", lazy="dynamic"))
    identificador_tipo_conselho_trabalho = db.Column(db.Integer, nullable=False)
    identificador_estado_conselho_trabalho = db.Column(db.Integer, db.ForeignKey('public.estado.identificador'),
                                                       nullable=False)
    registro_conselho_trabalho = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    assinatura_digitalizada = db.Column(db.LargeBinary(16), nullable=True)

    executor_laudo = db.relationship('LaudoEstudoDicomModel',
                                     foreign_keys='LaudoEstudoDicomModel.identificador_profissional_saude',
                                     backref='executor_laudo', lazy='dynamic')

    revisor_laudo = db.relationship('LaudoEstudoDicomModel',
                                    foreign_keys='LaudoEstudoDicomModel.identificador_profissional_saude_revisor',
                                    backref='revisor_laudo', lazy='dynamic')

    anotacao_estudo_dicom = db.relationship("AnotacaoEstudoDicomModel", back_populates="profissional_saude")
