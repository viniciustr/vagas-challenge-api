from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User
from .pessoa import Pessoa
from .vaga import Vaga
from .candidatura import Candidatura
