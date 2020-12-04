from api import db
from ..models.laudo_estudo_dicom_model import LaudoEstudoDicomModel as lem
from ..models.estudo_dicom_model import EstudoDicomModel
from base64 import b64encode


def listar_laudos(identificador_estabelecimento_saude):
    estudos = lem.query.filter_by(integrado=False)\
        .join(EstudoDicomModel)\
        .filter_by(
        identificador_estabelecimento_saude=identificador_estabelecimento_saude
    ).filter_by(situacao='V').all()
    return estudos


def listar_estudo_por_id(identificador):
    laudo = lem.query.filter_by(identificador=identificador).join(EstudoDicomModel).first()
    return laudo


def update_to_integrado(laudo):
    laudo.integrado = True
    db.session.commit()


def get_pdf(identificador: int) -> 'pdf in base64':
    laudo = lem.query.filter_by(identificador=identificador).first()
    if not laudo:
        raise Exception(f'Error, laudo not found')
    pdf_name = f'{laudo.identificador}-{laudo.data_hora_emissao}'
    dir_name = '/data/integracao/laudos/'

    try:
        pdf = open(f'{dir_name}{pdf_name}', 'rb').read()
    except FileNotFoundError as e:
        raise Exception(f'{FileNotFoundError} {e}')

    return b64encode(pdf)

