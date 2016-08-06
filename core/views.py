from django.shortcuts import render
from core.email import email
from core.models import Lead


def home(request):
    data = {}

    if request.method == 'POST':
        lead = Lead(name=request.POST.get('nome'), email=request.POST.get('email'))

        try:
            lead.save()
            data['message'] = 'Parabêns, você foi cadastrado com sucesso!'
            email(lead)
        except:
            data['message'] = 'Parabêns, você já esta cadastrado!'

    return render(request, 'core/index.html', data)
