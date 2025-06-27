from django.urls import path
from .views import (
    payment_dashboard_view,
    add_payment_card_view,
    delete_payment_card_view,
    redirect_to_payment_view,

)

urlpatterns = [
    path('', payment_dashboard_view, name='payment-dashboard'),
    path('add-card/', add_payment_card_view, name='add-payment-card'),
    path('delete-card/', delete_payment_card_view, name='delete-payment-card'),

    path('redirect_to_payment/', redirect_to_payment_view, name='redirect_to_payment'),
]
