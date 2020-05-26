import json
from flask import Flask, Response, render_template
from flask_caching import Cache
from mbta.BoardApi import boardApi

config = {
    'DEBUG': True,
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 30
}
app = Flask(__name__, static_url_path='', static_folder='../build', template_folder='../build')
app.config.from_mapping(config)

cache = Cache(app)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/api/v1/stations/<station>/commuterRailDepartures', methods=['GET'])
def commuterRailDepartureBoard(station):
    departures = cache.get(station)
    if departures == None:
        departures = boardApi.getCommuterRailDepartures(station)
        cache.set(station, departures)
    return Response(json.dumps([dep.getDict() for dep in departures]), mimetype='application/json')

app.run()
