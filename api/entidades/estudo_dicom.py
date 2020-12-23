from sqlalchemy.orm.session import Session
from api import logger
from ..models.estudo_dicom_model import EstudoDicomModel as Edm
from datetime import date, time, datetime
from typing import Union, Optional
from uuid import uuid4
from ..services.tools import modalidade
from ..services.constantes import (
    IDENTIFICADOR_ESTABELECIMENTO_SAUDE_PADRAO, SITUACAO,
    NUMERO_EXAMES_HIS, IDENTIFICADOR_PRIORIDADE_ESTUDO_DICOM, SITUACAO_LAUDO,
    SEXO_DEFAULT, ORIGEM_ESTUDO_DICOM, IMAGENS_DISPONIVEIS, MODALIDADE_PADRAO)
id_est = IDENTIFICADOR_ESTABELECIMENTO_SAUDE_PADRAO
sit = SITUACAO
neh = NUMERO_EXAMES_HIS
iped = IDENTIFICADOR_PRIORIDADE_ESTUDO_DICOM
sitlau = SITUACAO_LAUDO
patsex = SEXO_DEFAULT
oriest = ORIGEM_ESTUDO_DICOM
ima_dis = IMAGENS_DISPONIVEIS
mod_padrao = MODALIDADE_PADRAO


