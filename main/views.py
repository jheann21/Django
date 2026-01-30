from django.shortcuts import render

def homepage(request):
    return render(request, 'main/homepage.html')
def about(request):
    return render(request, 'main/about.html')
def contact(request):
    return render(request, 'main/contact.html')
