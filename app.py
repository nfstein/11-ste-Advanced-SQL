import app_data as ad
from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def main():
    __name__ = "__main__"
    endpoints = [
        "/test_data",
        "/api/v1.0/precipitation",
        "/api/v1.0/stations",
        "/api/v1.0/tobs",
        "/api/v1.0/<start>",
        "/api/v1.0/<start>/<end>",

    ]
    return jsonify(endpoints)

@app.route("/test_data")
def test():
    return ad.test_1

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(ad.precipitation())

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(ad.stations())

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(ad.tobs())

@app.route("/api/v1.0/<start>")
def then_on(start):
    return jsonify(ad.temp_for_range(start))

@app.route("/api/v1.0/<start>/<end>")
def for_range(start, end):
    return jsonify(ad.temp_for_range(start, end))

if __name__ == "__main__":
    app.run()#debug = True)