from django.urls import path
from .views import complaint_form_view, complaints_list_view

urlpatterns = [
    path('new/', complaint_form_view, name='complaint-form'),
    path('', complaints_list_view, name='complaint-list'),
]



