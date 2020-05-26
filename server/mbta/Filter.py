from enum import Enum

class Filter():
    def __init__(self, filterType, value):
        self.type = filterType
        self.value = value

class FilterType(Enum):
    ROUTE = 'route'
    STOP = 'stop'
    DIRECTION_ID = 'direction_id'
    ROUTE_TYPE = 'route_type'