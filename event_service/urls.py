from django.urls import path
from .views import (
    EventCreateView,
    EventDetailUpdateView,

)
from . import views
urlpatterns = [
    path('api/events/', EventCreateView.as_view(), name='event-create'),
    path('api/events/<int:id>/', EventDetailUpdateView.as_view(), name='event-detail-api'),


]

