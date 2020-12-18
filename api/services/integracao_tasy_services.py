from ..entidades import estudo_dicom, medicos
from ..models import integracao_tasy_model, estudo_dicom_model
from ..services.tools import modalidade
from ..services.medicos_services import cadastra_medico
from ..services.estudo_dicom_service import insert_on_taas
from api import db, logger
from uuid import uuid4

itm = integracao_tasy_model.IntegracaoTasyModel
medico = medicos.Medicos
estudo = estudo_dicom.EstudoDicom
estmod = estudo_dicom_model.EstudoDicomModel


def inserir_exame(exame):
    logger.info(f"Cadastrando exame {exame.nr_prescricao}{exame.nr_sequencia}")
    if verifica_se_ja_existe(exame):
        return False
    # Verifica se médico existe, se não existir é criado.
    try:
        medico_entidade = medico(crm=exame.nr_crm, uf=exame.uf_medico, nome=exame.nm_medico)
        medico_novo = cadastra_medico(medico_entidade)
    except Exception as excp:
        logger.error(f"Um erro ocorreu ao tentar cadastrar medico {excp}")

    identificador_solicitante = medico_novo.identificador if medico_novo else None
    estudo_entidade = estudo(
        patientname=exame.nm_social,
        patientbirthdate=exame.dt_nascimento,
        patientid=exame.nr_prontuario,
        studydescription=exame.ds_procedimento[0:64],
        studydate=exame.dt_liberacao,
        accessionnumber=f"{exame.nr_prescricao}{exame.nr_sequencia}",
        modalitiesinstudy=modalidade(exame.ds_local_exec),
        studytime=exame.dt_liberacao[-8:],
        patientsex=exame.ie_sexo,
        medico_sol=identificador_solicitante,
        studyinstanceuid=str(uuid4()),
    )
    estudo_novo = insert_on_taas(estudo_entidade)
    identificador_novo_estudo = estudo_novo.identificador if estudo_novo else None
    exame_novo = itm(
        nr_atendimento=exame.nr_atendimento,
        nr_prescricao=exame.nr_prescricao,
        nr_sequencia=exame.nr_sequencia,
        nr_seq_interno=exame.nr_seq_interno,
        nr_acess_number=exame.nr_acess_number,
        cd_proced_tasy=exame.cd_proced_tasy,
        cd_proced_integracao=exame.cd_proced_integracao,
        cd_proced_tasy_lado=exame.cd_proced_tasy_lado,
        ds_procedimento=exame.ds_procedimento,
        ie_lado=exame.ie_lado,
        ie_urgencia=exame.ie_urgencia,
        dt_prev_execucao=exame.dt_prev_execucao,
        cd_setor_paciente=exame.cd_setor_paciente,
        cd_estabelecimento=exame.cd_estabelecimento,
        nm_pessoa_fisica=exame.nm_pessoa_fisica,
        dt_prescricao=exame.dt_prescricao,
        cd_setor_execucao=exame.cd_setor_execucao,
        dt_liberacao=exame.dt_liberacao,
        cd_software_integracao=exame.cd_software_integracao,
        cd_estab_terceiro=exame.cd_estab_terceiro,
        cd_paciente=exame.cd_paciente,
        cd_prescritor=exame.cd_prescritor,
        ie_sexo=exame.ie_sexo,
        dt_nascimento=exame.dt_nascimento,
        cd_integracao_proc_interno=exame.cd_integracao_proc_interno,
        qt_altura_cm=exame.qt_altura_cm,
        qt_idade_pac=exame.qt_idade_pac,
        qt_peso=exame.qt_peso,
        nr_crm_prescritor=exame.nr_crm_prescritor,
        cd_modalidade_proc=exame.cd_modalidade_proc,
        uf_crm_prescritor=exame.uf_crm_prescritor,
        nr_cpf_paciente=exame.nr_cpf_paciente,
        qt_prescrito=exame.qt_prescrito,
        nr_identidade_paciente=exame.nr_identidade_paciente,
        nr_prontuario_paciente=exame.nr_prontuario_paciente,
        ds_endereco_paciente=exame.ds_endereco_paciente,
        nr_endereco_paciente=exame.nr_endereco_paciente,
        ds_bairro_paciente=exame.ds_bairro_paciente,
        ds_municipio_paciente=exame.ds_municipio_paciente,
        uf_paciente=exame.uf_paciente,
        cd_cep_paciente=exame.cd_cep_paciente,
        nr_telefone_paciente=exame.nr_telefone_paciente,
        cd_convenio=exame.cd_convenio,
        ds_categoria_convenio=exame.ds_categoria_convenio,
        ds_convenio=exame.ds_convenio,
        cd_cgc=exame.cd_cgc,
        nr_seq_motivo_atend=exame.nr_seq_motivo_atend,
        ds_motivo_atend=exame.ds_motivo_atend,
        ds_motivo_suspensao=exame.ds_motivo_suspensao,
        cd_pessoa_fisica=exame.cd_pessoa_fisica,
        cd_procedimento=exame.cd_procedimento,
        cd_tipo_procedimento=exame.cd_tipo_procedimento,
        qt_procedimento=exame.qt_procedimento,
        dt_atualizacao=exame.dt_atualizacao,
        nm_usuario=exame.nm_usuario,
        ds_observacao=exame.ds_observacao,
        ie_origem_proced=exame.ie_origem_proced,
        ds_dado_clinico=exame.ds_dado_clinico,
        ie_suspenso=exame.ie_suspenso,
        cd_setor_atendimento=exame.cd_setor_atendimento,
        cd_medico=exame.cd_medico,
        dt_liberacao_medico=exame.dt_liberacao_medico,
        ie_recem_nato=exame.ie_recem_nato,
        nm_paciente=exame.nm_paciente,
        nr_cpf=exame.nr_cpf,
        nr_prontuario=exame.nr_prontuario,
        nm_medico=exame.nm_medico,
        nr_crm=exame.nr_crm,
        cd_categoria=exame.cd_categoria,
        cd_usuario_convenio=exame.cd_usuario_convenio,
        cd_material_exame=exame.cd_material_exame,
        ds_material_especial=exame.ds_material_especial,
        ie_amostra_entregue=exame.ie_amostra_entregue,
        ds_horarios=exame.ds_horarios,
        nr_seq_exame=exame.nr_seq_exame,
        ds_endereco=exame.ds_endereco,
        nr_endereco=exame.nr_endereco,
        ds_complemento=exame.ds_complemento,
        ds_bairro=exame.ds_bairro,
        ds_municipio=exame.ds_municipio,
        sg_estado=exame.sg_estado,
        nr_telefone=exame.nr_telefone,
        cd_cep=exame.cd_cep,
        ds_setor_paciente=exame.ds_setor_paciente,
        cd_unidade=exame.cd_unidade,
        ie_executar_leito=exame.ie_executar_leito,
        ds_modalidade=exame.ds_modalidade,
        na_accessionnumber=exame.na_accessionnumber,
        ie_tipo_atendimento=exame.ie_tipo_atendimento,
        nr_seq_proc_interno=exame.nr_seq_proc_interno,
        cd_plano_convenio=exame.cd_plano_convenio,
        cd_plano=exame.cd_plano,
        cd_agenda=exame.cd_agenda,
        ds_agenda=exame.ds_agenda,
        cd_procedencia=exame.cd_procedencia,
        ds_procedencia=exame.ds_procedencia,
        cd_compl_conv=exame.cd_compl_conv,
        dt_validade_carteira=exame.dt_validade_carteira,
        dt_resultado=exame.dt_resultado,
        ds_senha=exame.ds_senha,
        nr_cpf_medico=exame.nr_cpf_medico,
        cd_estab_atend=exame.cd_estab_atend,
        cd_estab_prescr=exame.cd_estab_prescr,
        dt_entrada=exame.dt_entrada,
        ds_tipo_atendimento=exame.ds_tipo_atendimento,
        ds_observacao_pf=exame.ds_observacao_pf,
        ds_unidade_atend=exame.ds_unidade_atend,
        ds_plano=exame.ds_plano,
        dt_admissao_hosp=exame.dt_admissao_hosp,
        uf_medico=exame.uf_medico,
        ds_local=exame.ds_local,
        ds_local_exec=exame.ds_local_exec,
        nm_medico_aten_ext=exame.nm_medico_aten_ext,
        crm_medico_aten_ext=exame.crm_medico_aten_ext,
        nm_social=exame.nm_social,
        ds_email=exame.ds_email,
        identificador_estudo_dicom=identificador_novo_estudo,
    )
    db.session.add(exame_novo)
    db.session.commit()
    return exame_novo


