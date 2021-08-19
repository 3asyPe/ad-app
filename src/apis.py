from flask import request, Response

from app import app
from services import get_xml, create_ad_request, create_impression, get_stats


@app.route("/api/ad/get", methods=["GET"])
def get_ad_api():
    data = request.args

    try:
        user_name = data["user_name"]
        sdk_version = data["sdk_version"]
    except KeyError:
        return {"error": "REQUEST_FIELDS_ERROR"}, 400

    xml = get_xml()
    create_ad_request(user_name=user_name, sdk_version=sdk_version)

    return Response(xml)


@app.route("/api/impression", methods=["GET"])
def impression_api():
    data = request.args

    try:
        user_name = data["user_name"]
        sdk_version = data["sdk_version"]
    except KeyError:
        return {"error": "REQUEST_FIELDS_ERROR"}, 400

    create_impression(user_name=user_name, sdk_version=sdk_version)

    return Response(), 200


@app.route("/api/stats/get", methods=["GET"])
def get_stats_api():
    data = request.args

    try:
        filter_type = data["filter_type"]
    except KeyError:
        return {"error": "REQUEST_FIELDS_ERROR"}, 400

    try:
        stats = get_stats(filter_type=filter_type)
    except ValueError:
        return {"error": "FILTER_TYPE_ERROR"}, 400

    return stats, 200
    