from marshmallow import fields


from api import ma
from .estado_schema import EstadoSchema
from .pessoa_schema import PessoaSchema
from ..models import profissional_saude_model


class ProfissionalSaudeModelSchema(ma.ModelSchema):
    class Meta:
        model = profissional_saude_model.ProfissionalSaudeModel
        fields = ("registro_conselho_trabalho", "ativo", "pessoa",
                  "estado_conselho_trabalho", "assinatura_digitalizada")

    identificador = fields.Integer(required=True)
    identificador_pessoa = fields.Integer(required=True)
    pessoa = fields.Nested(PessoaSchema)
    assinatura_digitalizada = fields.String()
    estado_conselho_trabalho = fields.Nested(EstadoSchema)
    identificador_tipo_conselho_trabalho = fields.Integer(required=True)
    identificador_estado_conselho_trabalho = fields.Integer(required=True)
    registro_conselho_trabalho = fields.String()
    ativo = fields.Boolean(required=True)
