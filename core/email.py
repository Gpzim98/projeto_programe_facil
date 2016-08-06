from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse

# EMAIL
FROM = 'contato@programefacil.com.br'
ADMINS = ['adm@programefacil.com.br']


def email(contact):
    subject = "Parabéns você foi incrível!"
    to = [contact.email]
    from_email = FROM

    ctx = {
        'user': contact.name,
        'purchase': 'Books'
    }

    message = get_template('core/mail/client_subscribed.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, bcc=ADMINS, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email')
