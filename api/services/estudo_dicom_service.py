from sqlalchemy import or_

from ..models import estudo_dicom_model


def listar_estudos():
    estudos = estudo_dicom_model.EstudoDicomModel.query.all()
    return estudos


def listar_estudo_por_id(identificador):
    estudo = estudo_dicom_model.EstudoDicomModel.query.filter_by(
        identificador=identificador
    ).first()
    return estudo


def listar_estudo_por_studyinstanceuid(studyinstanceuid):
    estudo = estudo_dicom_model.EstudoDicomModel.query.filter_by(
        studyinstanceuid=studyinstanceuid
    ).first()
    return estudo


def listar_estudos_sem_laudos(identificador_estabelecimento_saude):
    estudos = (
        estudo_dicom_model.EstudoDicomModel.query.filter(
            or_(
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "N",
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "C",
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "R",
            )
        )
        .filter_by(
            identificador_estabelecimento_saude=identificador_estabelecimento_saude
        )
        .filter(
            or_(
                estudo_dicom_model.EstudoDicomModel.situacao == "V",
                estudo_dicom_model.EstudoDicomModel.situacao == "P",
            )
        )
        .all()
    )
    return estudos
