#!/usr/bin/python3
#from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify, Response, render_template
import json
from flask_restful import Resource, Api
from flask_cors import CORS
#from importlib import reload
import importlib
import sys
app = Flask(__name__)
api = Api(app)
CORS(app)

class CBD(Resource):
        def get(self):
            return 'Dev :Vijeth Kashyap'

        def post(self):
            import cmd_handler as cmd_handler
            #cmd_handler = reload(cmd_handler)
            fObj        = cmd_handler.cmd_handler()
            #return Response(fObj.run(request), mimetype='application/JSON')
            return fObj.run(request)


api.add_resource(CBD, '/hql') # Route_1

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,threaded=True, port=8080)
    #app.run(debug=True)