def verifica_se_ja_existe(exame):
    existe = itm.query.filter(itm.nr_prescricao == exame.nr_prescricao, itm.nr_sequencia == exame.nr_sequencia).first()
    return existe


def busca_por_prescricao(accession):
    existe = (
        itm.query.filter(itm.identificador_estudo_dicom == estmod.identificador)
        .filter(estmod.accessionnumber == accession)
        .first()
    )
    print(existe)
    return existe


def listar_exames_iniciados():
    exams = (
        itm.query.join(estmod, itm.identificador_estudo_dicom == estmod.identificador)
        .filter(itm.exame_iniciado == False)
        .filter(estmod.imagens_disponiveis == True)
        .all()
    )
    return exams


def exame_iniciado_to_true(nr_prescicao: str, nr_sequencia: str) -> itm:
    logger.info("Alterando para integrado True no banco.")
    sttmnt = itm.query.filter(itm.nr_prescricao == nr_prescicao, itm.nr_sequencia == nr_sequencia)
    exame = sttmnt.first()
    sttmnt.update({itm.exame_iniciado: True}, synchronize_session=False)
    db.session.commit()
    logger.info("Retornando.")
    return exame


def altera_para_iniciado(nr_accession):
    itm.query.join(estmod, itm.identificador_estudo_dicom == estmod.identificador).filter(
        estmod.accessionnumber == nr_accession
    ).first().update({itm.exame_iniciado: True})


def busca_exames_worklist_false():
    exames = itm.query.filter(itm.criado_worklist == False).all()
    return exames


def altera_criado_worklist_true(nr_prescricao, nr_sequencia):
    sttmt = itm.query.filter(itm.nr_sequencia == nr_sequencia, itm.nr_prescricao == nr_prescricao)
    sttmt.update({itm.criado_worklist: True}, synchronize_session=False)
    db.session.commit()
    return sttmt.first()


def altera_integrado_tasy(accession):
    sttmt = itm.query.filter(itm.nr_prescricao == accession[:-1], itm.nr_sequencia == accession[-1:])
    sttmt.update({itm.criado_worklist: True}, synchronize_session=False)
    db.session.commit()
    return sttmt.first()