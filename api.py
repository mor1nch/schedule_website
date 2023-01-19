from flask import Blueprint, jsonify
from utils import *

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/api/data/all")
def get_data_json():
    data = get_schedule()
    return jsonify(data)


@api_blueprint.route("/api/data/day/<weekday>")
def get_data1_json(weekday):
    data = get_schedule_by_day(weekday)
    return jsonify(data)


@api_blueprint.route("/api/data/query/<query>")
def get_data2_json(query):
    data = get_schedule_by_word(query)
    return jsonify(data)
