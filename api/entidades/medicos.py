"""Class to create doctors in database"""
from typing import Union, Optional
from ..services.constantes import IDENTIFICADOR_ESTABELECIMENTO_SAUDE_PADRAO
id_estab = IDENTIFICADOR_ESTABELECIMENTO_SAUDE_PADRAO


class Medicos:
    """
    Objeto que retorna um ProfissionalSaudeModel
    Entradas aceitas
        Required ->
            crm: [str, int] = 1º"<UF><NºCMR>" || 2º "<NºCMR><UF>" || 3º <NºCMR>
            **3º Require UF filled
        Optionals ->
            Nome: str = "Doctors name"
            uf: str = "UF" 2 digits only more or less will raise a except
            assinatura: bytes = "Jpeg from doctors signature"
            login: str = "default <uf><crm>
            identificador_estabelecimento_saude: int = <identificador> default is 1
            perfil: str = <perfil> ['ROLE_MEDICO_SOLICITANTE', 'ROLE_MEDICO_EXECUTOR, 'ROLE_ADMINISTRADOR',
            'ROLE_TECNICO', 'ROLE_VISUALIZADOR_GERAL']
    """
    def __init__(self,
                 crm: Union[int, str],
                 uf: Optional[str] = "",
                 nome: Optional[str] = "",
                 assinatura: Optional[bytes] = None,
                 login: Optional[str] = "",
                 identificador_estabelecimento_saude: Optional[int] = id_estab,
                 perfil: Optional[str] = 'ROLE_MEDICO_SOLICITANTE'
                 ) -> None:
        self.nome = nome
        self.crm = crm
        self.uf = uf if uf else crm
        self.assinatura = assinatura
        self.login = login if login else f"{self._uf.lower()}{self._crm}"
        self.identificador_estabelecimento_saude = identificador_estabelecimento_saude
        self.perfil = perfil

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, value):
        if isinstance(value, int):
            value = str(value)
        value = (''.join(filter(str.isdigit, value)) or None,
                 ''.join(filter(str.isalpha, value)) or None)
        self._crm = str(value[0])

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):
        if isinstance(value, str):
            try:
                value = (''.join(filter(str.isdigit, value)) or None,
                         ''.join(filter(str.isalpha, value)) or None)[1]
                self._uf = value.upper()
            except IndexError:
                raise ValueError('Um erro ocorreu ao tentar cadastrar o médico solicitante')
        else:
            raise AttributeError('UF Incorreta')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value:
            self._nome = value.upper()
        else:
            self._nome = ""

    @property
    def assinatura(self):
        return self._assinatura

    @assinatura.setter
    def assinatura(self, assinatura):
        self._assinatura = assinatura

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def identificador_estabelecimento_saude(self):
        return self._identificador_estabelecimento_saude

    @identificador_estabelecimento_saude.setter
    def identificador_estabelecimento_saude(self, identificador_estabelecimento_saude):
        self._identificador_estabelecimento_saude = identificador_estabelecimento_saude

    @property
    def perfil(self):
        return self._perfil

    @perfil.setter
    def perfil(self, perfil):
        self._perfil = perfil
