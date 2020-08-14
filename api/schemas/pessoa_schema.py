from api import ma
from ..models import pessoa_model
from marshmallow import fields


class PessoaSchema(ma.ModelSchema):
    class Meta:
        model = pessoa_model.PessoaModel
        fields = ("identificador", "nome", "data_nascimento",
                  "identificador_sexo", "identificador_raca", "ativa")

    identificador = fields.Integer(required=True)
    nome = fields.String(required=True)
    identificador_sexo = fields.Integer()
    identificador_raca = fields.Integer()
    data_nascimento = fields.Date()
    ativa = fields.Boolean(required=True)
