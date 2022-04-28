from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

#design
class WeatherCity(Resource):
    def get(self):
        return {"data":"Hello"}#dictinary->json

#call
api.add_resource(WeatherCity,"/weather")    
#run
if __name__ == "__main__":
    app.run(debug=True)