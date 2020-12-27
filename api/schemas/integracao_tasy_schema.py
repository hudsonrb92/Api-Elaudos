from marshmallow import fields
from api import ma
from ..models import integracao_tasy_model


class IntegracaoTasySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = integracao_tasy_model.IntegracaoTasyModel
        fields = (
            "identificador",
            "nr_atendimento",
            "nr_prescricao",
            "nr_sequencia",
            "nr_seq_interno",
            "nr_acess_number",
            "cd_proced_tasy",
            "cd_proced_integracao",
            "cd_proced_tasy_lado",
            "ds_procedimento",
            "ie_lado",
            "ie_urgencia",
            "dt_prev_execucao",
            "cd_setor_paciente",
            "cd_estabelecimento",
            "nm_pessoa_fisica",
            "dt_prescricao",
            "dt_liberacao",
            "cd_software_integracao",
            "nr_identidade_paciente",
            "cd_estab_terceiro",
            "cd_setor_execucao",
            "cd_paciente",
            "cd_prescritor",
            "ie_sexo",
            "dt_nascimento",
            "cd_integracao_proc_interno",
            "qt_altura_cm",
            "qt_idade_pac",
            "qt_peso",
            "nr_crm_prescritor",
            "cd_modalidade_proc",
            "uf_crm_prescritor",
            "nr_endereco_paciente",
            "nr_cpf_paciente",
            "qt_prescrito",
            "ds_endereco_paciente",
            "nr_prontuario_paciente",
            "ds_bairro_paciente",
            "ds_municipio_paciente",
            "uf_paciente",
            "cd_cep_paciente",
            "nr_telefone_paciente",
            "cd_convenio",
            "ds_categoria_convenio",
            "ds_convenio",
            "cd_cgc",
            "nr_seq_motivo_atend",
            "ds_motivo_atend",
            "ds_motivo_suspensao",
            "cd_pessoa_fisica",
            "cd_procedimento",
            "cd_tipo_procedimento",
            "qt_procedimento",
            "dt_atualizacao",
            "nm_usuario",
            "ds_observacao",
            "ie_origem_proced",
            "ds_dado_clinico",
            "ie_suspenso",
            "cd_setor_atendimento",
            "cd_medico",
            "dt_liberacao_medico",
            "ie_recem_nato",
            "nm_paciente",
            "nr_cpf",
            "nr_prontuario",
            "nm_medico",
            "nr_crm",
            "cd_categoria",
            "cd_usuario_convenio",
            "cd_material_exame",
            "ds_material_especial",
            "ie_amostra_entregue",
            "ds_horarios",
            "nr_seq_exame",
            "ds_endereco",
            "nr_endereco",
            "ds_complemento",
            "ds_bairro",
            "ds_municipio",
            "sg_estado",
            "nr_telefone",
            "cd_cep",
            "ds_setor_paciente",
            "cd_unidade",
            "ie_executar_leito",
            "ds_modalidade",
            "na_accessionnumber",
            "ie_tipo_atendimento",
            "nr_seq_proc_interno",
            "identificador_estudo_dicom",
            "cd_plano_convenio",
            "cd_plano",
            "cd_agenda",
            "ds_agenda",
            "cd_procedencia",
            "ds_procedencia",
            "cd_compl_conv",
            "dt_validade_carteira",
            "dt_resultado",
            "ds_senha",
            "nr_cpf_medico",
            "cd_estab_atend",
            "cd_estab_prescr",
            "dt_entrada",
            "ds_tipo_atendimento",
            "ds_observacao_pf",
            "ds_unidade_atend",
            "ds_plano",
            "dt_admissao_hosp",
            "uf_medico",
            "ds_local",
            "ds_local_exec",
            "nm_medico_aten_ext",
            "crm_medico_aten_ext",
            "nm_social",
            "ds_email",
            "integrado_tasy",
            "criado_worklist",
            "laudo_enviado",
            "exame_iniciado",
            "nm_sobrenome_pai",
            "nm_sobrenome_mae",
            "nm_primeiro_nome",
            "cancelado",
        )

    identificador = fields.Integer(required=False, default=None, allow_none=True)
    nr_atendimento = fields.Integer(required=False, default=None)
    nr_prescricao = fields.Integer(required=False, default=None)
    nr_sequencia = fields.Integer(required=False, default=None)
    nr_seq_interno = fields.Integer(required=False, default=None, allow_none=True)
    nr_acess_number = fields.Integer(required=False, default=None, allow_none=True)
    cd_proced_tasy = fields.String(required=False, default=None, allow_none=True)
    cd_proced_integracao = fields.String(required=False, default=None, allow_none=True)
    cd_proced_tasy_lado = fields.String(required=False, default=None, allow_none=True)
    ds_procedimento = fields.String(required=False, default=None, allow_none=True)
    ie_lado = fields.String(required=False, default=None, allow_none=True)
    ie_urgencia = fields.String(required=False, default=None, allow_none=True)
    dt_prev_execucao = fields.DateTime(required=False, default=None, allow_none=True)
    cd_setor_paciente = fields.String(required=False, default=None, allow_none=True)
    cd_estabelecimento = fields.String(required=False, default=None, allow_none=True)
    nm_pessoa_fisica = fields.String(required=False, default=None, allow_none=True)
    dt_prescricao = fields.DateTime(required=False, default=None, allow_none=True)
    dt_liberacao = fields.DateTime(required=False, default=None, allow_none=True)
    cd_software_integracao = fields.String(required=False, default=None, allow_none=True)
    cd_estab_terceiro = fields.String(required=False, default=None, allow_none=True)
    cd_setor_execucao = fields.String(required=False, default=None, allow_none=True)
    cd_paciente = fields.String(required=False, default=None, allow_none=True)
    cd_prescritor = fields.String(required=False, default=None, allow_none=True)
    ie_sexo = fields.String(required=False, default=None, allow_none=True)
    dt_nascimento = fields.Date(required=False, default=None)
    cd_integracao_proc_interno = fields.String(required=False, default=None, allow_none=True)
    qt_altura_cm = fields.String(required=False, default=None, allow_none=True)
    qt_idade_pac = fields.Integer(required=False, default=None, allow_none=True)
    qt_peso = fields.String(required=False, default=None, allow_none=True)
    nr_crm_prescritor = fields.Integer(required=False, default=None, allow_none=True)
    cd_modalidade_proc = fields.String(required=False, default=None, allow_none=True)
    uf_crm_prescritor = fields.String(required=False, default=None, allow_none=True)
    nr_cpf_paciente = fields.Integer(required=False, default=None, allow_none=True)
    qt_prescrito = fields.Integer(required=False, default=None, allow_none=True)
    nr_identidade_paciente = fields.String(required=False, default=None, allow_none=True)
    nr_prontuario_paciente = fields.Integer(required=False, default=None, allow_none=True)
    ds_endereco_paciente = fields.String(required=False, default=None, allow_none=True)
    nr_endereco_paciente = fields.Integer(required=False, default=None, allow_none=True)
    ds_bairro_paciente = fields.String(required=False, default=None, allow_none=True)
    ds_municipio_paciente = fields.String(required=False, default=None, allow_none=True)
    uf_paciente = fields.String(required=False, default=None, allow_none=True)
    cd_cep_paciente = fields.String(required=False, default=None, allow_none=True)
    nr_telefone_paciente = fields.String(required=False, default=None, allow_none=True)
    cd_convenio = fields.String(required=False, default=None, allow_none=True)
    ds_categoria_convenio = fields.String(required=False, default=None, allow_none=True)
    ds_convenio = fields.String(required=False, default=None, allow_none=True)
    cd_cgc = fields.String(required=False, default=None, allow_none=True)
    nr_seq_motivo_atend = fields.Integer(required=False, default=None, allow_none=True)
    ds_motivo_atend = fields.String(required=False, default=None, allow_none=True)
    ds_motivo_suspensao = fields.String(required=False, default=None, allow_none=True)
    cd_pessoa_fisica = fields.String(required=False, default=None, allow_none=True)
    cd_procedimento = fields.String(required=False, default=None, allow_none=True)
    cd_tipo_procedimento = fields.String(required=False, default=None, allow_none=True)
    qt_procedimento = fields.Integer(required=False, default=None, allow_none=True)
    dt_atualizacao = fields.DateTime(required=False, default=None, allow_none=True)
    nm_usuario = fields.String(required=False, default=None, allow_none=True)
    ds_observacao = fields.String(required=False, default=None, allow_none=True)
    ie_origem_proced = fields.String(required=False, default=None, allow_none=True)
    ds_dado_clinico = fields.String(required=False, default=None, allow_none=True)
    ie_suspenso = fields.String(required=False, default=None, allow_none=True)
    cd_setor_atendimento = fields.String(required=False, default=None, allow_none=True)
    cd_medico = fields.String(required=False, default=None, allow_none=True)
    dt_liberacao_medico = fields.DateTime(required=False, default=None, allow_none=True)
    ie_recem_nato = fields.String(required=False, default=None, allow_none=True)
    nm_paciente = fields.String(required=False, default=None, allow_none=True)
    nr_cpf = fields.Integer(required=False, default=None, allow_none=True)
    nr_prontuario = fields.Integer(required=False, default=None)
    nm_medico = fields.String(required=False, default=None, allow_none=True)
    nr_crm = fields.Integer(required=False, default=None, allow_none=True)
    cd_categoria = fields.String(required=False, default=None, allow_none=True)
    cd_usuario_convenio = fields.String(required=False, default=None, allow_none=True)
    cd_material_exame = fields.String(required=False, default=None, allow_none=True)
    ds_material_especial = fields.String(required=False, default=None, allow_none=True)
    ie_amostra_entregue = fields.String(required=False, default=None, allow_none=True)
    ds_horarios = fields.String(required=False, default=None, allow_none=True)
    nr_seq_exame = fields.Integer(required=False, default=None, allow_none=True)
    ds_endereco = fields.String(required=False, default=None, allow_none=True)
    nr_endereco = fields.Integer(required=False, default=None, allow_none=True)
    ds_complemento = fields.String(required=False, default=None, allow_none=True)
    ds_bairro = fields.String(required=False, default=None, allow_none=True)
    ds_municipio = fields.String(required=False, default=None, allow_none=True)
    sg_estado = fields.String(required=False, default=None, allow_none=True)
    nr_telefone = fields.String(required=False, default=None, allow_none=True)
    cd_cep = fields.String(required=False, default=None, allow_none=True)
    ds_setor_paciente = fields.String(required=False, default=None, allow_none=True)
    cd_unidade = fields.String(required=False, default=None, allow_none=True)
    ie_executar_leito = fields.String(required=False, default=None, allow_none=True)
    ds_modalidade = fields.String(required=False, default=None, allow_none=True)
    na_accessionnumber = fields.Integer(required=False, default=None, allow_none=True)
    ie_tipo_atendimento = fields.String(required=False, default=None, allow_none=True)
    nr_seq_proc_interno = fields.Integer(required=False, default=None, allow_none=True)
    cd_plano_convenio = fields.String(required=False, default=None, allow_none=True)
    cd_plano = fields.String(required=False, default=None, allow_none=True)
    cd_agenda = fields.String(required=False, default=None, allow_none=True)
    ds_agenda = fields.String(required=False, default=None, allow_none=True)
    cd_procedencia = fields.String(required=False, default=None, allow_none=True)
    ds_procedencia = fields.String(required=False, default=None, allow_none=True)
    cd_compl_conv = fields.String(required=False, default=None, allow_none=True)
    dt_validade_carteira = fields.String(required=False, default=None, allow_none=True)
    dt_resultado = fields.String(required=False, default=None, allow_none=True)
    ds_senha = fields.String(required=False, default=None, allow_none=True)
    nr_cpf_medico = fields.String(required=False, default=None, allow_none=True)
    cd_estab_atend = fields.String(required=False, default=None, allow_none=True)
    cd_estab_prescr = fields.String(required=False, default=None, allow_none=True)
    dt_entrada = fields.DateTime(required=False, default=None, allow_none=True)
    ds_tipo_atendimento = fields.String(required=False, default=None, allow_none=True)
    ds_observacao_pf = fields.String(required=False, default=None, allow_none=True)
    ds_unidade_atend = fields.String(required=False, default=None, allow_none=True)
    ds_plano = fields.String(required=False, default=None, allow_none=True)
    dt_admissao_hosp = fields.String(required=False, default=None, allow_none=True)
    uf_medico = fields.String(required=False, default=None, allow_none=True)
    ds_local = fields.String(required=False, default=None, allow_none=True)
    ds_local_exec = fields.String(required=False, default=None, allow_none=True)
    nm_medico_aten_ext = fields.String(required=False, default=None, allow_none=True)
    crm_medico_aten_ext = fields.Integer(required=False, default=None, allow_none=True)
    nm_social = fields.String(required=False, default=None)
    ds_email = fields.String(required=False, default=None, allow_none=True)
    integrado_tasy = fields.Boolean(required=False, default=None, allow_none=True)
    identificador_estudo_dicom = fields.Integer(required=False, default=None, allow_none=True)
    criado_worklist = fields.Boolean(required=False, default=None, allow_none=True)
    laudo_enviado = fields.Boolean(required=False, default=None, allow_none=True)
    exame_iniciado = fields.Boolean(required=False, default=None, allow_none=True)
    nm_sobrenome_pai = fields.String(required=False, default=None, allow_none=True)
    nm_sobrenome_mae = fields.String(required=False, default=None, allow_none=True)
    nm_primeiro_nome = fields.String(required=False, default=None, allow_none=True)
    cancelado = fields.String(required=False, default=False, allow_none=True)