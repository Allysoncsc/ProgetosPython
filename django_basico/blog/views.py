from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print("blog")
    return render(request, "blog/index.html")


def exemplo(request):
    print("exemplo")
    return render(request, "blog/exemplo.html")
