from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CONFIGURAÇÃO DO BANCO
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# PADRÃO CORRETO
db = SQLAlchemy(app)

# IMPORTS POR ÚLTIMO (MUITO IMPORTANTE)
from fakepinterest import routes, models