from api import db
from ..models.laudo_estudo_dicom_model import LaudoEstudoDicomModel as lem
from ..models.estudo_dicom_model import EstudoDicomModel
from base64 import b64encode


def listar_laudos(identificador_estabelecimento_saude):
    estudos = (
        lem.query.filter_by(integrado=False)
        .join(EstudoDicomModel)
        .filter(
            EstudoDicomModel.identificador_estabelecimento_saude == identificador_estabelecimento_saude,
            EstudoDicomModel.situacao == "V",
            EstudoDicomModel.accessionnumber != None,
        )
        .all()
    )
    return estudos


def listar_estudo_por_id(identificador):
    laudo = lem.query.filter_by(identificador=identificador).join(EstudoDicomModel).first()
    return laudo


def update_to_integrado(laudo):
    laudo.integrado = True
    db.session.commit()


def get_pdf(identificador: int) -> b64encode:
    laudo = lem.query.filter_by(identificador=identificador).first()
    if not laudo:
        raise Exception(f"Error, laudo not found")
    pdf_name = f"{laudo.identificador}-{laudo.data_hora_emissao}"
    dir_name = "/data/integracao/laudos/"

    try:
        pdf = open(f"{dir_name}{pdf_name}", "rb").read()
    except FileNotFoundError as e:
        raise Exception(f"{FileNotFoundError} {e}")

    return b64encode(pdf)


def get_laudo_id_estudo(identificador):
    laudo = lem.query.filter(lem.identificador_estudo_dicom == identificador)
    return laudo.first()


def update_integrado_id_estudo(identificador):
    sttmt = lem.query.filter(lem.identificador_estudo_dicom == identificador)
    exame = sttmt.first()
    if exame:
        sttmt.update({lem.integrado: True}, synchronize_session=False)
    return exame
