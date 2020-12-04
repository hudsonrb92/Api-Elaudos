from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas import estudo_dicom_schema
from ..services import estudo_dicom_service


class EstudoDicomDetail(Resource):
    @jwt_required
    def get(self, identificador):
        logger.info("Rota estudoDicomDetail acessada.")
        estudo = estudo_dicom_service.listar_estudo_por_id(identificador)
        logger.info(f"Identificador buscado {identificador}")
        if estudo:
            logger.info("Estudo encontrado.")
            es = estudo_dicom_schema.EstudoDicomSchema()
            return make_response(es.jsonify(estudo), 200)
        else:
            logger.info("Nenhum estudo foi encontrado.")
            return make_response(jsonify({"Message": "Estudo Não Encontrado"}), 404)


class EstudoDicomDetailStudy(Resource):
    @jwt_required
    def get(self, studyinstanceuid):
        logger.info("Rota EstudoDicomDetailStudy acessada.")
        estudo = estudo_dicom_service.listar_estudo_por_studyinstanceuid(
            studyinstanceuid)
        logger.info(f"Study buscado: {studyinstanceuid}")
        if estudo:
            logger.info("Estudo encontrado.")
            es = estudo_dicom_schema.EstudoDicomSchema()
            return make_response(es.jsonify(estudo), 200)
        else:
            logger.info("Nenhum estudo encontrado.")
            return make_response(jsonify({"Message": "Estudo Não Encontrado"}), 404)

    def post(self, studyinstanceuid):
        logger.info(
            "Rota para settar que exame foi marcado como teste no cliente.")
        estudo = estudo_dicom_service.listar_estudo_por_studyinstanceuid(
            studyinstanceuid)
        logger.info(f"Study buscado: {studyinstanceuid}")
        if not estudo:
            logger.info("Estudo não encontrado.")
        else:
            logger.info("Exame encontrado, marcado alterando status.")
            estudo.status = 1


class EstudoDicomNoReport(Resource):
    @jwt_required
    def get(self, identificador_estabelecimento_saude):
        logger.info(
            f"Rota EstudoDicomNoReport acessada, buscando identificador_es: {identificador_estabelecimento_saude}")
        estudos = estudo_dicom_service.listar_estudos_sem_laudos(
            identificador_estabelecimento_saude)
        logger.info(f"{len(estudos)} estudos encontrados.")
        if estudos:
            es = estudo_dicom_schema.EstudoDicomSchema(many=True)
            return make_response(es.jsonify(estudos))
        else:
            return make_response(jsonify({"message": "Nenhum Exame Sem Laudo"}), 200)


api.add_resource(EstudoDicomDetail, '/api/estudo/<int:identificador>')
api.add_resource(EstudoDicomDetailStudy,
                 '/api/study/<string:studyinstanceuid>')
api.add_resource(EstudoDicomNoReport,
                 '/api/estudoSemLaudo/<int:identificador_estabelecimento_saude>')
