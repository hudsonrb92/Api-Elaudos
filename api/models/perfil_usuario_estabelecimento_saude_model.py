from api import db


class PerfilUsuarioEstabelecimentoSaudeModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "perfil_usuario_estabelecimento_saude"

    identificador_perfil = db.Column(db.String, nullable=False)
    identificador_usuario = db.Column(
        db.Integer, db.ForeignKey("public.usuario.identificador"), nullable=False
    )
    identificador_estabelecimento_saude = db.Column(db.Integer, nullable=False)
    data_inicial = db.Column(db.Date, nullable=False, primary_key=True)
    data_final = db.Column(db.Date, nullable=True)