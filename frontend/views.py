from django.shortcuts import render

# Create your views here.
def indexView(request, *args, **kwargs):
    return render(request, "frontend/index.html")