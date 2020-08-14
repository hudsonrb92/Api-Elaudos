from api import ma
from ..models import laudo_estudo_dicom_model


class LaudoEstudoDicomSchema(ma.ModelSchema):
    class Meta:
        model = laudo_estudo_dicom_model.LaudoEstudoDicomModel
        fields = ("identificador", "identificador_estudo_dicom", "data_hora_emissao",
                  "texto",
                  "data_hora_revisao", "situacao", "numero_exames_relacionados", "identificador_profissional_saude",
                  "identificador_profissional_saude_revisor",
                  "situacao_envio_his", "integrado")