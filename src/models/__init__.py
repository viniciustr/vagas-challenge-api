from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .pessoa import Pessoa
from .vaga import Vaga
from .candidatura import Candidatura
from .ranking_item import RankingItem
