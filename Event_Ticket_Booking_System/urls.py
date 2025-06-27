from django.contrib import admin
from django.urls import path, include
from Event_Ticket_Booking_System.views import (
    home_view,
    event_detail_view,
    booking_success_view,
    about_view,
    organizer_dashboard_view,
    event_create_view,
    supervisor_panel_view,
    complaint_form_view,

    not_found_view,
    search_view,
    book_ticket_view,
    edit_event_view,
    delete_event_view,
    my_tickets_attendee,
    download_ticket_pdf,
    delete_reservation,
)
from user_service.views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    edit_profile_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Microservices
    path('api/', include('user_service.urls')),
    path('api/', include('ticket_service.urls')),
    path('api/', include('organizer_service.urls')),
    path('complaints/', include('complaint_service.urls')),
    path('user/<str:secure_token>/payment/', include('payment_service.urls')),

    # Public Views
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('search/', search_view, name='search'),

    # Event
    path('events/<int:event_id>/', event_detail_view, name='event-detail'),

    # Auth
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # User
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit-profile'),

    # Organizer
    path('organizer/<str:secure_token>/dashboard/', organizer_dashboard_view, name='organizer-dashboard'),
    path('organizer/<str:secure_token>/events/new/', event_create_view, name='event-create'),
    path('organizer/<str:secure_token>/event/<int:event_id>/edit/', edit_event_view, name='edit_event'),
    path('organizer/<str:secure_token>/event/<int:event_id>/delete/', delete_event_view, name='delete_event'),

    path('attendee-tickets/<str:secure_token>/', my_tickets_attendee, name='my_tickets_attendee'),
    path('delete-reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),


    # Supervisor
    path('supervisor/dashboard/', supervisor_panel_view, name='supervisor-panel'),

    # Complaints
    path('complaints/new/', complaint_form_view, name='complaint-form'),

    # Booking
    path('events/<int:event_id>/book/<str:secure_token>/', book_ticket_view, name='book-ticket'),
    path('booking-success/', booking_success_view, name='booking-success'),


    path('event/', include('event_service.urls')),
    path('download-ticket/<int:reservation_id>/', download_ticket_pdf, name='download_ticket'),
]

handler404 = not_found_view
