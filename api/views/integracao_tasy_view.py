from flask import make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas.integracao_tasy_schema import IntegracaoTasySchema
from ..services.integracao_tasy_services import busca_por_prescricao


class IntegracaoTasyDetail(Resource):
    @jwt_required
    def get(self, nr_sequencia, nr_prescricao):
        logger.info(f"Rota de consulta acessada"
                    f"Buscando exame {nr_prescricao}{nr_sequencia}")
        its = IntegracaoTasySchema()
        itser = busca_por_prescricao(nr_prescricao=nr_prescricao,
                                     nr_sequencia=nr_sequencia)
        return make_response(its.jsonify(itser), 200)


api.add_resource(IntegracaoTasyDetail, '/api/integracao/<int:nr_prescricao>/<int:nr_sequencia>')
