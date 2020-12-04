from ..models import usuario_model


def listar_usuario(login):
    u = usuario_model.UsuarioModel.query.filter_by(login=login).first()
    return u


def lista_usuario_por_id(identificador_pessoa):
    return usuario_model.UsuarioModel.query.filter_by(identificador_pessoa=identificador_pessoa).first()
