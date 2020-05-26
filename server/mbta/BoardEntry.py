import json

from mbta.Direction import Direction

class BoardEntry():
    def __init__(self, predictionData):
        self.direction = predictionData.direction
        self.carrier = predictionData.getCarrier()
        if self.direction == Direction.DEPARTING:
            self.time = predictionData.getDepartureTime()
        self.destination = predictionData.getDestination()
        self.train = predictionData.getTrain()
        self.track = predictionData.getTrack()
        self.status = predictionData.getStatus()
    
    def getDict(self):
        return self.__dict__

    def __eq__(self, other):
        if isinstance(other, BoardEntry):
            return (
                self.time == other.time and
                self.destination == other.destination and
                self.train == other.train and
                self.track == other.track and
                self.status == other.status and
                self.carrier == other.carrier and
                self.direction == other.direction
            )
        return False