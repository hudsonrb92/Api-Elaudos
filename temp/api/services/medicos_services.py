import hashlib

from ..models import (profissional_saude_model, usuario_model,
                      perfil_usuario_estabelecimento_saude_model, pessoa_model,
                      estado_model)
from api import logger, db
from base64 import b64decode

psm = profissional_saude_model.ProfissionalSaudeModel
usr = usuario_model.UsuarioModel
pm = pessoa_model.PessoaModel
pues = perfil_usuario_estabelecimento_saude_model.PerfilUsuarioEstabelecimentoSaudeModel
est = estado_model.EstadoModel


def cadastra_medico(medico) -> psm:
    """Function that return a Profissional Saude Model"""
    if not (medico.uf and medico.crm):
        logger.error("Sem nome ou crm ou uf. Impossível cadastrar médico.")
        raise Exception("Sem nome ou crm ou uf. Impossível cadastrar médico.")
    # Busca pelo identifcador do estado

    try:
        # tenta pegar o identificador do estado
        id_uf = est.query.filter_by(sigla=medico.uf).first().identificador
    # Caso não encontre identificador um erro sera jogado
    except AttributeError as excp:
        # Logger error para controle
        logger.error(f'Uf inválida: {medico.uf} - {excp}')
        # Lança erro para quem chamou a função
        raise AttributeError(f'Uf de estadi inválida {excp}')

    ps_alchemy = psm.query.filter(psm.registro_conselho_trabalho == medico.crm,
                                  psm.identificador_estado_conselho_trabalho == id_uf).first()

    usr_alchemy = usr.query.filter(usr.login == medico.login).first()
    logger.info('Buscando profissional de saude.')
    # Verificando se não à o usuário criado com o mesmo login passado nos parâmetros

    logger.info('Buscando usuário.')
    logger.info('Verificando se existe médico cadastrado')
    # Verificando se a assinatura caso não haja pressupõe-se que
    # será médico solicitante

    # Verifica se alguma das instâncias tanto pessoa
    # profissional de saúde é o usuário já estão existentes
    if ps_alchemy or usr_alchemy:
        logger.info('Usuario Já Cadastrado')
        # Caso seja encontrado o pessoa bucar o profissional saude e retorna-lo
        if ps_alchemy:
            # Caso já tenha o profissional saude já retorna o mesmo
            return ps_alchemy
        else:
            # Pega pessoa por usuário
            ps = psm.query.filter(psm.identificador_pessoa == usr_alchemy.identificador_pessoa).first()
            if not ps:
                logger.error(f" Um erro occoreu ao tentar cadastrar {medico.crm} {medico.uf} {medico.nome}")
                raise Exception(f"Usuário sem profissional de saude. {medico.crm} {medico.uf} {medico.nome}")
            return ps
    # Caso não exista inicia-se processo de criação do usuário
    elif not medico.nome:
        logger.info(f'Usuário não encontrado {medico.crm} - {medico.uf}')
        raise ValueError("Impossível cadastrar médico sem nome.")
    else:
        # Cria-se 1º. pessoa model
        p_novo = pm(nome=medico.nome, ativa=True)
        logger.info('Modelo de pessoa nova cadastrado')
        try:
            # Com pessoa model criado adiciona-se ao banco de dados
            db.session.add(p_novo)
            db.session.commit()
            logger.info('Nova pessoa commitada')
        except Exception as expc:
            logger.error('Erro ao cadastrar pessoa: %s', expc)
            db.session.rollback()
            raise Exception(f"Um erro ocorreu {expc}")

        # iniciasse agora o processo de criação do profissional de saude
        ps_novo = psm(
            identificador_pessoa=p_novo.identificador,
            identificador_tipo_conselho_trabalho=1,
            identificador_estado_conselho_trabalho=id_uf,
            registro_conselho_trabalho=medico.crm,
            ativo=True)
        # Com o modelo criado verifica se existe assinatura
        if medico.assinatura:
            # se houver assinatura atribui-se
            ps_novo.assinatura_digitalizada = b64decode(medico.assinatura)
        logger.info('Profissional de saude model criado')
        try:
            # persiste-se há informações no banco de dados
            db.session.add(ps_novo)
            logger.info('Profissinal de saude model inserido no banco.')
            db.session.commit()
        except Exception as expc:
            logger.error('Erro ao adicionar pessoa: %s', expc)
            db.session.rollback()
            db.session.delete(p_novo)
            db.session.commit()
            logger.info('Pessoa nova deletada.')
            raise Exception(f"Um erro ocorreu {expc}")

        # inicie o processo de criação de usuário
        usr_novo = usr(
            login=medico.login,
            senha=hashlib.md5(medico.crm.encode('utf-8')).hexdigest(),
            administrador=False,
            identificador_pessoa=p_novo.identificador,
            ativo=True
        )
        try:
            db.session.add(usr_novo)
            logger.info('Novo usuário inserido')
            db.session.commit()
        except Exception as expc:
            logger.error('Erro ao cadastrar usuário: %s', expc)
            db.session.rollback()
            db.session.delete(ps_novo)
            db.session.commit()
            db.session.delete(p_novo)
            db.session.commit()
            raise Exception(f"Um erro ocorreu {expc}")

        # inicia-se o processo de criação de perfil usuário de saúde
        pues_novo = pues(
            identificador_perfil=medico.perfil,
            identificador_usuario=usr_novo.identificador,
            identificador_estabelecimento_saude=medico.identificador_estabelecimento_saude,
            data_inicial='2020-06-01'
        )
        try:
            # A informação é persistido no banco de dados
            logger.info('Adicionando novo perfil usuário.')
            db.session.add(pues_novo)
            db.session.commit()
        except Exception as expc:
            logger.error('Erro ao adicionar perfil usuario estabelecimento saude: %s', expc)
            db.session.rollback()
            db.session.delete(usr_novo)
            db.session.commit()
            db.session.delete(ps_novo)
            db.session.commit()
            db.session.delete(p_novo)
            db.session.commit()
            raise Exception(f"Um erro ocorreu {expc}")
        # Caso tudo tenha ocorrido certo retornas e profissional de saúde
        return ps_novo
