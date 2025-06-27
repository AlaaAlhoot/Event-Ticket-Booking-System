from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.decorators import login_required
from .models import Complaint

def complaint_form_view(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, user=request.user)
        if form.is_valid():
            complaint = form.save(commit=False)
            if request.user.is_authenticated:
                complaint.user = request.user
                complaint.full_name = request.user.get_full_name()
                complaint.email = request.user.email
            complaint.save()
            messages.success(request, "✅ Your complaint has been submitted.")
            return redirect('complaint-form')
    else:
        form = ComplaintForm(user=request.user)

    return render(request, 'complaint_form.html', {'form': form})





@login_required
def complaints_list_view(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'complaints_list.html', {'complaints': complaints})
