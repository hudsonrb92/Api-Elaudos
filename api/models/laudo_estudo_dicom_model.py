from api import db


class LaudoEstudoDicomModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = 'laudo_estudo_dicom'

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_estudo_dicom = db.Column(db.Integer, db.ForeignKey('radius_taas.estudo_dicom.identificador'),
                                           nullable=False)
    estudo_dicom = db.relationship("EstudoDicomModel", back_populates="laudo_estudo_dicom")
    data_hora_emissao = db.Column(db.DateTime, nullable=False)
    identificador_profissional_saude = db.Column(db.Integer, db.ForeignKey('public.profissional_saude.identificador'),
                                                 nullable=True)
    identificador_profissional_saude_revisor = db.Column(db.Integer,
                                                         db.ForeignKey('public.profissional_saude.identificador'),
                                                         nullable=True)
    texto = db.Column(db.Text, nullable=False)
    data_hora_revisao = db.Column(db.DateTime, nullable=False)
    situacao = db.Column(db.String, nullable=False)
    numero_exames_relacionados = db.Column(db.Integer, nullable=True)
    situacao_envio_his = db.Column(db.String, nullable=False)
    integrado = db.Column(db.Boolean, nullable=False)
