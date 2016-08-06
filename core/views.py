from django.shortcuts import render
from core.email import email
from core.models import Lead


def home(request):
    if request.method == 'POST':
        lead = Lead(name=request.POST.get('nome'), email=request.POST.get('email'))
        lead.save()
        email(lead)

    return render(request, 'core/index.html')
