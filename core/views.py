from django.shortcuts import render
from core.email import email
from core.models import Lead
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver


@receiver(pre_social_login)
def new_user(request, sociallogin):
    lead = Lead(name='teste new user', email='contato@gregorypacheco.com.br')
    email(lead)
    request.message = 'teste new user'
    return request


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


def thanks(request):
    return render(request, 'core/thanks.html')
