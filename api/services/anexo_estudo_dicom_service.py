from base64 import b64encode

from ..models import anexo_estudo_dicom_model


def listar_anexo_por_identificador_estudo(identificador):
    anexos = anexo_estudo_dicom_model.AnexoEstudoDicomModel.query.filter_by(
        identificador_estudo_dicom=identificador).all()
    if len(anexos) > 0:
        for anexo in anexos:
            if anexo.conteudo_arquivo:
                anexo.conteudo_arquivo = b64encode(anexo.conteudo_arquivo)
        return anexos
    else:
        return None


def listar_anexo_por_identificador(identificador):
    anexo = anexo_estudo_dicom_model.AnexoEstudoDicomModel.query.filter_by(
        identificador=identificador).first()
    if anexo:
        anexo.conteudo_arquivo = b64encode(anexo.conteudo_arquivo)
        return anexo
    else:
        return None
