from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user_service.models import UserProfile
from .models import PaymentCard
from ticket_service.models import Ticket
from event_service.models import Reservation
from django.core.paginator import Paginator




@login_required
def payment_dashboard_view(request, secure_token):
    try:
        profile = UserProfile.objects.get(secure_token=secure_token)
    except UserProfile.DoesNotExist:
        return render(request, 'access_denied.html')

    if request.user != profile.user or profile.role != "attendee":
        return render(request, 'access_denied.html')

    card = PaymentCard.objects.filter(user=request.user).first()
    all_reservations = Reservation.objects.filter(user=request.user, event__is_deleted=False).select_related('event').order_by('-created_at')

    total_spent = sum(r.total_price for r in all_reservations)

    paginator = Paginator(all_reservations, 4)
    page_number = request.GET.get('page')
    reservations_page = paginator.get_page(page_number)


    page_total = sum(r.total_price for r in reservations_page)

    return render(request, 'payment_dashboard.html', {
        'card': card,
        'reservations': reservations_page,
        'total_spent': total_spent,
        'page_total': page_total,
        'months': [f"{i:02}" for i in range(1, 13)],
        'years': [str(y) for y in range(2025, 2031)],
        'secure_token': secure_token,
    })


@login_required
def add_payment_card_view(request, secure_token):
    profile = UserProfile.objects.filter(secure_token=secure_token).first()
    if not profile or profile.user != request.user or profile.role != 'attendee':
        return render(request, 'access_denied.html')

    if request.method == 'POST':
        if PaymentCard.objects.filter(user=request.user).exists():
            messages.error(request, "Card already added.", extra_tags='payment')
            return redirect('payment-dashboard', secure_token=secure_token)

        PaymentCard.objects.create(
            user=request.user,
            card_holder=request.POST['card_holder'],
            card_number=request.POST['card_number'],
            card_type=request.POST['card_type'],
            expiry_month=request.POST['expiry_month'],
            expiry_year=request.POST['expiry_year']
        )
        messages.success(request, "✅ Card added successfully.", extra_tags='payment swal')
        return redirect('payment-dashboard', secure_token=secure_token)


@login_required
def delete_payment_card_view(request, secure_token):
    profile = UserProfile.objects.filter(secure_token=secure_token).first()
    if not profile or profile.user != request.user or profile.role != 'attendee':
        return render(request, 'access_denied.html')

    PaymentCard.objects.filter(user=request.user).delete()
    messages.success(request, "🗑 Card deleted successfully.", extra_tags='payment')
    return redirect('payment-dashboard', secure_token=secure_token)




@login_required
def redirect_to_payment_view(request, secure_token):
    return render(request, 'redirect_to_payment.html', {'secure_token': secure_token})