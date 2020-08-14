from api import db
from .estabelecimento_saude_model import EstabelecimentoSaudeModel
from .laudo_estudo_dicom_model import LaudoEstudoDicomModel
from .anexo_estudo_dicom_model import AnexoEstudoDicomModel
from .anotacao_estudo_dicom_model import AnotacaoEstudoDicomModel


class EstudoDicomModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = 'estudo_dicom'

    identificador = db.Column(db.Integer, primary_key=True)

    identificador_estabelecimento_saude = db.Column(db.Integer,
                                                    db.ForeignKey('public.estabelecimento_saude.identificador'),
                                                    nullable=False)
    estabelecimento_saude = db.relationship(EstabelecimentoSaudeModel,
                                            backref=db.backref('estudo_dicom', lazy='dynamic'))
    laudo_estudo_dicom = db.relationship(LaudoEstudoDicomModel, back_populates="estudo_dicom")
    anotacao_estudo_dicom = db.relationship(AnotacaoEstudoDicomModel, back_populates="estudo_dicom")
    anexo_estudo_dicom = db.relationship(AnexoEstudoDicomModel, back_populates="estudo_dicom")

    identificador_convenio = db.Column(db.Integer(), db.ForeignKey('convenio.identificador'), nullable=True)

    identificador_prioridade_estudo_dicom = db.Column(db.Integer(),
                                                      db.ForeignKey('prioridade_estudo_dicom.identificador'),
                                                      nullable=False)

    identificador_profissional_saude_direcionado = db.Column(db.Integer(),
                                                             db.ForeignKey('public.profissional_saude.identificador'),
                                                             nullable=True)

    identificador_profissional_saude_operador = db.Column(db.Integer(),
                                                          db.ForeignKey('public.profissional_saude.identificador'),
                                                          nullable=True)

    identificador_profissional_saude_solicitante = db.Column(db.Integer(),
                                                             db.ForeignKey('public.profissional_saude.identificador'),
                                                             nullable=True)

    identificador_profissional_saude_validacao = db.Column(db.Integer(),
                                                           db.ForeignKey('public.profissional_saude.identificador'),
                                                           nullable=True)

    chave_primaria_origem = db.Column(db.Integer, nullable=True)

    studyinstanceuid = db.Column(db.String, nullable=False)

    studydate = db.Column(db.DateTime, nullable=False)

    studytime = db.Column(db.String, nullable=True)

    patientid = db.Column(db.String, nullable=True)

    patientname = db.Column(db.String, nullable=False)

    accessionnumber = db.Column(db.String, nullable=True)

    studydescription = db.Column(db.String, nullable=True)

    modalitiesinstudy = db.Column(db.String, nullable=True)

    data_hora_inclusao = db.Column(db.DateTime, nullable=False)

    data_hora_ultima_alteracao = db.Column(db.DateTime, nullable=True)

    situacao_laudo = db.Column(db.String, nullable=False)

    numero_exames_ris = db.Column(db.Integer, nullable=False)

    studyid = db.Column(db.String, nullable=True)

    patientsex = db.Column(db.String, nullable=True)

    patientbirthdate = db.Column(db.String, nullable=True)

    nome_operador = db.Column(db.String, nullable=True)

    numberofseries = db.Column(db.Integer, nullable=True)

    numberofinstances = db.Column(db.Integer, nullable=True)

    situacao = db.Column(db.String, nullable=False)

    nome_mae = db.Column(db.String, nullable=True)

    imagens_disponiveis = db.Column(db.Boolean, nullable=False)

    origem_registro = db.Column(db.String, nullable=False)

    data_hora_validacao = db.Column(db.DateTime, nullable=True)

    chave_primaria_origem_worklist = db.Column(db.Integer, nullable=True)
