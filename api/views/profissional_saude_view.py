from flask import make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas import profissional_saude_schema
from ..services import profissional_saude_service


class ProfissionalSaudeDetail(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info(f"Rota ProfissionalSaudeDetail buscando identificador: {identificador}")
        pesv = profissional_saude_service.listar_profissional_por_id(
            identificador)
        if pesv is None:
            logger.info("Não encontrado.")
            return make_response(jsonify({"Message": "Estudo Não Encontrado"}), 404)
        pes = profissional_saude_schema.ProfissionalSaudeModelSchema()
        logger.info("Encontrado criando retorno.")
        return make_response(pes.jsonify(pesv), 200)


api.add_resource(ProfissionalSaudeDetail, '/api/profissional/<int:identificador>')
