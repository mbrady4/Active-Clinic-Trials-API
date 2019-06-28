import boto3
import json
from decouple import config
from .data import add_data, init_db
from flask import Flask, request, jsonify
from flask_cors import CORS
from .filters import query_filters, get_all, search
from .models import DB, Studies
from sqlalchemy import *


def create_api():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    DB.init_app(app)

    @app.route('/')
    def home():
        return "<h1>Welcome to the Clinical Trial Finder API</h1>"    

    @app.route('/api/v1/studies/all', methods=['GET'])
    def api_all():
        json_list = get_all()
        return json_list
    
    @app.route('/api/v1/studies/query', methods=['GET'])
    def api_filter():
        query_parameters = request.args
        json_list = query_filters(query_parameters)
        return json_list

    @app.route('/api/v1/studies/search', methods=['GET'])
    def api_search():
        term = request.args.get('description')
        json_list = search(term)
        return json_list

    @app.route('/import_data')
    def import_data():
        query_parameters = request.args
        status = add_data(query_parameters)
        return status
        
    @app.route('/init_data')
    def init_data():
        status = init_db()
        return status
        
    return app 

