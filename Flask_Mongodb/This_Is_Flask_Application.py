from flask_pymongo import PyMongo
from flask import Flask, request, json, jsonify, render_template
from bson import json_util

#Let's start with creating an instance of the Flask class for our web app:----------------------------------------------
app = Flask(__name__)

#Now, we are connecting to our MongoDB database:------------------------------------------------------------------------
app.config["MONGO_URI"] = "mongodb://svetlana:cisco123@localhost:27017/Device_Configuration"

#We will use explicit BSON conversion to and from JSON:-----------------------------------------------------------------
json.dumps = json_util.dumps

#It's time to tell PyMongo to work with our Flask App:------------------------------------------------------------------
mongo = PyMongo(app)

#It's now time to create our apps for our APIs:-------------------------------------------------------------------------

#1)GET /<switch name>/interfaces.html-----------------------------------------------------------------------------------
#Return information about ALL interfaces of the switches in the database in HTML format
@app.route('/<SW>/interfaces.html', methods=['GET'])
def FindThisSwitch(SW):
    return render_template('FindThisSwitch.html', result = mongo.db.Interfaces.find({"Switch_name": SW}))

#2)GET /<switch name>/interfaces.json-----------------------------------------------------------------------------------
#Return information about ALL interfaces of the switch in the database in JSON format
@app.route('/<SW>/interfaces.json', methods=['GET'])
def FindThisSwitchJSON(SW):
    return jsonify(mongo.db.Interfaces.find({"Switch_name": SW}))

#3)GET /<switch name>/<interface_name>/details.html---------------------------------------------------------------------
#Return information only about specified interface in HTML format
@app.route('/<SW>/<INF>/details.html', methods=['GET'])
def FindThisSwitchInterface(SW, INF):
    return render_template('FindThisSwitchInterface.html', result = mongo.db.Interfaces.find({"Switch_name": SW, "Interface_Name": INF.replace('-', '/')}))

#4)GET /<switch name>/<interface_name>/details.json---------------------------------------------------------------------
#Return information only about specified interface in JSON format
@app.route('/<SW>/<INF>/details.json', methods=['GET'])
def FindThisSwitchInterfaceJSON(SW, INF):
    return jsonify(mongo.db.Interfaces.find({"Switch_name": SW, "Interface_Name": INF.replace('-', '/')}))

#5)PATCH /<switch name>/<interface id>----------------------------------------------------------------------------------
#With a JSON Payload  of ‘{“description”:”my cool interface”} – to change the description of the interface
#----------------AND-------------------
#6)PATCH /<switch name>/<interface id>----------------------------------------------------------------------------------
#With a JSON Payload  of {"state": "up"} – to change the state of the interfaces
@app.route('/<SW>/<INFID>', methods=['PATCH'])
def PATCHThisDescription(SW, INFID):
    payload = request.get_json()
    if request.get_json():
        result = mongo.db.Interfaces.find_one_and_update(
            {"Switch_name": SW, "_id": INFID},
            {'$set': payload},
            return_document = ReturnDocument.AFTER
        )
        return jsonify(result)
    return "Sorry, Could NOT Completed Your Valuable Request :("

#Finally, we can run our function---------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run()


