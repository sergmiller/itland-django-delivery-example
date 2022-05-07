from django.core.management.base import BaseCommand
from delivery.models.edge import *
from delivery.models.location import *


class Command(BaseCommand):
    def _initialize(self):
        locations = [Location(location_name='Лондон'),
                     Location(location_name='Москва'),
                     Location(location_name='Владивосток'),
                     Location(location_name='Казань')]
        loc_ids = []
        for loc in locations:
            loc.save()
            loc_ids.append(loc.id)
        type_ids = []
        types = [TypeOfEdge(cost=50, max_weight=10, name='Самолет'),
                 TypeOfEdge(cost=500, max_weight=1000, name='Контейнер'),
                 TypeOfEdge(cost=1, max_weight=20, name='Поезд')
                 ]
        for type_ in types:
            type_.save()
            type_ids.append(type_.id)
        edges = [Edge(start_location=locations[2], end_location=locations[1], edge_type_id=types[1],
                      length=8000),
                 Edge(start_location=locations[1], end_location=locations[2], edge_type_id=types[1],
                      length=8000),
                 Edge(start_location=locations[1], end_location=locations[0], edge_type_id=types[0],
                     length=8000),
                 Edge(start_location=locations[0], end_location=locations[1], edge_type_id=types[0],
                      length=8000),
                 Edge(start_location=locations[3], end_location=locations[1], edge_type_id=types[2],
                      length=10),
                 Edge(start_location=locations[1], end_location=locations[3], edge_type_id=types[2],
                      length=10)
                 ]
        for edge in edges:
            edge.save()

    def handle(self, *args, **options):
        self._initialize()
