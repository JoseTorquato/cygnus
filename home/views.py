from django.shortcuts import render

def home_view(request):
    return render(request, 'teste.html')

def handler404(request, exception):
    return render(request, '404.html')
