from flask import make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas import anexo_estudo_dicom_schema
from ..services import anexo_estudo_dicom_service


class AnexoEstudoDicomList(Resource):
    @jwt_required
    def get(self, identificador_estudo_dicom):
        logger.info(
            "Rota get AnexoEstudoDicomList por identificador_estudo acessada.")
        anexos = anexo_estudo_dicom_service.listar_anexo_por_identificador_estudo(
            identificador_estudo_dicom)
        logger.info(f"Tem {len(anexos)} anexo(s).")
        logger.info(
            f"Identificador_estudo_dicom buscado: {identificador_estudo_dicom}")
        if anexos is None:
            logger.info('Nenhum anexo encontrado.')
            return make_response(jsonify({"message": "Não Encontrado"}), 404)
        else:
            logger.info('Retornando anexo(s).')
            ans = anexo_estudo_dicom_schema.AnexoEstudoDicomSchema(many=True)
            return make_response(ans.jsonify(anexos), 200)


class AnexoEstudoDicomDetail(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info("Rota AnexoEstudoDicomDetail acessada.")
        anexo = anexo_estudo_dicom_service.listar_anexo_por_identificador(
            identificador)
        logger.info(f"Identificador buscado: {identificador}")
        if anexo is None:
            logger.info("Nenhum anexo encontrado.")
            return make_response(jsonify("Nao Encontrado"), 404)
        else:
            logger.info("Anexos encontrados.")
            anss = anexo_estudo_dicom_schema.AnexoEstudoDicomSchema()
            return make_response(anss.jsonify(anexo), 200)


api.add_resource(AnexoEstudoDicomList,
                 '/api/anexos/<int:identificador_estudo_dicom>')
api.add_resource(AnexoEstudoDicomDetail, '/api/anexo/<int:identificador>')
