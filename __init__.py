from flask import Flask, Blueprint
from distance_finder.routes import distance_finder

app = Flask(__name__)
app.register_blueprint(distance_finder.blueprint)

app.run(host = '10.1.3.11' ,port=8000, debug=True)
