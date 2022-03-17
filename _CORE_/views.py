from django.shortcuts import render


def homepage(request):
    return render(request, 'pages/homepage.html')


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')
