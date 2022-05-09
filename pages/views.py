from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, "pages/homepage.html", context)
