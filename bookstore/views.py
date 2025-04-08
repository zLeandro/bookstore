import os
import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        repo = git.Repo(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Code updated successfully", status=200)
    else:
        return render(request, 'hello_world.html')