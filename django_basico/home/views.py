from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    print("home")

    context = {"text": "Olá home"}

    return render(request, "home/index.html", context)
