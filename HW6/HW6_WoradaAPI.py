from flask import Flask
from flask import jsonify
#from logging.config import dictConfig
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
