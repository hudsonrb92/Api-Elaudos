class LaudoEstudoDicom:
    def __init__(self, identificador, integrado):
        self.__identificador = identificador
        self.__integrado = integrado

        @property
        def identificador():
            return self.__identificador

        @identificador.setter
        def identificador(identificador_novo):
            self.__identificador = identificador_novo

        @property
        def integrado():
            return self.__integrado

        @integrado.setter
        def integrado(integrado_novo):
            self.__integrado = integrado_novo
