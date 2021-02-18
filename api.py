import flask
import json_resources.sample_responses as sample_responses
from json_handler import config_handler
from flask_cors import CORS

USERNAME = "root"

port = 8080

folder = "api/logs"

path = "./{}".format(folder)

app = flask.Flask(__name__)

CORS(app)

jh = config_handler()

@app.route("/", methods=["HEAD"])
def ping():
    return flask.make_response("", 200)

## LIGHTS

# INDEX TODO: DONE
@app.route("/{}/lights".format(USERNAME), methods=["GET"])
def lights_all():
    lights = jh.get_lights_all()
    return flask.jsonify(lights)

# SHOW TODO: DONE
@app.route("/{}/lights/<id>".format(USERNAME), methods=["GET"])
def light(id):
    light = jh.get_light_by_id(id)
    return flask.jsonify(light)

# UPDATE TODO: DONE
@app.route("/{}/lights/<id>/state".format(USERNAME), methods=["PUT"])
def set_state(id):
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        jh.set_state_light(id, data)
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res

# CREATE TODO: DONE
@app.route("/{}/lights".format(USERNAME), methods=["POST"])
def search():
    return flask.make_response(flask.jsonify({ "success": { "/lights": "Searching for new devices" }}))

# DELETE TODO: maybe implement that the delete also deletes it out of the group
@app.route("/{}/lights/<id>".format(USERNAME), methods=["DELETE"])
def delete_light(id):
    jh.remove_light(id)
    return flask.make_response(flask.jsonify({}))

## ROOMS

# INDEX TODO: DONE
@app.route("/{}/groups".format(USERNAME), methods=["GET"])
def groups_all():
    groups = jh.get_groups_all()
    return flask.jsonify(group)

# SHOW TODO: DONE
@app.route("/{}/groups/<id>".format(USERNAME), methods=["GET"])
def group(id):
    group = jh.get_group_by_id(id)
    return flask.jsonify(group)

# UPDATE TODO: DONE
@app.route("/{}/groups/<id>/action".format(USERNAME), methods=["PUT"])
def set_action():
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()
    
    if check_keys(request_keys, state_keys):
        jh.set_state_group(id, data)
        res = flask.make_response(flask.jsonify({"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify({"message": "Keys not Matching"}), 400)

    return res

# CREATE
# CREATE GROUP TODO: implement changing dict logic
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
# ADD TO GROUP TODO: implement changing dict logic AND check if its ok
@app.route("/{}/groups/<id>".format(USERNAME), methods=["PUT"])
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
@app.route("/{}/groups/<id>".format(USERNAME), methods=["DELETE"])
def delete(id):
    jh.remove_group(id)
    return flask.make_response(flask.jsonify({}))

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