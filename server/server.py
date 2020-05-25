import json
from flask import Flask, Response, render_template
from flask_caching import Cache
from mbta.BoardApi import boardApi

config = {
    'DEBUG': True,
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 30
}
app = Flask(__name__, static_url_path='',
                  static_folder='../build',
                  template_folder='../build')
app.config.from_mapping(config)

cache = Cache(app)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/api/v1/stops/<stopId>/commuterRailDepartureBoard', methods=['GET'])
def commuterRailDepartureBoard(stopId):
    departures = cache.get(stopId)
    if not departures:
        departures = boardApi.getCommuterRailDepartures(stopId)
        cache.set(stopId, departures)
    return Response(json.dumps(departures), mimetype='application/json')

app.run()
