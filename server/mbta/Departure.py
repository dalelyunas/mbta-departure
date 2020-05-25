import json

from mbta.Direction import Direction

class Departure():
    def __init__(self, predictionData):
        if predictionData.direction != Direction.DEPARTING:
            raise ValueError('invalid direction for departure') 
        self.carrier = predictionData.getCarrier()
        self.departureTime = predictionData.getDepartureTime()
        self.destination = predictionData.getDestination()
        self.train = predictionData.getTrain()
        self.track = predictionData.getTrack()
        self.status = predictionData.getStatus()
    
    def getDict(self):
        return self.__dict__

    def __eq__(self, other):
        if isinstance(other, Departure):
            return (
                self.departureTime == other.departureTime and
                self.destination == other.destination and
                self.train == other.train and
                self.track == other.track and
                self.status == other.status and
                self.carrier == other.carrier
            )
        return False