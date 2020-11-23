from api import db
from ..models.integracao_tasy_model import IntegracaoTasyModel as itm
from ..models.estudo_dicom_model import EstudoDicomModel as edm


def busca_por_prescricao(nr_prescricao, nr_sequencia):
    exames = itm.query.join(edm).filter(
        itm.nr_prescricao == nr_prescricao).filter(
            itm.nr_sequencia == nr_sequencia).first()
    return exames
