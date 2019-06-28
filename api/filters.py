import requests
import json
from flask import Flask, jsonify, request
from .models import DB, Studies
from flask_cors import CORS
from sqlalchemy import *


def get_all():
    obs = Studies.query.limit(200).all()
    json_list = [i.serialize for i in obs]
    return jsonify(json_list)


def search(term):
    term = term.lower()
    query = "SELECT * FROM studies WHERE lower(description) LIKE \'%" + term + "%\' LIMIT 200;"
    results = Studies.query.from_statement(text(query)).all()
    json_list = [i.serialize for i in results]

    return jsonify(json_list)


def query_filters(query_parameters):
    phase = query_parameters.get('phase').lower()
    gender = query_parameters.get('gender').lower()
    study_type = query_parameters.get('studytype').lower()
    limit = query_parameters.get('limit')
    status = query_parameters.get('status').lower()
    healthy = query_parameters.get('healthy').lower()
    threshold = float(query_parameters.get('predproba'))
    max_age = query_parameters.get('maxage')
    min_age = query_parameters.get('minage')

    # Base Query
    query = "SELECT * FROM studies WHERE"

    if phase:
        query += f" lower(phase)='{phase}' AND"
    if study_type:
        query += f" lower(study_type)='{study_type}' AND"
    if gender:
        query += f" lower(gender)=\'{gender}\' AND"
    if threshold:
        query += f" float(completion_prob)>{threshold} AND"
    if status:
        query += f" lower(overall_status)=\'{status}\' AND"
    if healthy:
        query += f" lower(healthy_volunteers)=\'{healthy}\' AND"
    if max_age:
        query += f" maximum_age_val<='{max_age} AND"
    if min_age:
        query += f" minimum_age_val<='{min_age} AND"
    if not (phase or study_type or gender):
        return 'No Results' #api_all()
    if not limit:
        limit = 200

    query = query[:-4] + f" LIMIT {limit};"

    results = Studies.query.from_statement(text(query)).all()

    json_list = [i.serialize for i in results]

    return jsonify(json_list)