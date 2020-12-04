from marshmallow import fields
from api import ma
from ..models import usuario_model


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.UsuarioModel
        fields = ("login", "senha", "identificador_pessoa", "ativo")

    login = fields.String(required=True)
    senha = fields.String(required=True)
    identificador_pessoa = fields.Integer(required=False)
    ativo = fields.Boolean(required=False)
