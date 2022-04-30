import json
import logging
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

from logging.config import dictConfig

#for good format
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

#call
#Assignment 4
@app.route("/")
def hello_world():
    app.logger.info('Information')
    
    return jsonify(
        username="Worada",
        email="620@kmit.ac.th",
        id="62011295",
    )

@app.route("/friend",methods=['GET'])
def display_data():
    app.logger.info("Requesting friend name")
    jsonbody = {
        "name" : [],
    }
    with open('friend_data.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for item in data:
            jsonbody["name"].append(item)
        return jsonify(jsonbody)

@app.route("/save/<name>")
def save(name):
    app.logger.info("Saving food data")
    with open('friend_data.txt', 'a') as f:
        f.write('\n'+name)
        f.close()
    jsonbody = {
        "name" : name,
    }
    return jsonify(jsonbody)
    
#Assignment 5
#--------------------------------
@app.after_request
def logging_response_code(response):
    status_tostring = response.status
    logging.warning("Status: %s" % status_tostring)
    return response

#run
if __name__ == "__main__":
    app.run(debug=True)