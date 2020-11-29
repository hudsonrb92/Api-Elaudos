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
            ds_observacao_pf: Optional[str] = "",
            ds_unidade_atend: Optional[str] = "",
            ds_plano: Optional[str] = "",
            dt_admissao_hosp: Optional[str] = "",
            uf_medico: Optional[str] = "",
            ds_local: Optional[str] = "",
            ds_local_exec: Optional[str] = "",
            nm_medico_aten_ext: Optional[str] = "",
            crm_medico_aten_ext: Optional[str] = "",
            nm_social: Optional[str] = "",
            ds_email: Optional[str] = "") -> None:

        self.__nr_atendimento = nr_atendimento
        self.__nr_prescricao = nr_prescricao
        self.__nr_sequencia = nr_sequencia
        self.__nr_seq_interno = nr_seq_interno
        self.__nr_acess_number = nr_acess_number
        self.__cd_proced_tasy = str(cd_proced_tasy)
        self.__cd_proced_integracao = str(cd_proced_integracao)
        self.__cd_proced_tasy_lado = str(cd_proced_tasy_lado)
        self.__ds_procedimento = str(ds_procedimento)
        self.__ie_lado = ie_lado
        self.__ie_urgencia = ie_urgencia
        self.__dt_prev_execucao = dt_prev_execucao
        self.__cd_setor_paciente = str(cd_setor_paciente)
        self.__cd_estabelecimento = str(cd_estabelecimento)
        self.__nm_pessoa_fisica = nm_pessoa_fisica
        self.__dt_prescricao = dt_prescricao
        self.__cd_setor_execucao = str(cd_setor_execucao)
        self.__dt_liberacao = dt_liberacao
        self.__cd_software_integracao = str(cd_software_integracao)
        self.__cd_estab_terceiro = str(cd_estab_terceiro)
        self.__cd_paciente = str(cd_paciente)
        self.__cd_prescritor = str(cd_prescritor)
        self.__ie_sexo = ie_sexo
        self.__dt_nascimento = dt_nascimento
        self.__cd_integracao_proc_interno = str(cd_integracao_proc_interno)
        self.__qt_altura_cm = qt_altura_cm
        self.__qt_idade_pac = qt_idade_pac
        self.__qt_peso = qt_peso
        self.__nr_crm_prescritor = nr_crm_prescritor
        self.__cd_modalidade_proc = str(cd_modalidade_proc)
        self.__uf_crm_prescritor = uf_crm_prescritor
        self.__nr_cpf_paciente = nr_cpf_paciente
        self.__qt_prescrito = qt_prescrito
        self.__nr_identidade_paciente = nr_identidade_paciente
        self.__nr_prontuario_paciente = nr_prontuario_paciente
        self.__ds_endereco_paciente = ds_endereco_paciente
        self.__nr_endereco_paciente = nr_endereco_paciente
        self.__ds_bairro_paciente = str(ds_bairro_paciente)
        self.__ds_municipio_paciente = ds_municipio_paciente
        self.__uf_paciente = uf_paciente
        self.__cd_cep_paciente = str(cd_cep_paciente)
        self.__nr_telefone_paciente = nr_telefone_paciente
        self.__cd_convenio = str(cd_convenio)
        self.__ds_categoria_convenio = ds_categoria_convenio
        self.__ds_convenio = str(ds_convenio)
        self.__cd_cgc = str(cd_cgc)
        self.__nr_seq_motivo_atend = nr_seq_motivo_atend
        self.__ds_motivo_atend = str(ds_motivo_atend)
        self.__ds_motivo_suspensao = ds_motivo_suspensao
        self.__cd_pessoa_fisica = str(cd_pessoa_fisica)
        self.__cd_procedimento = str(cd_procedimento)
        self.__cd_tipo_procedimento = str(cd_tipo_procedimento)
        self.__qt_procedimento = qt_procedimento
        self.__dt_atualizacao = dt_atualizacao
        self.__nm_usuario = nm_usuario
        self.__ds_observacao = str(ds_observacao)
        self.__ie_origem_proced = ie_origem_proced
        self.__ds_dado_clinico = str(ds_dado_clinico)
        self.__ie_suspenso = ie_suspenso
        self.__cd_setor_atendimento = str(cd_setor_atendimento)
        self.__cd_medico = str(cd_medico)
        self.__dt_liberacao_medico = dt_liberacao_medico
        self.__ie_recem_nato = ie_recem_nato
        self.__nm_paciente = nm_paciente
        self.__nr_cpf = nr_cpf
        self.__nr_prontuario = nr_prontuario
        self.__nm_medico = nm_medico
        self.__nr_crm = nr_crm
        self.__cd_categoria = str(cd_categoria)
        self.__cd_usuario_convenio = str(cd_usuario_convenio)
        self.__cd_material_exame = str(cd_material_exame)
        self.__ds_material_especial = ds_material_especial
        self.__ie_amostra_entregue = ie_amostra_entregue
        self.__ds_horarios = str(ds_horarios)
        self.__nr_seq_exame = nr_seq_exame
        self.__ds_endereco = str(ds_endereco)
        self.__nr_endereco = nr_endereco
        self.__ds_complemento = str(ds_complemento)
        self.__ds_bairro = str(ds_bairro)
        self.__ds_municipio = str(ds_municipio)
        self.__sg_estado = sg_estado
        self.__nr_telefone = nr_telefone
        self.__cd_cep = str(cd_cep)
        self.__ds_setor_paciente = str(ds_setor_paciente)
        self.__cd_unidade = str(cd_unidade)
        self.__ie_executar_leito = ie_executar_leito
        self.__ds_modalidade = str(ds_modalidade)
        self.__na_accessionnumber = na_accessionnumber
        self.__ie_tipo_atendimento = ie_tipo_atendimento
        self.__nr_seq_proc_interno = nr_seq_proc_interno
        self.__cd_plano_convenio = str(cd_plano_convenio)
        self.__cd_plano = str(cd_plano)
        self.__cd_agenda = str(cd_agenda)
        self.__ds_agenda = str(ds_agenda)
        self.__cd_procedencia = str(cd_procedencia)
        self.__ds_procedencia = str(ds_procedencia)
        self.__cd_compl_conv = str(cd_compl_conv)
        self.__dt_validade_carteira = str(dt_validade_carteira)
        self.__dt_resultado = str(dt_resultado)
        self.__ds_senha = str(ds_senha)
        self.__nr_cpf_medico = nr_cpf_medico
        self.__cd_estab_atend = str(cd_estab_atend)
        self.__cd_estab_prescr = str(cd_estab_prescr)
        self.__dt_entrada = dt_entrada
        self.__ds_tipo_atendimento = ds_tipo_atendimento
        self.__ds_observacao_pf = str(ds_observacao_pf)
        self.__ds_unidade_atend = str(ds_unidade_atend)
        self.__ds_plano = str(ds_plano)
        self.__dt_admissao_hosp = str(dt_admissao_hosp)
        self.__uf_medico = uf_medico
        self.__ds_local = str(ds_local)
        self.__ds_local_exec = str(ds_local_exec)
        self.__nm_medico_aten_ext = nm_medico_aten_ext
        self.__crm_medico_aten_ext = crm_medico_aten_ext
        self.__nm_social = nm_social
        self.__ds_email = str(ds_email)

    @property
    def nr_atendimento(self):
        return self.__nr_atendimento

    @nr_atendimento.setter
    def nr_atendimento(self, nr_atendimento):
        self.__nr_atendimento = nr_atendimento

    @property
    def nr_prescricao(self):
        return self.__nr_prescricao

    @nr_prescricao.setter
    def nr_prescricao(self, nr_prescricao):
        self.__nr_prescricao = nr_prescricao

    @property
    def nr_sequencia(self):
        return self.__nr_sequencia

    @nr_sequencia.setter
    def nr_sequencia(self, nr_sequencia):
        self.__nr_sequencia = nr_sequencia

    @property
    def nr_seq_interno(self):
        return self.__nr_seq_interno

    @nr_seq_interno.setter
    def nr_seq_interno(self, nr_seq_interno):
        self.__nr_seq_interno = nr_seq_interno

    @property
    def nr_acess_number(self):
        return self.__nr_acess_number

    @nr_acess_number.setter
    def nr_acess_number(self, nr_acess_number):
        self.__nr_acess_number = nr_acess_number

    @property
    def cd_proced_tasy(self):
        return self.__cd_proced_tasy

    @cd_proced_tasy.setter
    def cd_proced_tasy(self, cd_proced_tasy):
        self.__cd_proced_tasy = cd_proced_tasy

    @property
    def cd_proced_integracao(self):
        return self.__cd_proced_integracao

    @cd_proced_integracao.setter
    def cd_proced_integracao(self, cd_proced_integracao):
        self.__cd_proced_integracao = cd_proced_integracao

    @property
    def cd_proced_tasy_lado(self):
        return self.__cd_proced_tasy_lado

    @cd_proced_tasy_lado.setter
    def cd_proced_tasy_lado(self, cd_proced_tasy_lado):
        self.__cd_proced_tasy_lado = cd_proced_tasy_lado

    @property
    def ds_procedimento(self):
        return self.__ds_procedimento

    @ds_procedimento.setter
    def ds_procedimento(self, ds_procedimento):
        self.__ds_procedimento = ds_procedimento

    @property
    def ie_lado(self):
        return self.__ie_lado

    @ie_lado.setter
    def ie_lado(self, ie_lado):
        self.__ie_lado = ie_lado

    @property
    def ie_urgencia(self):
        return self.__ie_urgencia

    @ie_urgencia.setter
    def ie_urgencia(self, ie_urgencia):
        self.__ie_urgencia = ie_urgencia

    @property
    def dt_prev_execucao(self):
        return self.__dt_prev_execucao

    @dt_prev_execucao.setter
    def dt_prev_execucao(self, dt_prev_execucao):
        self.__dt_prev_execucao = dt_prev_execucao

    @property
    def cd_setor_paciente(self):
        return self.__cd_setor_paciente

    @cd_setor_paciente.setter
    def cd_setor_paciente(self, cd_setor_paciente):
        self.__cd_setor_paciente = cd_setor_paciente

    @property
    def cd_estabelecimento(self):
        return self.__cd_estabelecimento

    @cd_estabelecimento.setter
    def cd_estabelecimento(self, cd_estabelecimento):
        self.__cd_estabelecimento = cd_estabelecimento

    @property
    def nm_pessoa_fisica(self):
        return self.__nm_pessoa_fisica

    @nm_pessoa_fisica.setter
    def nm_pessoa_fisica(self, nm_pessoa_fisica):
        self.__nm_pessoa_fisica = nm_pessoa_fisica

    @property
    def dt_prescricao(self):
        return self.__dt_prescricao

    @dt_prescricao.setter
    def dt_prescricao(self, dt_prescricao):
        self.__dt_prescricao = dt_prescricao

    @property
    def cd_setor_execucao(self):
        return self.__cd_setor_execucao

    @cd_setor_execucao.setter
    def cd_setor_execucao(self, cd_setor_execucao):
        self.__cd_setor_execucao = cd_setor_execucao

    @property
    def dt_liberacao(self):
        return self.__dt_liberacao

    @dt_liberacao.setter
    def dt_liberacao(self, dt_liberacao):
        self.__dt_liberacao = dt_liberacao

    @property
    def cd_software_integracao(self):
        return self.__cd_software_integracao

    @cd_software_integracao.setter
    def cd_software_integracao(self, cd_software_integracao):
        self.__cd_software_integracao = cd_software_integracao

    @property
    def cd_estab_terceiro(self):
        return self.__cd_estab_terceiro

    @cd_estab_terceiro.setter
    def cd_estab_terceiro(self, cd_estab_terceiro):
        self.__cd_estab_terceiro = cd_estab_terceiro

    @property
    def cd_paciente(self):
        return self.__cd_paciente

    @cd_paciente.setter
    def cd_paciente(self, cd_paciente):
        self.__cd_paciente = cd_paciente

    @property
    def cd_prescritor(self):
        return self.__cd_prescritor

    @cd_prescritor.setter
    def cd_prescritor(self, cd_prescritor):
        self.__cd_prescritor = cd_prescritor

    @property
    def ie_sexo(self):
        return self.__ie_sexo

    @ie_sexo.setter
    def ie_sexo(self, ie_sexo):
        self.__ie_sexo = ie_sexo

    @property
    def dt_nascimento(self):
        return self.__dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento):
        self.__dt_nascimento = dt_nascimento

    @property
    def cd_integracao_proc_interno(self):
        return self.__cd_integracao_proc_interno

    @cd_integracao_proc_interno.setter
    def cd_integracao_proc_interno(self, cd_integracao_proc_interno):
        self.__cd_integracao_proc_interno = cd_integracao_proc_interno

    @property
    def qt_altura_cm(self):
        return self.__qt_altura_cm

    @qt_altura_cm.setter
    def qt_altura_cm(self, qt_altura_cm):
        self.__qt_altura_cm = qt_altura_cm

    @property
    def qt_idade_pac(self):
        return self.__qt_idade_pac

    @qt_idade_pac.setter
    def qt_idade_pac(self, qt_idade_pac):
        self.__qt_idade_pac = qt_idade_pac

    @property
    def qt_peso(self):
        return self.__qt_peso

    @qt_peso.setter
    def qt_peso(self, qt_peso):
        self.__qt_peso = qt_peso

    @property
    def nr_crm_prescritor(self):
        return self.__nr_crm_prescritor

    @nr_crm_prescritor.setter
    def nr_crm_prescritor(self, nr_crm_prescritor):
        self.__nr_crm_prescritor = nr_crm_prescritor

    @property
    def cd_modalidade_proc(self):
        return self.__cd_modalidade_proc

    @cd_modalidade_proc.setter
    def cd_modalidade_proc(self, cd_modalidade_proc):
        self.__cd_modalidade_proc = cd_modalidade_proc

    @property
    def uf_crm_prescritor(self):
        return self.__uf_crm_prescritor

    @uf_crm_prescritor.setter
    def uf_crm_prescritor(self, uf_crm_prescritor):
        self.__uf_crm_prescritor = uf_crm_prescritor

    @property
    def nr_cpf_paciente(self):
        return self.__nr_cpf_paciente

    @nr_cpf_paciente.setter
    def nr_cpf_paciente(self, nr_cpf_paciente):
        self.__nr_cpf_paciente = nr_cpf_paciente

    @property
    def qt_prescrito(self):
        return self.__qt_prescrito

    @qt_prescrito.setter
    def qt_prescrito(self, qt_prescrito):
        self.__qt_prescrito = qt_prescrito

    @property
    def nr_identidade_paciente(self):
        return self.__nr_identidade_paciente

    @nr_identidade_paciente.setter
    def nr_identidade_paciente(self, nr_identidade_paciente):
        self.__nr_identidade_paciente = nr_identidade_paciente

    @property
    def nr_prontuario_paciente(self):
        return self.__nr_prontuario_paciente

    @nr_prontuario_paciente.setter
    def nr_prontuario_paciente(self, nr_prontuario_paciente):
        self.__nr_prontuario_paciente = nr_prontuario_paciente

    @property
    def ds_endereco_paciente(self):
        return self.__ds_endereco_paciente

    @ds_endereco_paciente.setter
    def ds_endereco_paciente(self, ds_endereco_paciente):
        self.__ds_endereco_paciente = ds_endereco_paciente

    @property
    def nr_endereco_paciente(self):
        return self.__nr_endereco_paciente

    @nr_endereco_paciente.setter
    def nr_endereco_paciente(self, nr_endereco_paciente):
        self.__nr_endereco_paciente = nr_endereco_paciente

    @property
    def ds_bairro_paciente(self):
        return self.__ds_bairro_paciente

    @ds_bairro_paciente.setter
    def ds_bairro_paciente(self, ds_bairro_paciente):
        self.__ds_bairro_paciente = ds_bairro_paciente

    @property
    def ds_municipio_paciente(self):
        return self.__ds_municipio_paciente

    @ds_municipio_paciente.setter
    def ds_municipio_paciente(self, ds_municipio_paciente):
        self.__ds_municipio_paciente = ds_municipio_paciente

    @property
    def uf_paciente(self):
        return self.__uf_paciente

    @uf_paciente.setter
    def uf_paciente(self, uf_paciente):
        self.__uf_paciente = uf_paciente

    @property
    def cd_cep_paciente(self):
        return self.__cd_cep_paciente

    @cd_cep_paciente.setter
    def cd_cep_paciente(self, cd_cep_paciente):
        self.__cd_cep_paciente = cd_cep_paciente

    @property
    def nr_telefone_paciente(self):
        return self.__nr_telefone_paciente

    @nr_telefone_paciente.setter
    def nr_telefone_paciente(self, nr_telefone_paciente):
        self.__nr_telefone_paciente = nr_telefone_paciente

    @property
    def cd_convenio(self):
        return self.__cd_convenio

    @cd_convenio.setter
    def cd_convenio(self, cd_convenio):
        self.__cd_convenio = cd_convenio

    @property
    def ds_categoria_convenio(self):
        return self.__ds_categoria_convenio

    @ds_categoria_convenio.setter
    def ds_categoria_convenio(self, ds_categoria_convenio):
        self.__ds_categoria_convenio = ds_categoria_convenio

    @property
    def ds_convenio(self):
        return self.__ds_convenio

    @ds_convenio.setter
    def ds_convenio(self, ds_convenio):
        self.__ds_convenio = ds_convenio

    @property
    def cd_cgc(self):
        return self.__cd_cgc

    @cd_cgc.setter
    def cd_cgc(self, cd_cgc):
        self.__cd_cgc = cd_cgc

    @property
    def nr_seq_motivo_atend(self):
        return self.__nr_seq_motivo_atend

    @nr_seq_motivo_atend.setter
    def nr_seq_motivo_atend(self, nr_seq_motivo_atend):
        self.__nr_seq_motivo_atend = nr_seq_motivo_atend

    @property
    def ds_motivo_atend(self):
        return self.__ds_motivo_atend

    @ds_motivo_atend.setter
    def ds_motivo_atend(self, ds_motivo_atend):
        self.__ds_motivo_atend = ds_motivo_atend

    @property
    def ds_motivo_suspensao(self):
        return self.__ds_motivo_suspensao

    @ds_motivo_suspensao.setter
    def ds_motivo_suspensao(self, ds_motivo_suspensao):
        self.__ds_motivo_suspensao = ds_motivo_suspensao

    @property
    def cd_pessoa_fisica(self):
        return self.__cd_pessoa_fisica

    @cd_pessoa_fisica.setter
    def cd_pessoa_fisica(self, cd_pessoa_fisica):
        self.__cd_pessoa_fisica = cd_pessoa_fisica

    @property
    def cd_procedimento(self):
        return self.__cd_procedimento

    @cd_procedimento.setter
    def cd_procedimento(self, cd_procedimento):
        self.__cd_procedimento = cd_procedimento

    @property
    def cd_tipo_procedimento(self):
        return self.__cd_tipo_procedimento

    @cd_tipo_procedimento.setter
    def cd_tipo_procedimento(self, cd_tipo_procedimento):
        self.__cd_tipo_procedimento = cd_tipo_procedimento

    @property
    def qt_procedimento(self):
        return self.__qt_procedimento

    @qt_procedimento.setter
    def qt_procedimento(self, qt_procedimento):
        self.__qt_procedimento = qt_procedimento

    @property
    def dt_atualizacao(self):
        return self.__dt_atualizacao

    @dt_atualizacao.setter
    def dt_atualizacao(self, dt_atualizacao):
        self.__dt_atualizacao = dt_atualizacao

    @property
    def nm_usuario(self):
        return self.__nm_usuario

    @nm_usuario.setter
    def nm_usuario(self, nm_usuario):
        self.__nm_usuario = nm_usuario

    @property
    def ds_observacao(self):
        return self.__ds_observacao

    @ds_observacao.setter
    def ds_observacao(self, ds_observacao):
        self.__ds_observacao = ds_observacao

    @property
    def ie_origem_proced(self):
        return self.__ie_origem_proced

    @ie_origem_proced.setter
    def ie_origem_proced(self, ie_origem_proced):
        self.__ie_origem_proced = ie_origem_proced

    @property
    def ds_dado_clinico(self):
        return self.__ds_dado_clinico

    @ds_dado_clinico.setter
    def ds_dado_clinico(self, ds_dado_clinico):
        self.__ds_dado_clinico = ds_dado_clinico

    @property
    def ie_suspenso(self):
        return self.__ie_suspenso

    @ie_suspenso.setter
    def ie_suspenso(self, ie_suspenso):
        self.__ie_suspenso = ie_suspenso

    @property
    def cd_setor_atendimento(self):
        return self.__cd_setor_atendimento

    @cd_setor_atendimento.setter
    def cd_setor_atendimento(self, cd_setor_atendimento):
        self.__cd_setor_atendimento = cd_setor_atendimento

    @property
    def cd_medico(self):
        return self.__cd_medico

    @cd_medico.setter
    def cd_medico(self, cd_medico):
        self.__cd_medico = cd_medico

    @property
    def dt_liberacao_medico(self):
        return self.__dt_liberacao_medico

    @dt_liberacao_medico.setter
    def dt_liberacao_medico(self, dt_liberacao_medico):
        self.__dt_liberacao_medico = dt_liberacao_medico

    @property
    def ie_recem_nato(self):
        return self.__ie_recem_nato

    @ie_recem_nato.setter
    def ie_recem_nato(self, ie_recem_nato):
        self.__ie_recem_nato = ie_recem_nato

    @property
    def nm_paciente(self):
        return self.__nm_paciente

    @nm_paciente.setter
    def nm_paciente(self, nm_paciente):
        self.__nm_paciente = nm_paciente

    @property
    def nr_cpf(self):
        return self.__nr_cpf

    @nr_cpf.setter
    def nr_cpf(self, nr_cpf):
        self.__nr_cpf = nr_cpf

    @property
    def nr_prontuario(self):
        return self.__nr_prontuario

    @nr_prontuario.setter
    def nr_prontuario(self, nr_prontuario):
        self.__nr_prontuario = nr_prontuario

    @property
    def nm_medico(self):
        return self.__nm_medico

    @nm_medico.setter
    def nm_medico(self, nm_medico):
        self.__nm_medico = nm_medico

    @property
    def nr_crm(self):
        return self.__nr_crm

    @nr_crm.setter
    def nr_crm(self, nr_crm):
        self.__nr_crm = nr_crm

    @property
    def cd_categoria(self):
        return self.__cd_categoria

    @cd_categoria.setter
    def cd_categoria(self, cd_categoria):
        self.__cd_categoria = cd_categoria

    @property
    def cd_usuario_convenio(self):
        return self.__cd_usuario_convenio

    @cd_usuario_convenio.setter
    def cd_usuario_convenio(self, cd_usuario_convenio):
        self.__cd_usuario_convenio = cd_usuario_convenio

    @property
    def cd_material_exame(self):
        return self.__cd_material_exame

    @cd_material_exame.setter
    def cd_material_exame(self, cd_material_exame):
        self.__cd_material_exame = cd_material_exame

    @property
    def ds_material_especial(self):
        return self.__ds_material_especial

    @ds_material_especial.setter
    def ds_material_especial(self, ds_material_especial):
        self.__ds_material_especial = ds_material_especial

    @property
    def ie_amostra_entregue(self):
        return self.__ie_amostra_entregue

    @ie_amostra_entregue.setter
    def ie_amostra_entregue(self, ie_amostra_entregue):
        self.__ie_amostra_entregue = ie_amostra_entregue

    @property
    def ds_horarios(self):
        return self.__ds_horarios

    @ds_horarios.setter
    def ds_horarios(self, ds_horarios):
        self.__ds_horarios = ds_horarios

    @property
    def nr_seq_exame(self):
        return self.__nr_seq_exame

    @nr_seq_exame.setter
    def nr_seq_exame(self, nr_seq_exame):
        self.__nr_seq_exame = nr_seq_exame

    @property
    def ds_endereco(self):
        return self.__ds_endereco

    @ds_endereco.setter
    def ds_endereco(self, ds_endereco):
        self.__ds_endereco = ds_endereco

    @property
    def nr_endereco(self):
        return self.__nr_endereco

    @nr_endereco.setter
    def nr_endereco(self, nr_endereco):
        self.__nr_endereco = nr_endereco

    @property
    def ds_complemento(self):
        return self.__ds_complemento

    @ds_complemento.setter
    def ds_complemento(self, ds_complemento):
        self.__ds_complemento = ds_complemento

    @property
    def ds_bairro(self):
        return self.__ds_bairro

    @ds_bairro.setter
    def ds_bairro(self, ds_bairro):
        self.__ds_bairro = ds_bairro

    @property
    def ds_municipio(self):
        return self.__ds_municipio

    @ds_municipio.setter
    def ds_municipio(self, ds_municipio):
        self.__ds_municipio = ds_municipio

    @property
    def sg_estado(self):
        return self.__sg_estado

    @sg_estado.setter
    def sg_estado(self, sg_estado):
        self.__sg_estado = sg_estado

    @property
    def nr_telefone(self):
        return self.__nr_telefone

    @nr_telefone.setter
    def nr_telefone(self, nr_telefone):
        self.__nr_telefone = nr_telefone

    @property
    def cd_cep(self):
        return self.__cd_cep

    @cd_cep.setter
    def cd_cep(self, cd_cep):
        self.__cd_cep = cd_cep

    @property
    def ds_setor_paciente(self):
        return self.__ds_setor_paciente

    @ds_setor_paciente.setter
    def ds_setor_paciente(self, ds_setor_paciente):
        self.__ds_setor_paciente = ds_setor_paciente

    @property
    def cd_unidade(self):
        return self.__cd_unidade

    @cd_unidade.setter
    def cd_unidade(self, cd_unidade):
        self.__cd_unidade = cd_unidade

    @property
    def ie_executar_leito(self):
        return self.__ie_executar_leito

    @ie_executar_leito.setter
    def ie_executar_leito(self, ie_executar_leito):
        self.__ie_executar_leito = ie_executar_leito

    @property
    def ds_modalidade(self):
        return self.__ds_modalidade

    @ds_modalidade.setter
    def ds_modalidade(self, ds_modalidade):
        self.__ds_modalidade = ds_modalidade

    @property
    def na_accessionnumber(self):
        return self.__na_accessionnumber

    @na_accessionnumber.setter
    def na_accessionnumber(self, na_accessionnumber):
        self.__na_accessionnumber = na_accessionnumber

    @property
    def ie_tipo_atendimento(self):
        return self.__ie_tipo_atendimento

    @ie_tipo_atendimento.setter
    def ie_tipo_atendimento(self, ie_tipo_atendimento):
        self.__ie_tipo_atendimento = ie_tipo_atendimento

    @property
    def nr_seq_proc_interno(self):
        return self.__nr_seq_proc_interno

    @nr_seq_proc_interno.setter
    def nr_seq_proc_interno(self, nr_seq_proc_interno):
        self.__nr_seq_proc_interno = nr_seq_proc_interno

    @property
    def cd_plano_convenio(self):
        return self.__cd_plano_convenio

    @cd_plano_convenio.setter
    def cd_plano_convenio(self, cd_plano_convenio):
        self.__cd_plano_convenio = cd_plano_convenio

    @property
    def cd_plano(self):
        return self.__cd_plano

    @cd_plano.setter
    def cd_plano(self, cd_plano):
        self.__cd_plano = cd_plano

    @property
    def cd_agenda(self):
        return self.__cd_agenda

    @cd_agenda.setter
    def cd_agenda(self, cd_agenda):
        self.__cd_agenda = cd_agenda

    @property
    def ds_agenda(self):
        return self.__ds_agenda

    @ds_agenda.setter
    def ds_agenda(self, ds_agenda):
        self.__ds_agenda = ds_agenda

    @property
    def cd_procedencia(self):
        return self.__cd_procedencia

    @cd_procedencia.setter
    def cd_procedencia(self, cd_procedencia):
        self.__cd_procedencia = cd_procedencia

    @property
    def ds_procedencia(self):
        return self.__ds_procedencia

    @ds_procedencia.setter
    def ds_procedencia(self, ds_procedencia):
        self.__ds_procedencia = ds_procedencia

    @property
    def cd_compl_conv(self):
        return self.__cd_compl_conv

    @cd_compl_conv.setter
    def cd_compl_conv(self, cd_compl_conv):
        self.__cd_compl_conv = cd_compl_conv

    @property
    def dt_validade_carteira(self):
        return self.__dt_validade_carteira

    @dt_validade_carteira.setter
    def dt_validade_carteira(self, dt_validade_carteira):
        self.__dt_validade_carteira = dt_validade_carteira

    @property
    def dt_resultado(self):
        return self.__dt_resultado

    @dt_resultado.setter
    def dt_resultado(self, dt_resultado):
        self.__dt_resultado = dt_resultado

    @property
    def ds_senha(self):
        return self.__ds_senha

    @ds_senha.setter
    def ds_senha(self, ds_senha):
        self.__ds_senha = ds_senha

    @property
    def nr_cpf_medico(self):
        return self.__nr_cpf_medico

    @nr_cpf_medico.setter
    def nr_cpf_medico(self, nr_cpf_medico):
        self.__nr_cpf_medico = nr_cpf_medico

    @property
    def cd_estab_atend(self):
        return self.__cd_estab_atend

    @cd_estab_atend.setter
    def cd_estab_atend(self, cd_estab_atend):
        self.__cd_estab_atend = cd_estab_atend

    @property
    def cd_estab_prescr(self):
        return self.__cd_estab_prescr

    @cd_estab_prescr.setter
    def cd_estab_prescr(self, cd_estab_prescr):
        self.__cd_estab_prescr = cd_estab_prescr

    @property
    def dt_entrada(self):
        return self.__dt_entrada

    @dt_entrada.setter
    def dt_entrada(self, dt_entrada):
        self.__dt_entrada = dt_entrada

    @property
    def ds_tipo_atendimento(self):
        return self.__ds_tipo_atendimento

    @ds_tipo_atendimento.setter
    def ds_tipo_atendimento(self, ds_tipo_atendimento):
        self.__ds_tipo_atendimento = ds_tipo_atendimento

    @property
    def ds_observacao_pf(self):
        return self.__ds_observacao_pf

    @ds_observacao_pf.setter
    def ds_observacao_pf(self, ds_observacao_pf):
        self.__ds_observacao_pf = ds_observacao_pf

    @property
    def ds_unidade_atend(self):
        return self.__ds_unidade_atend

    @ds_unidade_atend.setter
    def ds_unidade_atend(self, ds_unidade_atend):
        self.__ds_unidade_atend = ds_unidade_atend

    @property
    def ds_plano(self):
        return self.__ds_plano

    @ds_plano.setter
    def ds_plano(self, ds_plano):
        self.__ds_plano = ds_plano

    @property
    def dt_admissao_hosp(self):
        return self.__dt_admissao_hosp

    @dt_admissao_hosp.setter
    def dt_admissao_hosp(self, dt_admissao_hosp):
        self.__dt_admissao_hosp = dt_admissao_hosp

    @property
    def uf_medico(self):
        return self.__uf_medico

    @uf_medico.setter
    def uf_medico(self, uf_medico):
        self.__uf_medico = uf_medico

    @property
    def ds_local(self):
        return self.__ds_local

    @ds_local.setter
    def ds_local(self, ds_local):
        self.__ds_local = ds_local

    @property
    def ds_local_exec(self):
        return self.__ds_local_exec

    @ds_local_exec.setter
    def ds_local_exec(self, ds_local_exec):
        self.__ds_local_exec = ds_local_exec

    @property
    def nm_medico_aten_ext(self):
        return self.__nm_medico_aten_ext

    @nm_medico_aten_ext.setter
    def nm_medico_aten_ext(self, nm_medico_aten_ext):
        self.__nm_medico_aten_ext = nm_medico_aten_ext

    @property
    def crm_medico_aten_ext(self):
        return self.__crm_medico_aten_ext

    @crm_medico_aten_ext.setter
    def crm_medico_aten_ext(self, crm_medico_aten_ext):
        self.__crm_medico_aten_ext = crm_medico_aten_ext

    @property
    def nm_social(self):
        return self.__nm_social

    @nm_social.setter
    def nm_social(self, nm_social):
        self.__nm_social = nm_social

    @property
    def ds_email(self):
        return self.__ds_email

    @ds_email.setter
    def ds_email(self, ds_email):
        self.__ds_email = ds_email