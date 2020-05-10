from flask import Flask
from flask_restful import Api, Resource, reqparse
import bigdata

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    #def get(self, name):
        
        #return , 404
        
    def post(self):

        bigdata.do_process()
        
        return "Data processed", 201
        
    #def put(self, name):
        
        #return user, 201
        
    #def delete(self, name):
        
        #return , 200
        
api.add_resource(Data, "/processdata/")

app.run(debug=True)