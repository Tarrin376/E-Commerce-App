from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

limiter = Limiter(
  get_remote_address,
  app=app,
  storage_uri=os.environ['REDIS_STORAGE_URI'],
  storage_options={"socket_connect_timeout": 30},
  strategy="fixed-window"
)