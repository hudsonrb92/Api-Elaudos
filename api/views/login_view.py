from datetime import timedelta

from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from api import api, logger
from ..schemas.usuario_schema import UsuarioSchema
from ..services import usuario_service


class LoginList(Resource):
    def post(self):
        us = UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            login = request.json['login']
            logger.info(f"Fazendo login {login}.")
            senha = request.json['senha']
            usuario_bd = usuario_service.listar_usuario(login)
            if usuario_bd and usuario_bd.ver_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.identificador,
                    expires_delta=timedelta(minutes=30)
                )
                return make_response(jsonify({
                    'access_token': access_token,
                    'Message': 'Login Realizado com sucesso'
                }))
            return make_response(jsonify({
                'message': 'Credenciais inválidas'
            }))


api.add_resource(LoginList, '/api/login')
