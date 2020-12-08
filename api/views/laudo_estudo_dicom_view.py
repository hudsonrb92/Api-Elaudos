from flask import make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas import laudo_estudo_dicom_schema
from ..services import laudo_estudo_dicom_service


class LaudoEstudoDicomListNoPaginate(Resource):
    @jwt_required
    def get(self, identificador_estabelecimento_saude):
        logger.info(f"Rota LaudoEstudoDicomListNoPaginate acessada, buscando {identificador_estabelecimento_saude}.")
        lsq = laudo_estudo_dicom_schema.LaudoEstudoDicomSchema(many=True)
        les = laudo_estudo_dicom_service.listar_laudos(identificador_estabelecimento_saude)
        return make_response(lsq.jsonify(les), 200)


class LaudoEstudoDicomDetail(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info(f"Acessada rota LaudoEstudoDicomDetail, buscando: {identificador}")
        laudo = laudo_estudo_dicom_service.listar_estudo_por_id(identificador)
        if laudo:
            logger.info("Laudo encontrado.")
            es = laudo_estudo_dicom_schema.LaudoEstudoDicomSchema()
            return make_response(es.jsonify(laudo), 200)
        else:
            logger.info("Laudo não encontrado.")
            return make_response(jsonify({"Message": "Estudo Não Encontrado"}), 404)

    @jwt_required
    def put(self, identificador):
        logger.info("Mudando status para integrado.")
        laudo = laudo_estudo_dicom_service.listar_estudo_por_id(identificador)
        if laudo is None:
            logger.info("Identificador não encontrado.")
            return make_response(jsonify("Laudo Não Encontrado"), 404)
        else:
            logger.info("Mudando laudo para integrado.")
            ls = laudo_estudo_dicom_schema.LaudoEstudoDicomSchema()
            laudo_estudo_dicom_service.update_to_integrado(laudo)
            laudo_atualizado = laudo_estudo_dicom_service.listar_estudo_por_id(identificador)
            return make_response(ls.jsonify(laudo_atualizado), 200)


class LaudoEstudoDicomIDEstudo(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info(f"Buscando laudo do estudo {identificador}")
        laudo = laudo_estudo_dicom_service.get_laudo_id_estudo(identificador)
        if laudo is None:
            logger.info("Identificador não encontrado.")
            return make_response(jsonify("Laudo Não Encontrado"), 404)
        else:
            logger.info(f"Exame encontrado {laudo.identificador}")
            ls = laudo_estudo_dicom_schema.LaudoEstudoDicomSchema()
            return make_response(ls.jsonify(laudo), 200)

    @jwt_required
    def put(self, identificador):
        logger.info(f"Alterando exame para integrado true pelo id do estudo {identificador}")
        exame = laudo_estudo_dicom_service.update_integrado_id_estudo(identificador)
        if exame is None:
            logger.info(f"Nenhum exame encontrado no identificador {identificador}")
            return make_response(jsonify({"Message": "Nenhum exame encontrado"}), 404)
        else:
            ls = laudo_estudo_dicom_schema.LaudoEstudoDicomSchema
            return make_response(ls.jsonify(exame), 202)


class LaudoEstudoDicomPdf(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info(f"Rota de retorno de exame em pdf acessada {identificador}")
        try:
            laudo = laudo_estudo_dicom_service.get_pdf(identificador)
            laudo = laudo.decode("utf8")
            return make_response({"pdf": laudo})
        except Exception as e:
            logger.info(f"Excessão {e}")
            return make_response({"Message": "Laudo Não Encontrado."})


api.add_resource(LaudoEstudoDicomDetail, "/api/laudo/<int:identificador>")
api.add_resource(LaudoEstudoDicomListNoPaginate, "/api/laudos/<int:identificador_estabelecimento_saude>")
api.add_resource(LaudoEstudoDicomPdf, "/api/laudopdf/<int:identificador>")
api.add_resource(LaudoEstudoDicomIDEstudo, "/api/laudo_estudo/<int:identificador>")
