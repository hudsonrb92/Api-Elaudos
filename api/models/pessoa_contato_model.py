from api import db


class PessoaContatoModel(db.Model):
    __table_args__ = {"schema": "public"}
    __tablename__ = "pessoa_contato"

    identificador = db.Column(db.Integer, primary_key=True)
    identificador_pessoa = db.Column(
        db.Integer, db.ForeignKey("public.pessoa.identificador"), nullable=False
    )
    identificador_tipo_contato = db.Column(db.String, nullable=False)
    contato = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)