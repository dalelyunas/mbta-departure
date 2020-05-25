from collections import defaultdict

import requests

from mbta.Filter import Filter, FilterType
from mbta.Resource import Resource
from mbta.Departure import Departure
from mbta.PredictionData import PredictionData


class MbtaApi():
    def __init__(self):
        self.BASE_URL = 'https://api-v3.mbta.com/'

    def _getResource(self, path, filters, resources):
        params = {}
        for filter in filters:
            params[filter.type.value] = filter.value
        params['include'] = ','.join([resource.value for resource in resources])
        response = requests.get(self.BASE_URL + path, params)
        return response.json()

    # get prediction data for the provided station
    # the data includes schedule, trip, stop, and prediction information
    def getPredictionData(self, station, routeType, direction):
        resources = [Resource.STOP, Resource.SCHEDULE, Resource.TRIP]
        filters = []
        filters.append(Filter(FilterType.DIRECTION_ID, direction.value))
        filters.append(Filter(FilterType.STOP, station))
        filters.append(Filter(FilterType.ROUTE_TYPE, routeType.value))

        raw = self._getResource('predictions', filters, resources)
        
        if not raw:
            return []

        schedules = {}
        trips = {}
        stops = {}
        
        if 'included' in raw:
            for resource in raw['included']:
                resourceType = resource['type']
                if resourceType == Resource.SCHEDULE.value:
                    schedules[resource['id']] = resource
                elif resourceType == Resource.STOP.value:
                    stops[resource['id']] = resource
                elif resourceType == Resource.TRIP.value:
                    trips[resource['id']] = resource
        
        predictionData = []
        for prediction in raw['data']:
            relationships = prediction['relationships']
            schedule = schedules.get(relationships['schedule']['data']['id'], {}) 
            trip = trips.get(relationships['trip']['data']['id'], {})
            stopId = relationships['stop']['data']['id']
            stop = stops.get(stopId, {})
            predictionData.append(PredictionData(prediction['attributes'], schedule['attributes'], stop['attributes'], trip['attributes'], direction))

        return predictionData

mbtaApi = MbtaApi()