class EstudoDicom:
    """Classe que gerencia Estudos Dicom e insere no banco de dados
    Esta classe trata os campos garantindo que não dará erro ao tentar inserir
    Itens obrigatórios para usar essa classe são:
        patientname str: [0:255]

    """
    def __init__(self,
                 patientname: str,
                 patientbirthdate: Union[str, date, datetime, None],
                 patientid: Union[str, int, None] = None,
                 studydescription: Optional[str] = None,
                 studydate: Union[str, datetime, date] = datetime.now().date(),
                 accessionnumber: Optional[str] = None,
                 modalitiesinstudy: str = mod_padrao,
                 studytime: Union[time, date, datetime, str] = str(datetime.now().time()),
                 studyinstanceuid: str = str(uuid4()),
                 imagens_disponiveis: bool = ima_dis,
                 origem_registro: str = oriest,
                 patientsex: str = patsex,
                 situacao_laudo: str = sitlau,
                 identificador_prioridade_estudo_dicom: str = iped,
                 numero_exames_ris: int = neh,
                 situacao: str = sit,
                 identificador_estabelecimento_saude: int = id_est,
                 medico_sol: int = None,
                 medico_dir: int = None):

        self.studyinstanceuid = studyinstanceuid
        self.accessionnumber = accessionnumber
        self.patientname = patientname
        self.patientid = patientid
        self.patientsex = patientsex
        self.patientbirthdate = patientbirthdate
        self.studydescription = studydescription
        self.modalitiesinstudy = modalidade(modalitiesinstudy)
        self.imagens_disponiveis = imagens_disponiveis
        self.origem_registro = origem_registro
        self.identificador_estabelecimento_saude = identificador_estabelecimento_saude
        self.studydate = studydate
        self.studytime = studytime
        self.situacao_laudo = situacao_laudo
        self.identificador_prioridade_estudo_dicom = identificador_prioridade_estudo_dicom
        self.numero_exames_ris = numero_exames_ris
        self.situacao = situacao
        self.medico_sol = medico_sol
        self.medico_dir = medico_dir

    @property
    def studyinstanceuid(self):
        return self._studyinstanceuid

    @property
    def accessionnumber(self):
        return self._accessionnumber

    @property
    def patientname(self):
        return self._patientname

    @property
    def patientid(self):
        return self._patientid

    @property
    def patientsex(self):
        return self._patientsex

    @property
    def patientbirthdate(self):
        return self._patientbirthdate

    @property
    def studydescription(self):
        return self._studydescription

    @property
    def modalitiesinstudy(self):
        return self._modalitiesinstudy

    @property
    def imagens_disponiveis(self):
        return self._imagens_disponiveis

    @property
    def origem_registro(self):
        return self._origem_registro

    @property
    def identificador_estabelecimento_saude(self):
        return self._identificador_estabelecimento_saude

    @property
    def studydate(self):
        return self._studydate

    @property
    def studytime(self):
        return self._studytime

    @property
    def situacao_laudo(self):
        return self._situacao_laudo

    @property
    def identificador_prioridade_estudo_dicom(self):
        return self._identificador_prioridade_estudo_dicom

    @property
    def numero_exames_ris(self):
        return self._numero_exames_ris

    @property
    def situacao(self):
        return self._situacao

    @property
    def medico_sol(self):
        return self._medico_sol

    @property
    def medico_dir(self):
        return self._medico_dir

    @studytime.setter
    def studytime(self, studytime):
        if isinstance(studytime, str):
            self._studytime = studytime
        elif isinstance(studytime, time) or isinstance(studytime, datetime):
            studytime = f"{studytime.hour:02}:{studytime.minute:02}{studytime.second:02}"
            self._studytime = studytime
        else:
            self._studytime = None

    @imagens_disponiveis.setter
    def imagens_disponiveis(self, value):
        if isinstance(value, bool):
            self._imagens_disponiveis = value
        else:
            self._imagens_disponiveis = False

    @origem_registro.setter
    def origem_registro(self, origem_registro):
        if not isinstance(origem_registro, str):
            origem_registro = 'W'
            self._origem_registro = origem_registro
        elif isinstance(origem_registro, str) and origem_registro in ['W', 'P']:
            self._origem_registro = origem_registro
        else:
            self._origem_registro = 'W'

    @identificador_estabelecimento_saude.setter
    def identificador_estabelecimento_saude(self, identificador_estabelecimento_saude):
        if isinstance(identificador_estabelecimento_saude, str):
            try:
                identificador_estabelecimento_saude = int(identificador_estabelecimento_saude)
                self._identificador_estabelecimento_saude = identificador_estabelecimento_saude
            except Exception as expt:
                raise TypeError(f"Tipo do identificador do estabelecimento de saude incorreto. {expt}")
        elif not identificador_estabelecimento_saude:
            self._identificador_estabelecimento_saude = id_est
        else:
            self._identificador_estabelecimento_saude = identificador_estabelecimento_saude

    @studyinstanceuid.setter
    def studyinstanceuid(self, value):
        if not value:
            value = str(uuid4())
            self._studyinstanceuid = value
        else:
            self._studyinstanceuid = value

    @accessionnumber.setter
    def accessionnumber(self, accessionnumber):
        self._accessionnumber = str(accessionnumber)

    @patientname.setter
    def patientname(self, value):
        if value:
            self._patientname = value.upper()
        else:
            self._patientname = value

    @patientid.setter
    def patientid(self, patientid):
        self._patientid = str(patientid)

    @patientsex.setter
    def patientsex(self, patientsex):
        self._patientsex = patientsex

    @patientbirthdate.setter
    def patientbirthdate(self, patientbirthdate):
        self._patientbirthdate = str(patientbirthdate).replace('-','')

    @studydescription.setter
    def studydescription(self, studydescription):
        self._studydescription = str(studydescription)[0:64]

    @modalitiesinstudy.setter
    def modalitiesinstudy(self, modalitiesinstudy):
        self._modalitiesinstudy = modalitiesinstudy

    @studydate.setter
    def studydate(self, studydate):
        self._studydate = studydate

    @situacao_laudo.setter
    def situacao_laudo(self, situacao_laudo):
        self._situacao_laudo = situacao_laudo

    @identificador_prioridade_estudo_dicom.setter
    def identificador_prioridade_estudo_dicom(self, identificador_prioridade_estudo_dicom):
        self._identificador_prioridade_estudo_dicom = identificador_prioridade_estudo_dicom

    @numero_exames_ris.setter
    def numero_exames_ris(self, numero_exames_ris):
        self._numero_exames_ris = numero_exames_ris

    @situacao.setter
    def situacao(self, situacao):
        self._situacao = situacao

    @medico_sol.setter
    def medico_sol(self, medico_sol):
        self._medico_sol = medico_sol

    @medico_dir.setter
    def medico_dir(self, medico_dir):
        self._medico_dir = medico_dir
