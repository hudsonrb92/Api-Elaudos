from api import db
from .profissional_saude_model import ProfissionalSaudeModel


class AnotacaoEstudoDicomModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = 'anotacao_estudo_dicom'

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_estudo_dicom = db.Column(db.ForeignKey('radius_taas.estudo_dicom.identificador'), nullable=False)
    data_hora_registro = db.Column(db.DateTime, nullable=False)
    identificador_profissional_saude = db.Column(db.ForeignKey('public.profissional_saude.identificador'),
                                                 nullable=True)
    texto = db.Column(db.Text, nullable=False)
    origem = db.Column(db.String, nullable=False)
    estudo_dicom = db.relationship("EstudoDicomModel", back_populates="anotacao_estudo_dicom")
    profissional_saude = db.relationship(ProfissionalSaudeModel, back_populates="anotacao_estudo_dicom")
