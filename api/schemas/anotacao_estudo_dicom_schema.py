from marshmallow import fields


from api import ma
from ..models import anotacao_estudo_dicom_model
from .profissional_saude_schema import ProfissionalSaudeModelSchema

class AnotacaoEstudoDicomSchema(ma.ModelSchema):
    class Meta:
        model = anotacao_estudo_dicom_model.AnotacaoEstudoDicomModel
        fields = ("identificador", "identificador_estudo_dicom", "data_hora_registro",
                  "identificador_profissional_saude", "texto", "origem", "profissional_saude")

    profissional_saude = fields.Nested(ProfissionalSaudeModelSchema, exclude=("assinatura_digitalizada",))
