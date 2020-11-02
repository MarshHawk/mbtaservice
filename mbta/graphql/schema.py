import graphene
from collections import namedtuple
from .types import Route, Stop, Departure
from requests.auth import HTTPBasicAuth
import requests
import os

apikey = os.getenv('API_KEY')
auth = HTTPBasicAuth('apikey', apikey)

class Query(graphene.ObjectType):
    routes = graphene.List(Route)
    stops = graphene.List(Stop, routeId=graphene.String())
    departures = graphene.List(
        Departure, stopId=graphene.String())

    def resolve_routes(self, info):
        url = "https://api-v3.mbta.com/routes?filter[type]=0,1"
        req = requests.get(url, auth=auth)
        data = req.json()['data']
        routes = [{'id': d['id'],
                  'direction_names': d['attributes']['direction_names']} for d in data]
        return routes

    def resolve_stops(self, info, routeId):
        url = 'https://api-v3.mbta.com/stops?filter[route]={}'.format(routeId)
        req = requests.get(url, auth=auth)
        return req.json()['data']

    def resolve_departures(self, info, stopId):
        url = 'https://api-v3.mbta.com/predictions?filter[stop]={},sort=departure_time'.format(
            stopId)
        req = requests.get(url, auth=auth)
        data = req.json()['data']
        departures = [
            {'id': d['id'],
             'direction_id': d['attributes']['direction_id'],
             'departure_time': d['attributes']['departure_time'],
             'route_id': d['relationships']['route']['data']['id']} for d in data]
        return departures

schema = graphene.Schema(query=Query, types=[Route])
