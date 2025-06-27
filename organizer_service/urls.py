from django.urls import path
from .views import OrganizerCreateView, OrganizerListView

urlpatterns = [
    path('organizers/', OrganizerListView.as_view(), name='organizer-list'),
    path('organizers/create/', OrganizerCreateView.as_view(), name='organizer-create'),
]
