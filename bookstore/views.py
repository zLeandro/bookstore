from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.management import call_command

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        call_command("migrate")
        return HttpResponse("Migração feita com sucesso no Render!", status=200)
    return HttpResponse("Deploy manual não é necessário no Render.", status=200)