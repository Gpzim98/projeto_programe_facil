from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse

# EMAIL
FROM = 'contato@programefacil.com.br'
ADMINS = ['adm@programefacil.com.br']


def email(contact, template, subject):
    to = [contact.email]
    from_email = FROM

    ctx = {
        'user': contact.name,
        'code_confirm': contact.code_confirm,
    }

    message = get_template(template).render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, bcc=ADMINS, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email')
