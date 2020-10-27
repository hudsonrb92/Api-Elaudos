from api import db


class EstabelecimentoSaudeContato(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "estabelecimento_saude_contato"

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_estabelecimento_saude = db.Column(
        db.Integer,
        db.ForeignKey("public.estabelecimento_saude.identificador"),
        nullable=False,
    )
    identificador_tipo_contato = db.Column(db.String, nullable=False)
    contato = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)