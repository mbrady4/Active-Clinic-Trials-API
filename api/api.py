import boto3
import json
from decouple import config
from flask import Flask, request, jsonify
from .models import DB, Studies
from sqlalchemy import create_engine


def create_api():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def home():
        return "<h1>Welcome to the Clinical Trial Finder API</h1>"
    

    @app.route('/api/v1/studies/all', methods=['GET'])
    def api_all():
        obs = Studies.query.limit(200).all()
        json_list = [i.serialize for i in obs]
        return jsonify(json_list)
    
    @app.route('/api/v1/studies', methods=['GET'])
    def api_filter():
        query_parameters = request.args
        phase = query_parameters.get('phase')

        results = Studies.query.filter(Studies.phase == phase).all()

        json_list = [i.serialize for i in results]

        return jsonify(json_list)

    @app.route('/import_data')
    def import_data():
        DB.drop_all()
        DB.create_all()

        query_parameters = request.args
        num = query_parameters.get('arg')
        file_name = str(num) + '_data.json'

        s3 = boto3.resource('s3')
        content_object = s3.Object('clf-api', file_name)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        num = int(num) * 1000 -1000
        for i in range(int(num),int(num)+1000,1):
            trial = json_content[str(i)]
            instance = Studies()
            DB.session.add(instance)
            instance.nct_id = trial['nct_id']
            instance.start_date = trial['start_date']
            instance.completion_date = trial['completion_date']
            instance.study_type = trial['study_type']
            instance.overall_status = trial['overall_status']
            instance.brief_title = trial['brief_title']
            instance.phase = trial['phase']
            instance.condition_name = trial['condition_name']
            instance.description = trial['description']
            instance.gender = trial['gender']
            instance.minimum_age = trial['minimum_age']
            instance.maximum_age = trial['maximum_age']
            instance.healthy_volunteers = trial['healthy_volunteers']
            instance.sponsor_name = trial['sponsor_name']
            instance.name = trial['name']
            instance.phone = trial['phone']
            instance.email = trial['email']
            instance.completion_prob = trial['completion_prob']
            DB.session.commit()

        return f'Data from {file_name} Imported Successfully'
        
    @app.route('/init_data')
    def init_data():
        DB.drop_all()
        DB.create_all()

        s3 = boto3.resource('s3')
        content_object = s3.Object('clf-api', '82_data.json')
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        
        #81655
        for i in range(81000,81656,1):
            trial = json_content[str(i)]
            instance = Studies()
            DB.session.add(instance)
            instance.nct_id = trial['nct_id']
            instance.start_date = trial['start_date']
            instance.completion_date = trial['completion_date']
            instance.study_type = trial['study_type']
            instance.overall_status = trial['overall_status']
            instance.brief_title = trial['brief_title']
            instance.phase = trial['phase']
            instance.condition_name = trial['condition_name']
            instance.description = trial['description']
            instance.gender = trial['gender']
            instance.minimum_age = trial['minimum_age']
            instance.maximum_age = trial['maximum_age']
            instance.healthy_volunteers = trial['healthy_volunteers']
            instance.sponsor_name = trial['sponsor_name']
            instance.name = trial['name']
            instance.phone = trial['phone']
            instance.email = trial['email']
            instance.completion_prob = trial['completion_prob']
            DB.session.commit()

        return f'Database initialized and seeded successfully'

    return app 

