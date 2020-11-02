from graphene import ObjectType, String, List, Int
from graphene_django import DjangoObjectType

class Route(ObjectType):
    id = String()
    direction_names = List(String)

class Stop(ObjectType):
    id = String()

class Departure(ObjectType):
    id = String()
    departure_time = String()
    direction_id = Int()
    route_id = String()