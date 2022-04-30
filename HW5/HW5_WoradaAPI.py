from flask import Flask
from flask import jsonify
import logging

app = Flask(__name__)

#route and design
@app.route("/loging")
def hello_world():
    app.logger.info('first test message')
    
    return jsonify(
        username="Cream",
        email="Wcream@gmail.com",
        id="62011295",
    )

#run
if __name__ == "__main__":
    app.run(debug=True)


#from logging.config import dictConfig
"""dictConfig({
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
})"""