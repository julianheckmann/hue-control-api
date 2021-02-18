import flask
from flatten_dict import flatten
import json_resources.sample_responses as sample_responses
import os
from flask_cors import CORS

port = 8080

folder = "api/logs"

path = "./{}".format(folder)

if not os.path.exists(path):
    os.makedirs(path)

USERNAME = "root"
ID = "1"

app = flask.Flask(__name__)

CORS(app)

## LIGHTS

# INDEX
@app.route("/{}/lights".format(USERNAME), methods=["GET"])
def lights_all():
    lights = sample_responses.all_lights
    return flask.jsonify(lights)

# SHOW
@app.route("/{}/lights/{}".format(USERNAME, ID), methods=["GET"])
def light():
    light = sample_responses.test_light
    return flask.jsonify(light)

# UPDATE
@app.route("/{}/lights/{}/state".format(USERNAME, ID), methods=["PUT"])
def set_state():
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res

# CREATE
@app.route("/{}/lights".format(USERNAME), methods=["POST"])
def search():
    return flask.make_response(flask.jsonify({ "success": { "/lights": "Searching for new devices" }}))

# DELETE
@app.route("/{}/lights/{}".format(USERNAME, ID), methods=["DELETE"])
def delete_light():
    return flask.make_response(flask.jsonify({}))

## ROOMS

# INDEX
@app.route("/{}/groups".format(USERNAME), methods=["GET"])
def groups_all():
    groups = sample_responses.all_groups
    return flask.jsonify(groups)

# SHOW
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["GET"])
def group():
    group = sample_responses.test_group
    return flask.jsonify(group)

# UPDATE
@app.route("/{}/groups/{}/action".format(USERNAME, ID), methods=["PUT"])
def set_action():
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res

# CREATE
# CREATE GROUP
@app.route("/{}/groups".format(USERNAME), methods=["POST"])
def create_group():
    state_keys = sample_responses.group_keys
    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res
# ADD TO GROUP
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["PUT"])
def update_group():
    state_keys = sample_responses.group_keys
    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res

# DELETE
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["DELETE"])
def delete():
    return flask.make_response(flask.jsonify({}))


# INDEX ROUTE
@app.route("/", methods=["GET"])
def index():
    return flask.make_response("/", 200)

## FUNCTION

def check_keys(request, all):
    for key in request:
        if key not in all:
            return False

    return True

def get_timestamp() -> str:
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%d-%m-%Y_%H:%M:%S")

if __name__ == "__main__":
    import logging

    logging.basicConfig(filename="{}/log_{}.txt".format(folder, get_timestamp()), level=logging.DEBUG)

    app.run(host = "0.0.0.0", port = port, debug = True)
