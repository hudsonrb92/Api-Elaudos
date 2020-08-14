from base64 import b64encode

from ..models import profissional_saude_model


def listar_profissional_por_id(identificador):
    profissional = profissional_saude_model.ProfissionalSaudeModel.query.filter_by(
        identificador=identificador).first()
    if profissional is not None:
        if profissional.assinatura_digitalizada is not None:
            profissional.assinatura_digitalizada = b64encode(
                profissional.assinatura_digitalizada)
            return profissional
        return profissional
