from flask import Flask
from flask_restful import Api, Resource, reqparse
import bigdata
import py_eureka_client.eureka_client as eureka_client

eureka_client.init_registry_client("http://localhost:8761/eureka/",
app_name="DataProcessor",
instance_port=8761)

app = Flask(__name__)
api = Api(app)

class Data(Resource):
        
    def post(self):

        bigdata.do_process()
        
        return "Data processed", 201
        
    def delete(self):
        
        bigdata.do_remove()
        
        return "Data Cleared", 200
        
api.add_resource(Data, "/processdata/")

app.run(debug=True)