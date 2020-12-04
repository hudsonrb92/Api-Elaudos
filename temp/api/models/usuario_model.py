from api import db
from hashlib import md5
from .pessoa_model import PessoaModel


class UsuarioModel(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'usuario'

    identificador = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    administrador = db.Column(db.Boolean, nullable=False)
    identificador_pessoa = db.Column(db.Integer, db.ForeignKey('public.pessoa.identificador'), nullable=False)
    pessoa = db.relationship(PessoaModel, backref=db.backref("usuario", lazy="dynamic"))
    ativo = db.Column(db.Boolean, nullable=False)

    def ver_senha(self, senha):
        senha = md5(senha.encode())
        senha = senha.hexdigest()
        if self.senha == senha:
            return True
        else:
            return False
