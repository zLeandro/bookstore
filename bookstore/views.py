from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        return HttpResponse("Deploy manual não é necessário no Render.", status=200)
    else:
        return render(request, 'hello_world.html')