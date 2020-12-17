from sqlalchemy import or_

from ..models import estudo_dicom_model, integracao_tasy_model
from api import db, logger

itm = integracao_tasy_model.IntegracaoTasyModel


def listar_estudos():
    logger.info("Listando exames em geral")
    estudos = estudo_dicom_model.EstudoDicomModel.query.all()
    return estudos


def listar_estudo_por_id(identificador):
    logger.info(f"Listando exame por identificador {identificador}")
    estudo = estudo_dicom_model.EstudoDicomModel.query.filter_by(identificador=identificador).first()
    return estudo


def listar_estudo_por_studyinstanceuid(studyinstanceuid):
    logger.info(f"Lista exame por uid {studyinstanceuid}")
    estudo = estudo_dicom_model.EstudoDicomModel.query.filter_by(studyinstanceuid=studyinstanceuid).first()
    return estudo


def listar_estudos_sem_laudos(identificador_estabelecimento_saude):
    logger.info(f"Verificando exames sem laudo id_estab:{identificador_estabelecimento_saude}")
    estudos = (
        estudo_dicom_model.EstudoDicomModel.query.filter(
            or_(
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "N",
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "C",
                estudo_dicom_model.EstudoDicomModel.situacao_laudo == "R",
            )
        )
        .filter_by(identificador_estabelecimento_saude=identificador_estabelecimento_saude)
        .filter(
            or_(
                estudo_dicom_model.EstudoDicomModel.situacao == "V",
                estudo_dicom_model.EstudoDicomModel.situacao == "P",
            )
        )
        .all()
    )
    return estudos


def insert_on_taas(estudo):
    edm = estudo_dicom_model.EstudoDicomModel
    exame = check_if_already_exists(estudo)
    if not exame:
        try:
            estudo_model = edm(
                studyinstanceuid=estudo.studyinstanceuid,
                accessionnumber=estudo.accessionnumber,
                patientname=estudo.patientname,
                patientid=estudo.patientid,
                patientsex=estudo.patientsex,
                patientbirthdate=estudo.patientbirthdate,
                studydescription=estudo.studydescription,
                modalitiesinstudy=estudo.modalitiesinstudy,
                imagens_disponiveis=estudo.imagens_disponiveis,
                origem_registro=estudo.origem_registro,
                identificador_estabelecimento_saude=estudo.identificador_estabelecimento_saude,
                studydate=estudo.studydate,
                studytime=estudo.studytime,
                situacao_laudo=estudo.situacao_laudo,
                identificador_prioridade_estudo_dicom=estudo.identificador_prioridade_estudo_dicom,
                numero_exames_ris=estudo.numero_exames_ris,
                situacao=estudo.situacao,
                identificador_profissional_saude_solicitante=estudo.medico_sol,
                identificador_profissional_saude_direcionado=estudo.medico_dir,
            )
            db.session.add(estudo_model)
            db.session.commit()
            logger.info(f"Exame inserido no nimbus_taas {estudo.accessionnumber} - {estudo.patientid}")
            return estudo_model
        except Exception as expt:
            db.session.rollback()
            logger.error(f"Um erro ocorreu ao tentar cadastrar {estudo.accessionnumber} {expt}")
            raise Exception(f"Um erro ocorreu ao tentar cadastrar {expt} {estudo.accessionnumber}")
    else:
        raise Exception("Erro ao tentar fazer o cadastro.")


def check_if_already_exists(estudo):
    logger.info(f"Verificando se exame já existe id:{estudo.patientid}  accession: {estudo.accessionnumber}")
    edm = estudo_dicom_model.EstudoDicomModel
    exame = (
        edm.query.filter(edm.patientid == estudo.patientid)
        .filter(edm.patientbirthdate == estudo.patientbirthdate)
        .filter(edm.accessionnumber == estudo.accessionnumber)
        .first()
    )
    return exame


def invalida_exames(requisicoes: list) -> estudo_dicom_model.EstudoDicomModel:
    logger.info(f"Invalidando lista de exames {requisicoes}")
    edm = estudo_dicom_model.EstudoDicomModel
    sttms = itm.query.join(edm).filter(edm.accessionnumber.in_(requisicoes))
    exames = sttms.all()
    edm.query.filter(
        edm.accessionnumber.in_(requisicoes),
        edm.imagens_disponiveis == False,
        edm.situacao_laudo == "N",
        edm.situacao == "V",
    ).update({edm.situacao: "I"}, synchronize_session=False)
    db.session.commit()
    return exames
