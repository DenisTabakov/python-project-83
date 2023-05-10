from flask import Flask
from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask!'
