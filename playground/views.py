from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        send_mail('subject', 'message',
                  'info@sanghubazar.com', ['anik@test.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'mosh'})
