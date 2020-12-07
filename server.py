#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import subprocess


app = Flask(__name__)
api = Api(app)

class Hosts(Resource):
   def post(self):
      ReceivedData = request.get_json()
      id = ReceivedData["id"]
      hostname = ReceivedData["hostname"]
      status = ReceivedData["status"]
      int(id)

      #hostName = hostData["hostname"]
      parsedAnswer = str(id) + hostname + status
      AnswerData = {
           "id" : id,
           "hostname": hostname,
           "status": status,
           "StatusCode" : 200
      }
      statusfile = open("status.db","a")
      statusfile.write(str(AnswerData) + "\n")
      statusfile.close()
      return jsonify(AnswerData)

class Sensors(Resource):
    def post(self):

        sensorData = request.get_json()
        sensorID = sensorData["id"]
        sensorName = sensorData["name"]
        sensorStatus = sensorData["status"]
        sensorMessage = sensorData["message"]
        returnData = {
             "ID" : sensorID,
             "Sensore Name" : sensorName,
             "Sensor Status" : sensorStatus,
             "Sensor Message" : sensorMessage,
        }
        sensorsFile = open("sensorData.db","a")
        sensorsFile.write(str(returnData))
        sensorsFile.close()
        return jsonify(returnData)


api.add_resource(Hosts, "/hosts")
api.add_resource(Sensors, "/sensors")



@app.route('/')
def hello_world():
   return("RestAPI Automation Tool")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
