from django.conf import settings
from django.core import mail
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    """Dispacher - Ponto de Entrada"""
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    """Se o pedido vier como GET - mostra o formulário vazio"""
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def create(request):
    """Se o pedido vier como POST"""
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        """Caso de insucesso - aborta o pedido"""
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    """Caso de sucesso!"""

    # Send email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    # # Success feedback
    # messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist: #Levanta o erro se não existir na base de dados.
        raise Http404


    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
