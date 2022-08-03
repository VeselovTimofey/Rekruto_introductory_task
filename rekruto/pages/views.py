from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    name = str(request.GET.get("name", ""))
    message = str(request.GET.get("message", ""))
    context = {"name": name, "message": message}
    return render(request, "index.html", context)
