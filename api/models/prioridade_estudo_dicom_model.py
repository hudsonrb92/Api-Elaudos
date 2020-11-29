from api import db


class PrioridadeEstudoDicomModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = "prioridade_estudo_dicom"

    identificador = db.Column(db.String, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    ordenacao = db.Column(db.Integer, nullable=False)
    estudo_dicom = db.relationship("EstudoDicomModel", back_populates="prioridade_estudo_dicom", uselist=False)