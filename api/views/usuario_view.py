from flask import make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas import usuario_schema
from ..services import usuario_service


class UsuarioDetail(Resource):
    @jwt_required
    def get(self, identificador_pessoa):
        logger.info(f"Rota UsuarioDetail acessada, buscando por id_pessoa: {identificador_pessoa}.")
        usuario = usuario_service.lista_usuario_por_id(identificador_pessoa)
        if usuario is None:
            logger.info("Nenhum usuario encontrado.")
            return make_response(jsonify({"Message": "Estudo Não Encontrado"}), 404)
        us = usuario_schema.UsuarioSchema()
        logger.info("Retornando usuário encontrado.")
        return make_response(us.jsonify(usuario), 200)


api.add_resource(UsuarioDetail, '/api/usuario/<int:identificador_pessoa>')
