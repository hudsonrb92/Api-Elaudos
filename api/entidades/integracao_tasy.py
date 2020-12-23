"""Class to manage table integracao tasy"""
from typing import Optional
from datetime import date, datetime, timedelta


class IntegracaoTasy:
    """Class to manage interations with table integracao_tasy"""

    def __init__(
        self,
        nr_atendimento: int,
        nr_prescricao: int,
        nr_sequencia: int,
        nr_seq_interno: Optional[int] = None,
        nr_acess_number: Optional[int] = None,
        cd_proced_tasy: Optional[str] = "",
        cd_proced_integracao: Optional[str] = "",
        cd_proced_tasy_lado: Optional[str] = "",
        ds_procedimento: Optional[str] = "",
        ie_lado: Optional[str] = "",
        ie_urgencia: Optional[str] = "",
        dt_prev_execucao: Optional[datetime] = datetime.now() + timedelta(1.0),
        cd_setor_paciente: Optional[str] = "",
        cd_estabelecimento: Optional[str] = "",
        nm_pessoa_fisica: Optional[str] = "",
        dt_prescricao: Optional[datetime] = datetime.now(),
        cd_setor_execucao: Optional[str] = "",
        dt_liberacao: Optional[datetime] = datetime.now(),
        cd_software_integracao: Optional[str] = "",
        cd_estab_terceiro: Optional[str] = "",
        cd_paciente: Optional[str] = "",
        cd_prescritor: Optional[str] = "",
        ie_sexo: Optional[str] = "",
        dt_nascimento: Optional[date] = datetime.now(),
        cd_integracao_proc_interno: Optional[str] = "",
        qt_altura_cm: Optional[str] = "",
        qt_idade_pac: Optional[int] = None,
        qt_peso: Optional[str] = "",
        nr_crm_prescritor: Optional[int] = None,
        cd_modalidade_proc: Optional[str] = "",
        uf_crm_prescritor: Optional[str] = "",
        nr_cpf_paciente: Optional[int] = None,
        qt_prescrito: Optional[int] = None,
        nr_identidade_paciente: Optional[str] = "",
        nr_prontuario_paciente: Optional[int] = None,
        ds_endereco_paciente: Optional[str] = "",
        nr_endereco_paciente: Optional[int] = None,
        ds_bairro_paciente: Optional[str] = "",
        ds_municipio_paciente: Optional[str] = "",
        uf_paciente: Optional[str] = "",
        cd_cep_paciente: Optional[str] = "",
        nr_telefone_paciente: Optional[str] = "",
        cd_convenio: Optional[str] = "",
        ds_categoria_convenio: Optional[str] = "",
        ds_convenio: Optional[str] = "",
        cd_cgc: Optional[str] = "",
        nr_seq_motivo_atend: Optional[int] = None,
        ds_motivo_atend: Optional[str] = "",
        ds_motivo_suspensao: Optional[str] = "",
        cd_pessoa_fisica: Optional[str] = "",
        cd_procedimento: Optional[str] = "",
        cd_tipo_procedimento: Optional[str] = "",
        qt_procedimento: Optional[int] = None,
        dt_atualizacao: Optional[datetime] = None,
        nm_usuario: Optional[str] = "",
        ds_observacao: Optional[str] = "",
        ie_origem_proced: Optional[str] = "",
        ds_dado_clinico: Optional[str] = "",
        ie_suspenso: Optional[str] = "",
        cd_setor_atendimento: Optional[str] = "",
        cd_medico: Optional[str] = "",
        dt_liberacao_medico: Optional[datetime] = None,
        ie_recem_nato: Optional[str] = "",
        nm_paciente: Optional[str] = "",
        nr_cpf: Optional[int] = None,
        nr_prontuario: Optional[int] = None,
        nm_medico: Optional[str] = "",
        nr_crm: Optional[str] = "",
        cd_categoria: Optional[str] = "",
        cd_usuario_convenio: Optional[str] = "",
        cd_material_exame: Optional[str] = "",
        ds_material_especial: Optional[str] = "",
        ie_amostra_entregue: Optional[str] = "",
        ds_horarios: Optional[str] = "",
        nr_seq_exame: Optional[int] = None,
        ds_endereco: Optional[str] = "",
        nr_endereco: Optional[int] = None,
        ds_complemento: Optional[str] = "",
        ds_bairro: Optional[str] = "",
        ds_municipio: Optional[str] = "",
        sg_estado: Optional[str] = "",
        nr_telefone: Optional[str] = "",
        cd_cep: Optional[str] = "",
        ds_setor_paciente: Optional[str] = "",
        cd_unidade: Optional[str] = "",
        ie_executar_leito: Optional[str] = "",
        ds_modalidade: Optional[str] = "",
        na_accessionnumber: Optional[str] = "",
        ie_tipo_atendimento: Optional[str] = "",
        nr_seq_proc_interno: Optional[int] = None,
        cd_plano_convenio: Optional[str] = "",
        cd_plano: Optional[str] = "",
        cd_agenda: Optional[str] = "",
        ds_agenda: Optional[str] = "",
        cd_procedencia: Optional[str] = "",
        ds_procedencia: Optional[str] = "",
        cd_compl_conv: Optional[str] = "",
        dt_validade_carteira: Optional[str] = "",
        dt_resultado: Optional[str] = "",
        ds_senha: Optional[str] = "",
        nr_cpf_medico: Optional[str] = "",
        cd_estab_atend: Optional[str] = "",
        cd_estab_prescr: Optional[str] = "",
        dt_entrada: Optional[datetime] = None,
        ds_tipo_atendimento: Optional[str] = "",
        dt_admissao_hosp: Optional[str] = "",
        uf_medico: Optional[str] = "",
        ds_local: Optional[str] = "",
        ds_observacao_pf: Optional[str] = "",
        ds_unidade_atend: Optional[str] = "",
        ds_plano: Optional[str] = "",
        ds_local_exec: Optional[str] = "",
        nm_medico_aten_ext: Optional[str] = "",
        crm_medico_aten_ext: Optional[str] = "",
        nm_social: Optional[str] = "",
        ds_email: Optional[str] = "",
        nm_sobrenome_pai: Optional[str] = "",
        nm_sobrenome_mae: Optional[str] = "",
        nm_primeiro_nome: Optional[str] = "",
        cancelado: Optional[bool] = False,
    ) -> None:
        self.nr_atendimento = nr_atendimento
        self.nr_prescricao = nr_prescricao
        self.nr_sequencia = nr_sequencia
        self.nr_seq_interno = nr_seq_interno
        self.nr_acess_number = nr_acess_number
        self.cd_proced_tasy = cd_proced_tasy
        self.cd_proced_integracao = cd_proced_integracao
        self.cd_proced_tasy_lado = cd_proced_tasy_lado
        self.ds_procedimento = ds_procedimento
        self.ie_lado = ie_lado
        self.ie_urgencia = ie_urgencia
        self.dt_prev_execucao = dt_prev_execucao
        self.cd_setor_paciente = cd_setor_paciente
        self.cd_estabelecimento = cd_estabelecimento
        self.nm_pessoa_fisica = nm_pessoa_fisica
        self.dt_prescricao = dt_prescricao
        self.cd_setor_execucao = cd_setor_execucao
        self.dt_liberacao = dt_liberacao
        self.cd_software_integracao = cd_software_integracao
        self.cd_estab_terceiro = cd_estab_terceiro
        self.cd_paciente = cd_paciente
        self.cd_prescritor = cd_prescritor
        self.ie_sexo = ie_sexo
        self.dt_nascimento = dt_nascimento
        self.cd_integracao_proc_interno = cd_integracao_proc_interno
        self.qt_altura_cm = qt_altura_cm
        self.qt_idade_pac = qt_idade_pac
        self.qt_peso = qt_peso
        self.nr_crm_prescritor = nr_crm_prescritor
        self.cd_modalidade_proc = cd_modalidade_proc
        self.uf_crm_prescritor = uf_crm_prescritor
        self.nr_cpf_paciente = nr_cpf_paciente
        self.qt_prescrito = qt_prescrito
        self.nr_identidade_paciente = nr_identidade_paciente
        self.nr_prontuario_paciente = nr_prontuario_paciente
        self.ds_endereco_paciente = ds_endereco_paciente
        self.nr_endereco_paciente = nr_endereco_paciente
        self.ds_bairro_paciente = ds_bairro_paciente
        self.ds_municipio_paciente = ds_municipio_paciente
        self.uf_paciente = uf_paciente
        self.cd_cep_paciente = cd_cep_paciente
        self.nr_telefone_paciente = nr_telefone_paciente
        self.cd_convenio = cd_convenio
        self.ds_categoria_convenio = ds_categoria_convenio
        self.ds_convenio = ds_convenio
        self.cd_cgc = cd_cgc
        self.nr_seq_motivo_atend = nr_seq_motivo_atend
        self.ds_motivo_atend = ds_motivo_atend
        self.ds_motivo_suspensao = ds_motivo_suspensao
        self.cd_pessoa_fisica = cd_pessoa_fisica
        self.cd_procedimento = cd_procedimento
        self.cd_tipo_procedimento = cd_tipo_procedimento
        self.qt_procedimento = qt_procedimento
        self.dt_atualizacao = dt_atualizacao
        self.nm_usuario = nm_usuario
        self.ds_observacao = ds_observacao
        self.ie_origem_proced = ie_origem_proced
        self.ds_dado_clinico = ds_dado_clinico
        self.ie_suspenso = ie_suspenso
        self.cd_setor_atendimento = cd_setor_atendimento
        self.cd_medico = cd_medico
        self.dt_liberacao_medico = dt_liberacao_medico
        self.ie_recem_nato = ie_recem_nato
        self.nm_paciente = nm_paciente
        self.nr_cpf = nr_cpf
        self.nr_prontuario = nr_prontuario
        self.nm_medico = nm_medico
        self.nr_crm = nr_crm
        self.cd_categoria = cd_categoria
        self.cd_usuario_convenio = cd_usuario_convenio
        self.cd_material_exame = cd_material_exame
        self.ds_material_especial = ds_material_especial
        self.ie_amostra_entregue = ie_amostra_entregue
        self.ds_horarios = ds_horarios
        self.nr_seq_exame = nr_seq_exame
        self.ds_endereco = ds_endereco
        self.nr_endereco = nr_endereco
        self.ds_complemento = ds_complemento
        self.ds_bairro = ds_bairro
        self.ds_municipio = ds_municipio
        self.sg_estado = sg_estado
        self.nr_telefone = nr_telefone
        self.cd_cep = cd_cep
        self.ds_setor_paciente = ds_setor_paciente
        self.cd_unidade = cd_unidade
        self.ie_executar_leito = ie_executar_leito
        self.ds_modalidade = ds_modalidade
        self.na_accessionnumber = na_accessionnumber
        self.ie_tipo_atendimento = ie_tipo_atendimento
        self.nr_seq_proc_interno = nr_seq_proc_interno
        self.cd_plano_convenio = cd_plano_convenio
        self.cd_plano = cd_plano
        self.cd_agenda = cd_agenda
        self.ds_agenda = ds_agenda
        self.cd_procedencia = cd_procedencia
        self.ds_procedencia = ds_procedencia
        self.cd_compl_conv = cd_compl_conv
        self.dt_validade_carteira = dt_validade_carteira
        self.dt_resultado = dt_resultado
        self.ds_senha = ds_senha
        self.nr_cpf_medico = nr_cpf_medico
        self.cd_estab_atend = cd_estab_atend
        self.cd_estab_prescr = cd_estab_prescr
        self.dt_entrada = dt_entrada
        self.ds_tipo_atendimento = ds_tipo_atendimento
        self.ds_observacao_pf = ds_observacao_pf
        self.ds_unidade_atend = ds_unidade_atend
        self.ds_plano = ds_plano
        self.dt_admissao_hosp = dt_admissao_hosp
        self.uf_medico = uf_medico
        self.ds_local = ds_local
        self.ds_local_exec = ds_local_exec
        self.nm_medico_aten_ext = nm_medico_aten_ext
        self.crm_medico_aten_ext = crm_medico_aten_ext
        self.nm_social = nm_social
        self.ds_email = ds_email
        self.nm_sobrenome_pai = nm_sobrenome_pai
        self.nm_sobrenome_mae = nm_sobrenome_mae
        self.nm_primeiro_nome = nm_primeiro_nome
        self.cancelado = cancelado

    @property
    def nr_atendimento(self):
        return self._nr_atendimento

    @nr_atendimento.setter
    def nr_atendimento(self, value):
        self._nr_atendimento = value

    @property
    def nr_prescricao(self):
        return self._nr_prescricao

    @nr_prescricao.setter
    def nr_prescricao(self, value):
        self._nr_prescricao = value

    @property
    def nr_sequencia(self):
        return self._nr_sequencia

    @nr_sequencia.setter
    def nr_sequencia(self, value):
        self._nr_sequencia = value

    @property
    def nr_seq_interno(self):
        return self._nr_seq_interno

    @nr_seq_interno.setter
    def nr_seq_interno(self, value):
        self._nr_seq_interno = value

    @property
    def nr_acess_number(self):
        return self._nr_acess_number

    @nr_acess_number.setter
    def nr_acess_number(self, value):
        self._nr_acess_number = value

    @property
    def cd_proced_tasy(self):
        return self._cd_proced_tasy

    @cd_proced_tasy.setter
    def cd_proced_tasy(self, value):
        self._cd_proced_tasy = value

    @property
    def cd_proced_integracao(self):
        return self._cd_proced_integracao

    @cd_proced_integracao.setter
    def cd_proced_integracao(self, value):
        self._cd_proced_integracao = value

    @property
    def cd_proced_tasy_lado(self):
        return self._cd_proced_tasy_lado

    @cd_proced_tasy_lado.setter
    def cd_proced_tasy_lado(self, value):
        self._cd_proced_tasy_lado = value

    @property
    def ds_procedimento(self):
        return self._ds_procedimento

    @ds_procedimento.setter
    def ds_procedimento(self, ds_procedimento):
        self._ds_procedimento = ds_procedimento.upper()

    @property
    def ie_lado(self):
        return self._ie_lado

    @ie_lado.setter
    def ie_lado(self, value):
        self._ie_lado = value

    @property
    def ie_urgencia(self):
        return self._ie_urgencia

    @ie_urgencia.setter
    def ie_urgencia(self, value):
        self._ie_urgencia = value

    @property
    def dt_prev_execucao(self):
        return self._dt_prev_execucao

    @dt_prev_execucao.setter
    def dt_prev_execucao(self, value):
        self._dt_prev_execucao = value

    @property
    def cd_setor_paciente(self):
        return self._cd_setor_paciente

    @cd_setor_paciente.setter
    def cd_setor_paciente(self, value):
        self._cd_setor_paciente = value

    @property
    def cd_estabelecimento(self):
        return self._cd_estabelecimento

    @cd_estabelecimento.setter
    def cd_estabelecimento(self, value):
        self._cd_estabelecimento = value

    @property
    def nm_pessoa_fisica(self):
        return self._nm_pessoa_fisica

    @nm_pessoa_fisica.setter
    def nm_pessoa_fisica(self, value):
        if value:
            self._nm_pessoa_fisica = value.upper()

    @property
    def dt_prescricao(self):
        return self._dt_prescricao

    @dt_prescricao.setter
    def dt_prescricao(self, value):
        self._dt_prescricao = value

    @property
    def cd_setor_execucao(self):
        return self._cd_setor_execucao

    @cd_setor_execucao.setter
    def cd_setor_execucao(self, value):
        self._cd_setor_execucao = value

    @property
    def dt_liberacao(self):
        return self._dt_liberacao

    @dt_liberacao.setter
    def dt_liberacao(self, value):
        self._dt_liberacao = value

    @property
    def cd_software_integracao(self):
        return self._cd_software_integracao

    @cd_software_integracao.setter
    def cd_software_integracao(self, value):
        self._cd_software_integracao = value

    @property
    def cd_estab_terceiro(self):
        return self._cd_estab_terceiro

    @cd_estab_terceiro.setter
    def cd_estab_terceiro(self, value):
        self._cd_estab_terceiro = value

    @property
    def cd_paciente(self):
        return self._cd_paciente

    @cd_paciente.setter
    def cd_paciente(self, value):
        self._cd_paciente = value

    @property
    def cd_prescritor(self):
        return self._cd_prescritor

    @cd_prescritor.setter
    def cd_prescritor(self, value):
        self._cd_prescritor = value

    @property
    def ie_sexo(self):
        return self._ie_sexo

    @ie_sexo.setter
    def ie_sexo(self, value):
        self._ie_sexo = value

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, value):
        self._dt_nascimento = value

    @property
    def cd_integracao_proc_interno(self):
        return self._cd_integracao_proc_interno

    @cd_integracao_proc_interno.setter
    def cd_integracao_proc_interno(self, value):
        self._cd_integracao_proc_interno = value

    @property
    def qt_altura_cm(self):
        return self._qt_altura_cm

    @qt_altura_cm.setter
    def qt_altura_cm(self, value):
        self._qt_altura_cm = value

    @property
    def qt_idade_pac(self):
        return self._qt_idade_pac

    @qt_idade_pac.setter
    def qt_idade_pac(self, value):
        self._qt_idade_pac = value

    @property
    def qt_peso(self):
        return self._qt_peso

    @qt_peso.setter
    def qt_peso(self, value):
        self._qt_peso = value

    @property
    def nr_crm_prescritor(self):
        return self._nr_crm_prescritor

    @nr_crm_prescritor.setter
    def nr_crm_prescritor(self, value):
        self._nr_crm_prescritor = value

    @property
    def cd_modalidade_proc(self):
        return self._cd_modalidade_proc

    @cd_modalidade_proc.setter
    def cd_modalidade_proc(self, value):
        self._cd_modalidade_proc = value

    @property
    def uf_crm_prescritor(self):
        return self._uf_crm_prescritor

    @uf_crm_prescritor.setter
    def uf_crm_prescritor(self, value):
        self._uf_crm_prescritor = value

    @property
    def nr_cpf_paciente(self):
        return self._nr_cpf_paciente

    @nr_cpf_paciente.setter
    def nr_cpf_paciente(self, value):
        self._nr_cpf_paciente = value

    @property
    def qt_prescrito(self):
        return self._qt_prescrito

    @qt_prescrito.setter
    def qt_prescrito(self, value):
        self._qt_prescrito = value

    @property
    def nr_identidade_paciente(self):
        return self._nr_identidade_paciente

    @nr_identidade_paciente.setter
    def nr_identidade_paciente(self, value):
        self._nr_identidade_paciente = value

    @property
    def nr_prontuario_paciente(self):
        return self._nr_prontuario_paciente

    @nr_prontuario_paciente.setter
    def nr_prontuario_paciente(self, value):
        self._nr_prontuario_paciente = value

    @property
    def ds_endereco_paciente(self):
        return self._ds_endereco_paciente

    @ds_endereco_paciente.setter
    def ds_endereco_paciente(self, value):
        self._ds_endereco_paciente = value

    @property
    def nr_endereco_paciente(self):
        return self._nr_endereco_paciente

    @nr_endereco_paciente.setter
    def nr_endereco_paciente(self, value):
        self._nr_endereco_paciente = value

    @property
    def ds_bairro_paciente(self):
        return self._ds_bairro_paciente

    @ds_bairro_paciente.setter
    def ds_bairro_paciente(self, value):
        self._ds_bairro_paciente = value

    @property
    def ds_municipio_paciente(self):
        return self._ds_municipio_paciente

    @ds_municipio_paciente.setter
    def ds_municipio_paciente(self, value):
        self._ds_municipio_paciente = value

    @property
    def uf_paciente(self):
        return self._uf_paciente

    @uf_paciente.setter
    def uf_paciente(self, value):
        self._uf_paciente = value

    @property
    def cd_cep_paciente(self):
        return self._cd_cep_paciente

    @cd_cep_paciente.setter
    def cd_cep_paciente(self, value):
        self._cd_cep_paciente = value

    @property
    def nr_telefone_paciente(self):
        return self._nr_telefone_paciente

    @nr_telefone_paciente.setter
    def nr_telefone_paciente(self, value):
        self._nr_telefone_paciente = value

    @property
    def cd_convenio(self):
        return self._cd_convenio

    @cd_convenio.setter
    def cd_convenio(self, cd_convenio):
        self._cd_convenio = cd_convenio

    @property
    def ds_categoria_convenio(self):
        return self._ds_categoria_convenio

    @ds_categoria_convenio.setter
    def ds_categoria_convenio(self, value):
        self._ds_categoria_convenio = value

    @property
    def ds_convenio(self):
        return self._ds_convenio

    @ds_convenio.setter
    def ds_convenio(self, value):
        self._ds_convenio = value

    @property
    def cd_cgc(self):
        return self._cd_cgc

    @cd_cgc.setter
    def cd_cgc(self, value):
        self._cd_cgc = value

    @property
    def nr_seq_motivo_atend(self):
        return self._nr_seq_motivo_atend

    @nr_seq_motivo_atend.setter
    def nr_seq_motivo_atend(self, value):
        self._nr_seq_motivo_atend = value

    @property
    def ds_motivo_atend(self):
        return self._ds_motivo_atend

    @ds_motivo_atend.setter
    def ds_motivo_atend(self, value):
        self._ds_motivo_atend = value

    @property
    def ds_motivo_suspensao(self):
        return self._ds_motivo_suspensao

    @ds_motivo_suspensao.setter
    def ds_motivo_suspensao(self, value):
        self._ds_motivo_suspensao = value

    @property
    def cd_pessoa_fisica(self):
        return self._cd_pessoa_fisica

    @cd_pessoa_fisica.setter
    def cd_pessoa_fisica(self, value):
        self._cd_pessoa_fisica = value

    @property
    def cd_procedimento(self):
        return self._cd_procedimento

    @cd_procedimento.setter
    def cd_procedimento(self, value):
        self._cd_procedimento = value

    @property
    def cd_tipo_procedimento(self):
        return self._cd_tipo_procedimento

    @cd_tipo_procedimento.setter
    def cd_tipo_procedimento(self, value):
        self._cd_tipo_procedimento = value

    @property
    def qt_procedimento(self):
        return self._qt_procedimento

    @qt_procedimento.setter
    def qt_procedimento(self, value):
        self._qt_procedimento = value

    @property
    def dt_atualizacao(self):
        return self._dt_atualizacao

    @dt_atualizacao.setter
    def dt_atualizacao(self, value):
        self._dt_atualizacao = value

    @property
    def nm_usuario(self):
        return self._nm_usuario

    @nm_usuario.setter
    def nm_usuario(self, value):
        self._nm_usuario = value

    @property
    def ds_observacao(self):
        return self._ds_observacao

    @ds_observacao.setter
    def ds_observacao(self, value):
        self._ds_observacao = value

    @property
    def ie_origem_proced(self):
        return self._ie_origem_proced

    @ie_origem_proced.setter
    def ie_origem_proced(self, value):
        self._ie_origem_proced = value

    @property
    def ds_dado_clinico(self):
        return self._ds_dado_clinico

    @ds_dado_clinico.setter
    def ds_dado_clinico(self, value):
        self._ds_dado_clinico = value

    @property
    def ie_suspenso(self):
        return self._ie_suspenso

    @ie_suspenso.setter
    def ie_suspenso(self, value):
        self._ie_suspenso = value

    @property
    def cd_setor_atendimento(self):
        return self._cd_setor_atendimento

    @cd_setor_atendimento.setter
    def cd_setor_atendimento(self, value):
        self._cd_setor_atendimento = value

    @property
    def cd_medico(self):
        return self._cd_medico

    @cd_medico.setter
    def cd_medico(self, value):
        self._cd_medico = value

    @property
    def dt_liberacao_medico(self):
        return self._dt_liberacao_medico

    @dt_liberacao_medico.setter
    def dt_liberacao_medico(self, value):
        self._dt_liberacao_medico = value

    @property
    def ie_recem_nato(self):
        return self._ie_recem_nato

    @ie_recem_nato.setter
    def ie_recem_nato(self, value):
        self._ie_recem_nato = value

    @property
    def nm_paciente(self):
        return self._nm_paciente

    @nm_paciente.setter
    def nm_paciente(self, value):
        self._nm_paciente = value

    @property
    def nr_cpf(self):
        return self._nr_cpf

    @nr_cpf.setter
    def nr_cpf(self, value):
        self._nr_cpf = value

    @property
    def nr_prontuario(self):
        return self._nr_prontuario

    @nr_prontuario.setter
    def nr_prontuario(self, value):
        self._nr_prontuario = value

    @property
    def nm_medico(self):
        return self._nm_medico

    @nm_medico.setter
    def nm_medico(self, value):
        self._nm_medico = value

    @property
    def nr_crm(self):
        return self._nr_crm

    @nr_crm.setter
    def nr_crm(self, value):
        self._nr_crm = value

    @property
    def cd_categoria(self):
        return self._cd_categoria

    @cd_categoria.setter
    def cd_categoria(self, value):
        self._cd_categoria = value

    @property
    def cd_usuario_convenio(self):
        return self._cd_usuario_convenio

    @cd_usuario_convenio.setter
    def cd_usuario_convenio(self, value):
        self._cd_usuario_convenio = value

    @property
    def cd_material_exame(self):
        return self._cd_material_exame

    @cd_material_exame.setter
    def cd_material_exame(self, value):
        self._cd_material_exame = value

    @property
    def ds_material_especial(self):
        return self._ds_material_especial

    @ds_material_especial.setter
    def ds_material_especial(self, value):
        self._ds_material_especial = value

    @property
    def ie_amostra_entregue(self):
        return self._ie_amostra_entregue

    @ie_amostra_entregue.setter
    def ie_amostra_entregue(self, value):
        self._ie_amostra_entregue = value

    @property
    def ds_horarios(self):
        return self._ds_horarios

    @ds_horarios.setter
    def ds_horarios(self, value):
        self._ds_horarios = value

    @property
    def nr_seq_exame(self):
        return self._nr_seq_exame

    @nr_seq_exame.setter
    def nr_seq_exame(self, value):
        self._nr_seq_exame = value

    @property
    def ds_endereco(self):
        return self._ds_endereco

    @ds_endereco.setter
    def ds_endereco(self, value):
        self._ds_endereco = value

    @property
    def nr_endereco(self):
        return self._nr_endereco

    @nr_endereco.setter
    def nr_endereco(self, value):
        self._nr_endereco = value

    @property
    def ds_complemento(self):
        return self._ds_complemento

    @ds_complemento.setter
    def ds_complemento(self, value):
        self._ds_complemento = value

    @property
    def ds_bairro(self):
        return self._ds_bairro

    @ds_bairro.setter
    def ds_bairro(self, value):
        self._ds_bairro = value

    @property
    def ds_municipio(self):
        return self._ds_municipio

    @ds_municipio.setter
    def ds_municipio(self, value):
        self._ds_municipio = value

    @property
    def sg_estado(self):
        return self._sg_estado

    @sg_estado.setter
    def sg_estado(self, value):
        self._sg_estado = value

    @property
    def nr_telefone(self):
        return self._nr_telefone

    @nr_telefone.setter
    def nr_telefone(self, value):
        self._nr_telefone = value

    @property
    def cd_cep(self):
        return self._cd_cep

    @cd_cep.setter
    def cd_cep(self, cd_cep):
        self._cd_cep = cd_cep

    @property
    def ds_setor_paciente(self):
        return self._ds_setor_paciente

    @ds_setor_paciente.setter
    def ds_setor_paciente(self, value):
        self._ds_setor_paciente = value

    @property
    def cd_unidade(self):
        return self._cd_unidade

    @cd_unidade.setter
    def cd_unidade(self, value):
        self._cd_unidade = value

    @property
    def ie_executar_leito(self):
        return self._ie_executar_leito

    @ie_executar_leito.setter
    def ie_executar_leito(self, value):
        self._ie_executar_leito = value

    @property
    def ds_modalidade(self):
        return self._ds_modalidade

    @ds_modalidade.setter
    def ds_modalidade(self, value):
        self._ds_modalidade = value

    @property
    def na_accessionnumber(self):
        return self._na_accessionnumber

    @na_accessionnumber.setter
    def na_accessionnumber(self, value):
        self._na_accessionnumber = value

    @property
    def ie_tipo_atendimento(self):
        return self._ie_tipo_atendimento

    @ie_tipo_atendimento.setter
    def ie_tipo_atendimento(self, value):
        self._ie_tipo_atendimento = value

    @property
    def nr_seq_proc_interno(self):
        return self._nr_seq_proc_interno

    @nr_seq_proc_interno.setter
    def nr_seq_proc_interno(self, value):
        self._nr_seq_proc_interno = value

    @property
    def cd_plano_convenio(self):
        return self._cd_plano_convenio

    @cd_plano_convenio.setter
    def cd_plano_convenio(self, value):
        self._cd_plano_convenio = value

    @property
    def cd_plano(self):
        return self._cd_plano

    @cd_plano.setter
    def cd_plano(self, value):
        self._cd_plano = value

    @property
    def cd_agenda(self):
        return self._cd_agenda

    @cd_agenda.setter
    def cd_agenda(self, value):
        self._cd_agenda = value

    @property
    def ds_agenda(self):
        return self._ds_agenda

    @ds_agenda.setter
    def ds_agenda(self, value):
        self._ds_agenda = value

    @property
    def cd_procedencia(self):
        return self._cd_procedencia

    @cd_procedencia.setter
    def cd_procedencia(self, value):
        self._cd_procedencia = value

    @property
    def ds_procedencia(self):
        return self._ds_procedencia

    @ds_procedencia.setter
    def ds_procedencia(self, value):
        self._ds_procedencia = value

    @property
    def cd_compl_conv(self):
        return self._cd_compl_conv

    @cd_compl_conv.setter
    def cd_compl_conv(self, value):
        self._cd_compl_conv = value

    @property
    def dt_validade_carteira(self):
        return self._dt_validade_carteira

    @dt_validade_carteira.setter
    def dt_validade_carteira(self, value):
        self._dt_validade_carteira = value

    @property
    def dt_resultado(self):
        return self._dt_resultado

    @dt_resultado.setter
    def dt_resultado(self, value):
        self._dt_resultado = value

    @property
    def ds_senha(self):
        return self._ds_senha

    @ds_senha.setter
    def ds_senha(self, value):
        self._ds_senha = value

    @property
    def nr_cpf_medico(self):
        return self._nr_cpf_medico

    @nr_cpf_medico.setter
    def nr_cpf_medico(self, value):
        self._nr_cpf_medico = value

    @property
    def cd_estab_atend(self):
        return self._cd_estab_atend

    @cd_estab_atend.setter
    def cd_estab_atend(self, value):
        self._cd_estab_atend = value

    @property
    def cd_estab_prescr(self):
        return self._cd_estab_prescr

    @cd_estab_prescr.setter
    def cd_estab_prescr(self, value):
        self._cd_estab_prescr = value

    @property
    def dt_entrada(self):
        return self._dt_entrada

    @dt_entrada.setter
    def dt_entrada(self, value):
        self._dt_entrada = value

    @property
    def ds_tipo_atendimento(self):
        return self._ds_tipo_atendimento

    @ds_tipo_atendimento.setter
    def ds_tipo_atendimento(self, value):
        self._ds_tipo_atendimento = value

    @property
    def ds_observacao_pf(self):
        return self._ds_observacao_pf

    @ds_observacao_pf.setter
    def ds_observacao_pf(self, value):
        self._ds_observacao_pf = value

    @property
    def ds_unidade_atend(self):
        return self._ds_unidade_atend

    @ds_unidade_atend.setter
    def ds_unidade_atend(self, value):
        self._ds_unidade_atend = value

    @property
    def ds_plano(self):
        return self._ds_plano

    @ds_plano.setter
    def ds_plano(self, value):
        self._ds_plano = value

    @property
    def dt_admissao_hosp(self):
        return self._dt_admissao_hosp

    @dt_admissao_hosp.setter
    def dt_admissao_hosp(self, value):
        self._dt_admissao_hosp = value

    @property
    def uf_medico(self):
        return self._uf_medico

    @uf_medico.setter
    def uf_medico(self, value):
        self._uf_medico = value

    @property
    def ds_local(self):
        return self._ds_local

    @ds_local.setter
    def ds_local(self, value):
        self._ds_local = value

    @property
    def ds_local_exec(self):
        return self._ds_local_exec

    @ds_local_exec.setter
    def ds_local_exec(self, value):
        self._ds_local_exec = value

    @property
    def nm_medico_aten_ext(self):
        return self._nm_medico_aten_ext

    @nm_medico_aten_ext.setter
    def nm_medico_aten_ext(self, value):
        self._nm_medico_aten_ext = value

    @property
    def crm_medico_aten_ext(self):
        return self._crm_medico_aten_ext

    @crm_medico_aten_ext.setter
    def crm_medico_aten_ext(self, value):
        self._crm_medico_aten_ext = value

    @property
    def nm_social(self):
        return self._nm_social

    @nm_social.setter
    def nm_social(self, value):
        self._nm_social = value

    @property
    def ds_email(self):
        return self._ds_email

    @ds_email.setter
    def ds_email(self, value):
        self._ds_email = value

    @property
    def nm_sobrenome_pai(self):
        return self._nm_sobrenome_pai

    @nm_sobrenome_pai.setter
    def nm_sobrenome_pai(self, value):
        self._nm_sobrenome_pai = value

    @property
    def nm_sobrenome_mae(self):
        return self._nm_sobrenome_mae

    @nm_sobrenome_mae.setter
    def nm_sobrenome_mae(self, value):
        self._nm_sobrenome_mae = value

    @property
    def nm_primeiro_nome(self):
        return self._nm_primeiro_nome

    @nm_primeiro_nome.setter
    def nm_primeiro_nome(self, value):
        self._nm_primeiro_nome = value

    @property
    def cancelado(self):
        return self._cancelado

    @cancelado.setter
    def cancelado(self, value):
        self._cancelado = value
