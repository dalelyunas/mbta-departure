from mbta.Carrier import Carrier

class PredictionData():
    def __init__(self, prediction, schedule, stop, trip, direction):
        self.prediction = prediction
        self.stop = stop
        self.schedule = schedule
        self.trip = trip
        self.direction = direction

    def getDepartureTime(self):
        if self.prediction:
            predDepart = self.prediction['departure_time']
            if predDepart:
                return predDepart
        if self.schedule:
            return self.schedule['departure_time']
        return None

    def getDirection(self):
        return self.direction

    def getDestination(self):
        if self.trip:
            return self.trip['headsign']
        return None

    def getTrain(self):
        if self.trip:
            return self.trip['name']
        return None

    def getTrack(self):
        if self.stop:
            return self.stop['platform_code']
        return None

    def getStatus(self):
        if self.prediction:
            return self.prediction['status']
        return None

    def getCarrier(self):
        return Carrier.MBTA.value
