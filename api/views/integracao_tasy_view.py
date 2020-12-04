from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api, logger
from ..schemas.integracao_tasy_schema import IntegracaoTasySchema
from ..services.integracao_tasy_services import (
    inserir_exame,
    busca_por_prescricao,
    listar_exames_iniciados,
    busca_exames_worklist_false,
    altera_criado_worklist_true,
    altera_integrado_tasy,
    exame_iniciado_to_true)
from ..services.estudo_dicom_service import invalida_exames
from ..entidades.integracao_tasy import IntegracaoTasy


class IntegracaoTasyDetail(Resource):
    @jwt_required
    def get(self, accession):
        logger.info(f"Rota de consulta acessada, buscando exame {accession}")
        its = IntegracaoTasySchema()
        itser = busca_por_prescricao(accession)
        response = make_response(its.jsonify(itser), 200)
        return response

    @jwt_required
    def put(self, accession):
        logger.info(f"Alterado integrado_tasy para true")
        its = IntegracaoTasySchema()
        altr = altera_integrado_tasy(accession)
        if altr:
            return make_response(its.jsonify(altr), 202)
        else:
            return make_response(jsonify({'Error': 'Exame já integrado.'}))


class InsereExameIntegracao(Resource):
    @jwt_required
    def post(self):
        its = IntegracaoTasySchema()
        validate = its.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        ite = IntegracaoTasy(**request.json)
        result = inserir_exame(ite)
        if result:
            return make_response(its.jsonify(result))
        else:
            return make_response(jsonify({"Error": "Exame já cadastrado"}), 208)

    @jwt_required
    def delete(self):
        logger.info(f'Alterando exame para cancelado')
        accession = request.json
        its = IntegracaoTasySchema()
        exame = invalida_exames(accession['accessions'])
        if exame:
            return make_response(its.jsonify(exame, many=True), 200)
        else:
            return make_response(jsonify({'Error': 'Exame não encontrado, já iniciado ou já cancelado'}), 400)


class IntegracaoTasyListIniciados(Resource):
    @jwt_required
    def get(self):
        its = IntegracaoTasySchema()
        logger.info("Buscando exames iniciados")
        estudos = listar_exames_iniciados()
        logger.info(estudos)
        if estudos:
            return make_response(its.jsonify(estudos, many=True), 200)
        else:
            return make_response(jsonify({'Message': 'Nenhum exame encontrado'}))

    @jwt_required
    def put(self):
        its = IntegracaoTasySchema()
        logger.info(f'Rota PuT Exames iniciaos')
        logger.info(request.__dir__())
        nr_sequencia = request.json['nr_sequencia']
        nr_prescricao = request.json['nr_prescricao']
        exame = exame_iniciado_to_true(nr_prescicao=nr_prescricao, nr_sequencia=nr_sequencia)
        if exame:
            return make_response(its.jsonify(exame), 202)
        else:
            return make_response(jsonify({'Error': 'Exame não encontrado'}), 400)


class IntegracaoWorklistNotCreated(Resource):
    @jwt_required
    def get(self):
        its = IntegracaoTasySchema()
        logger.info("Buscando exames que ainda não foram criados no worklist")
        exames = busca_exames_worklist_false()
        return make_response(its.jsonify(exames, many=True), 200)

    @jwt_required
    def put(self):
        its = IntegracaoTasySchema()
        nr_prescricao = request.json['nr_prescricao']
        nr_sequencia = request.json['nr_sequencia']
        exames = altera_criado_worklist_true(nr_sequencia=nr_sequencia, nr_prescricao=nr_prescricao)
        return make_response(its.jsonify(exames), 200)


api.add_resource(IntegracaoTasyDetail, '/api/integracao/<string:accession>')
api.add_resource(InsereExameIntegracao, '/api/exame-integracao/')
api.add_resource(IntegracaoTasyListIniciados, '/api/integracao/iniciados/')
api.add_resource(IntegracaoWorklistNotCreated, '/api/worklist')
