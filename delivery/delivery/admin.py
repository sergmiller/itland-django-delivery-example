from django.contrib import admin
from .models.delivery_base import DeliveryBase
from .models.edge import Edge, TypeOfEdge
from .models.location import Location
from .models.order import Order
from .models.route import Route
from .models.service import Service


admin.site.register(DeliveryBase)
admin.site.register(Edge)
admin.site.register(TypeOfEdge)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Route)
admin.site.register(Service)

