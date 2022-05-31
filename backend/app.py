from distutils.debug import DEBUG
from flask import Flask, jsonify
from flask_cors import CORS

# config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# TODO this allows CORS from ANY domain, protocol, or port. This is not 
# acceptable, and needs to be changed to only allow requests from the frontends
# domain. See https://flask-cors.readthedocs.io/ for more.
CORS(app, resources={r'/*': {'origins':'*'}})  

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()