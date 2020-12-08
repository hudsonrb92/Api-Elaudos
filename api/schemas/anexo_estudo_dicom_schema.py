from marshmallow import fields


from api import ma
from ..models import anexo_estudo_dicom_model


class AnexoEstudoDicomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = anexo_estudo_dicom_model.AnexoEstudoDicomModel
        fields = ("identificador", "identificador_estudo_dicom", "nome_arquivo", "descricao", "conteudo_arquivo")
