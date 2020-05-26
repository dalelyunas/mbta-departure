import pytz
from datetime import datetime

from mbta.RouteType import RouteType
from mbta.MbtaApi import mbtaApi
from mbta.Direction import Direction
from mbta.BoardEntry import BoardEntry

class BoardApi():
    def _isAfterNow(self, departureTime):
        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        time = datetime.fromisoformat(departureTime)
        return now <= time

    def getCommuterRailDepartures(self, station):
        predictionData = mbtaApi.getPredictionData(station, RouteType.COMMUTER_RAIL, Direction.DEPARTING)
        if not predictionData:
            return []
        entries = [BoardEntry(predD) for predD in predictionData]
        entries = [entry for entry in entries if self._isAfterNow(entry.time)]
        entries.sort(key=lambda dep: dep.time)
        return entries

boardApi = BoardApi()