from api import db, logger
from ..models.laudo_estudo_dicom_model import LaudoEstudoDicomModel as lem
from ..models.integracao_tasy_model import IntegracaoTasyModel as itm
from ..models.estudo_dicom_model import EstudoDicomModel as edm
from base64 import b64encode


def listar_laudos(identificador_estabelecimento_saude):
    sttmnt = (
        lem.query.filter(
            lem.identificador_estudo_dicom == itm.identificador_estudo_dicom,
            lem.identificador_estudo_dicom == edm.identificador,
        )
        .filter(edm.accessionnumber != None)
        .filter(lem.integrado == False)
    )
    estudos = sttmnt.all()
    return estudos


def listar_estudo_por_id(identificador):
    laudo = lem.query.filter_by(identificador=identificador).join(edm).first()
    return laudo


def update_to_integrado(laudo):
    laudo.integrado = True
    logger.info(f"Exame alterado para integrado {laudo.identificador_estudo_dicom} - {laudo.integrado}")
    db.session.commit()


def get_pdf(identificador: int) -> b64encode:
    laudo = lem.query.filter_by(identificador=identificador).first()
    if not laudo:
        raise Exception("Error, laudo not found")
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
