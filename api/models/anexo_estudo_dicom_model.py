from api import db


class AnexoEstudoDicomModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = 'anexo_estudo_dicom'

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_estudo_dicom = db.Column(db.ForeignKey('radius_taas.estudo_dicom.identificador'))
    nome_arquivo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=True)
    conteudo_arquivo = db.Column(db.LargeBinary(16), nullable=False)
    estudo_dicom = db.relationship("EstudoDicomModel", back_populates="anexo_estudo_dicom")
