from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.management import call_command

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        return HttpResponse("Servidor alcançado. Tudo certo até aqui!", status=200)
    return HttpResponse("GET não é usado aqui.", status=200)