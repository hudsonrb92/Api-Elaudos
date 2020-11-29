from api import db

class ConvenioModel(db.Model):
    __table_args__ = {'schema': 'radius_taas'}
    __tablename__ = "convenio"

    identificador = db.Column(db.Integer, primary_key=True, nullable=False)
    razao_social = db.Column(db.String, nullable=True)
    nome_fantasia = db.Column(db.String, nullable=False)
    numero_cnpj = db.Column(db.String, nullable=True)
    numero_registro_ans = db.Column(db.Integer, nullable=False)
    identificador_estabelecimento_saude = db.Column(db.Integer, db.ForeignKey(
        'public.estabelecimento_saude.identificador'), nullable=False)
    identificador_usuario = db.Column(db.Integer, nullable=True)
    estudo_dicom = db.relationship("EstudoDicomModel", back_populates="convenio", uselist=False)