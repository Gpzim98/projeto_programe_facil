from django.shortcuts import render, redirect
from core.email import email
from django.core.mail import EmailMessage
from core.models import Lead
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver


@receiver(pre_social_login)
def new_user(request, sociallogin, **kwargs):
    lead = Lead(name=sociallogin.user.first_name, email=sociallogin.user.email, email_confirmed=True)
    if save_lead(lead) == 0:
        email(contact=lead, template='core/mail/email_confirmed.html', subject='Parabéns você foi incrível!')
        request.message = 'Brilhante, parabêns!, você foi cadastrado com sucesso!'
    else:
        request.message = 'Parabêns, você já esta cadastrado!'
    return request


def save_lead(lead):
    if Lead.objects.filter(email=lead.email).count() == 0:
        lead.code_confirm = hash_generator()
        lead.save()
        return 0
    else:
        return 1


def home(request):
    data = {}

    if request.method == 'POST':
        lead = Lead(name=request.POST.get('nome'), email=request.POST.get('email'))
        if save_lead(lead) == 0:
            data['message'] = 'Brilhante, parabêns!, você foi cadastrado com sucesso!'
            email(contact=lead, template='core/mail/client_subscribed.html', subject="Parabéns você foi incrível!")
        else:
            data['message'] = 'Parabêns, você já esta cadastrado!'

    return render(request, 'core/index.html', data)


def email_confim(request, code):
    try:
        lead = Lead.objects.get(code_confirm=code)
        lead.email_confirmed = True
        lead.save()
        email(contact=lead, template='core/mail/email_confirmed.html', subject='Parabêns, seu e-mail foi confirmado')
        return render(request, 'core/index.html', {'message': 'E-mail confirmado com sucesso'})
    except Exception as e:
        message = '''Oops, houve um problema durante a confirmacao do e-mail, por favor envie
                                     um email para contato@programefacil.com.br para que possamos resolver este problema
                                     pra você'''
        msg = EmailMessage('Fail at confirm email', message + str(e), to=('adm@programefacil.com.br',),
                           from_email='adm@programefacil.com.br')
        msg.send()
        return render(request, 'core/index.html',
                      {'message': message})


def thanks(request):
    return render(request, 'core/thanks.html')


def hash_generator():
    import random
    return ''.join(random.choice('0123456789ABCDEF') for i in range(25))


def email_teste(request, code):
    lead = Lead.objects.all()[0]
    return render(request, 'core/mail/client_subscribed.html', {'lead': lead, 'code': code})
