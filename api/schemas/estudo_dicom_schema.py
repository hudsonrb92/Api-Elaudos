from marshmallow import fields

from api import ma
from ..models import estudo_dicom_model
from marshmallow_sqlalchemy import ModelSchema


class EstudoDicomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = estudo_dicom_model.EstudoDicomModel
        fields = (
            "identificador",
            "patientname",
            "identificador_estabelecimento_saude",
            "chave_primaria_origem",
            "patientbirthdate",
            "studyinstanceuid",
            "imagens_disponiveis",
            "studytime",
            "patientid",
            "accessionnumber",
            "studydescription",
            "modalitiesinstudy",
            "data_hora_inclusao",
            "data_hora_ultima_alteracao",
            "situacao_laudo",
            "numero_exames_ris",
            "studyid",
            "patientsex",
            "numberofinstances",
            "situacao",
            "nome_mae",
            "data_hora_validacao",
            "anexo_estudo_dicom",
            "anotacao_estudo_dicom",
        )

    identificador = fields.Integer(required=True)
    patientname = fields.String(required=False)
    identificador_estabelecimento_saude = fields.Integer(required=False)
    chave_primaria_origem = fields.Integer(required=False)
    studyinstanceuid = fields.String(required=True)
    studytime = fields.String(required=False)
    patientid = fields.String(required=False)
    accessionnumber = fields.String(required=False)
    studydescription = fields.String(required=False)
    modalitiesinstudy = fields.String(required=False)
    data_hora_inclusao = fields.DateTime(required=False)
    data_hora_ultima_alteracao = fields.DateTime(required=False)
    situacao_laudo = fields.String(required=False)
    numero_exames_ris = fields.Integer(required=False)
    studyid = fields.String(required=False)
    integrado = fields.Boolean(required=True)
    patientsex = fields.String(required=False)
    patientbirthdate = fields.String(required=False)
    nome_operador = fields.String(required=False)
    numberofseries = fields.Integer(required=False)
    numberofinstances = fields.Integer(required=False)
    situacao = fields.String(required=False)
    nome_mae = fields.String(required=False)
    imagens_disponiveis = fields.Boolean(required=False)
    origem_registro = fields.String(required=False)
    data_hora_validacao = fields.DateTime(required=False)
    chave_primaria_origem_worklist = fields.Integer(required=False)
