from api import ma
from ..models import estado_model
from marshmallow import fields


class EstadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = estado_model.EstadoModel
        fields = ("nome", "sigla")

    identificador = fields.Integer(required=True)
    nome = fields.String(required=True)
    codigo_ibge = fields.String(required=True)
    identificador_pais = fields.Integer(required=True)
    ativo = fields.Boolean(required=True)
    sigla = fields.String(required=True)
