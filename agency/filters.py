import django_filters
from django_filters import CharFilter,NumberFilter,ChoiceFilter
from .models import CAR,CAR_MODEL

FUEL_CHOICES = (
        ('PETROL', 'PETROL'),
        ('DIESEL', 'DIESEL'),
    )
BODY_CHOICES = (
    ('HATCHBACK', 'HATCHBACK'),
    ('SEDAN', 'SEDAN'),
    ('COUPE', 'COUPE'),
    ('STATION WAGON', 'STATION WAGON'),
    ('CONVERTABLE', 'CONVERTABLE'),
)
TRANSMISSION_CHOICES = (
    ('MANUAL', 'MANUAL'),
    ('AUTOMATIC', 'AUTOMATIC'),
)
class CarFilter(django_filters.FilterSet):
    color = CharFilter(field_name="color", lookup_expr='icontains',label='Color')
    fare = NumberFilter(field_name="fare__car_fare", lookup_expr='lte',label='Max Fare')
    fuel = ChoiceFilter(choices=FUEL_CHOICES)
    car_model__engine_capacity = NumberFilter(field_name="car_model__engine_capacity", lookup_expr='icontains',label='Max Engine Capacity')
    car_model__transmission = ChoiceFilter(choices=TRANSMISSION_CHOICES)
    car_model__body_type = ChoiceFilter(choices=BODY_CHOICES)
    class Meta:
        model = CAR
        fields = ['color','fare','car_model__engine_capacity']
