from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handle = logging.FileHandler("integration.log")
file_handle.setFormatter(formatter)
logger.addHandler(file_handle)

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
ma = Marshmallow(app)
JWTManager(app)
api = Api(app)

from .views import (
    estudo_dicom_view,
    login_view,
    laudo_estudo_dicom_view,
    profissional_saude_view,
    anexo_estudo_dicom_view,
    usuario_view,
    integracao_tasy_view,
)
