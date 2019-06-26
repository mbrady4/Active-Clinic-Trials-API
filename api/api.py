from decouple import config
from flask import Flask, request, jsonify
from .models import DB, Studies
from sqlalchemy import create_engine

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


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
        obs = Studies.query.all()
        json_list = [i.serialize for i in obs]
        return jsonify(json_list)
    
    @app.route('/api/v1/studies', methods=['GET'])
    def api_filter():
        query_parameters = request.args
        phase = query_parameters.get('phase')

        results = Studies.query.filter(Studies.phase == phase).all()

        json_list = [i.serialize for i in results]

        return jsonify(json_list)



    @app.route('/dummy_data')
    def dummy_data():
        study1 = Studies()
        DB.session.add(study1)
        study1.nct_id = 10303
        study1.start_date = '9/10/2018'
        study1.completion_date = '9/10/2020'
        study1.study_type = 'Clinical'
        study1.overall_status = 'Recruiting'
        study1.brief_title = 'Applying immonocology to stage IV melanoma'
        study1.phase = '2a'
        DB.session.commit()

        study2 = Studies()
        DB.session.add(study2)
        study2.nct_id = 22039
        study2.start_date = '6/4/2019'
        study2.completion_date = '11/12/2024'
        study2.study_type = 'Observational'
        study2.overall_status = 'Active, not yet recruiting'
        study2.brief_title = 'Studying the origins of irritable bowel syndrome'
        study2.phase = '3'
        DB.session.commit()

        return 'Dummy Data Added'

    return app 

