import boto3
import json
from decouple import config
from flask import Flask, request, jsonify
from flask_cors import CORS
from .models import DB, Studies
from sqlalchemy import *


def add_data(query_parameters):
    num = query_parameters.get('arg')
    file_name = str(num) + '_data.json'

    s3 = boto3.resource('s3',
                        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))
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
        instance.minimum_age_val = trial['minimum_age_val']
        instance.maximum_age_val = trial['maximum_age_val']
        DB.session.commit()

    return f'Data from {file_name} Imported Successfully'


def init_db():
    DB.drop_all()
    DB.create_all()

    s3 = boto3.resource('s3', 
                        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))
    content_object = s3.Object('clf-api', '82_data.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    
    #81655
    for i in range(81000, 81656, 1):
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
        instance.minimum_age_val = trial['minimum_age_val']
        instance.maximum_age_val = trial['maximum_age_val']
        DB.session.commit()

    return f'Database initialized and seeded successfully'