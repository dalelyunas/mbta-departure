from datetime import datetime
import pytz

from mbta.RouteType import RouteType
from mbta.MbtaApi import mbtaApi
from mbta.Direction import Direction
from mbta.Departure import Departure

class BoardApi():
    def _isAfterNow(self, departureTime):
        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        time = datetime.fromisoformat(departureTime)
        return now <= time

    def getCommuterRailDepartures(self, station):
        predictionData = mbtaApi.getPredictionData(station, RouteType.COMMUTER_RAIL, Direction.DEPARTING)
        if not predictionData:
            return []
        departures = [Departure(predD) for predD in predictionData if self._isAfterNow(predD.getDepartureTime())]
        departures.sort(key=lambda dep: dep.departureTime)
        return departures

boardApi = BoardApi()