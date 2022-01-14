import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

List=[
      {'id': 1,
     'comment': '1',
     'user': '1',
                                                                                                                   
     }
     ]
@app.route('/api/v1/list', methods=['GET'])
def api_cards():
        return ("Api Deployed")


app.run(host="0.0.0.0",port="5004")
