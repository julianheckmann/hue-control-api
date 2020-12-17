import flask
import json_resources.sample_responses as sample_responses

"""
Small dummy REST API for testing during devolpment of a web app for a diyHue 
bridge. This API is only for testing purposes since our hardware is limited 
and testing like this is easier in our current situation (COVID-19).

The following calls are available for lights aswell as groups:

    index:      get all available lights/groups
    show:       show light/room with id x
    update:     update state/action of light/room with id x
    create:     
        light:  enable search for new lights 
        groups: create new group with the following ids    
    delete: delete light/group

The API only checks if the keywords of the calls are correct. IDs and usernames
are static for testing. 

"""

USERNAME = "root"  # Username of the Hue Bridge account/user
ID = "1"  # ID for lights and groups

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# LIGHTS

# INDEX
@app.route("/{}/lights".format(USERNAME), methods=["GET"])
def lights_all():
    """
    Sample output of all lights available
    """
    lights = sample_responses.all_lights
    return flask.jsonify(lights)

# SHOW
@app.route("/{}/lights/{}".format(USERNAME, ID), methods=["GET"])
def light():
    """
    Sample output for light with ID
    """
    light = sample_responses.test_light
    return flask.jsonify(light)

# UPDATE
@app.route("/{}/lights/{}/state".format(USERNAME, ID), methods=["PUT"])
def set_state():
    """
    Sample output for changing state of a light with ID. Function checks if the 
    keywords are matching with the ones documented in the Hue API. If the check 
    fails a ERROR 400 is being returned.
    """
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()

    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify(
            {"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify(
            {"message": "Keys not Matching"}), 400)

    return res

# CREATE
@app.route("/{}/lights".format(USERNAME), methods=["POST"])
def search():
    """
    Dummy response searching (creating) new lights
    """
    return flask.make_response(flask.jsonify({"success": {"/lights": "Searching for new devices"}}))

# DELETE
@app.route("/{}/lights/{}".format(USERNAME, ID), methods=["DELETE"])
def delete_light():
    """
    Dummy response for deleting light with ID
    """
    return flask.make_response(flask.jsonify({}))

# ROOMS

# INDEX
@app.route("/{}/groups".format(USERNAME), methods=["GET"])
def groups_all():
    """
    Sample output of all groups available
    """
    groups = sample_responses.all_groups
    return flask.jsonify(groups)

# SHOW
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["GET"])
def group():
    """
    Sample output of group with ID
    """
    group = sample_responses.test_group
    return flask.jsonify(group)

# UPDATE
@app.route("/{}/groups/{}/action".format(USERNAME, ID), methods=["PUT"])
def set_action():
    """
    Sample output for changing action of a group with ID. Function checks if 
    the keywords are matching with the ones documented in the Hue API. If the
    check fails a ERROR 400 is being returned.
    """
    state_keys = sample_responses.actions

    data = flask.request.get_json()
    request_keys = data.keys()

    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify(
            {"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify(
            {"message": "Keys not Matching"}), 400)

    return res

# CREATE
# CREATE GROUP
@app.route("/{}/groups".format(USERNAME), methods=["POST"])
def create_group():
    """
    Dummy response for creating a group. Function checks if the keywords are
    matching with the ones documented in the Hue API. If the check fails a 
    ERROR 400 is being returned.
    """
    state_keys = sample_responses.group_keys
    data = flask.request.get_json()
    request_keys = data.keys()

    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify(
            {"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify(
            {"message": "Keys not Matching"}), 400)

    return res
# ADD TO GROUP
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["PUT"])
def update_group():
    """
    Dummy response for adding a light to a group. Function checks if the 
    keywords are matching with the ones documented in the Hue API. If the
    check fails a ERROR 400 is being returned.
    """
    state_keys = sample_responses.group_keys
    data = flask.request.get_json()
    request_keys = data.keys()

    if check_keys(request_keys, state_keys):
        res = flask.make_response(flask.jsonify(
            {"message": "Value Changed"}), 201)
    else:
        res = flask.make_response(flask.jsonify(
            {"message": "Keys not Matching"}), 400)

    return res

# DELETE
@app.route("/{}/groups/{}".format(USERNAME, ID), methods=["DELETE"])
def delete():
    """
    Dummy response for deleting group with ID
    """
    return flask.make_response(flask.jsonify({}))

# FUNCTION
def check_keys(request, all):
    """
    Checks if the keywords that are in the request list are all valid
    ones that are found in the all list.
    """
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
    logging.basicConfig(
        filename="logs/log_{}.txt".format(get_timestamp()), level=logging.DEBUG)

    app.run()
