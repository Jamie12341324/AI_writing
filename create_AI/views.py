from django.shortcuts import render

# Create your views here.
def home(request):
    template='home.html'
    return render(request,template)
def AI_create(request):
    template='AI_create.html'
    return render(request,template)
def your_AI_list(request):
    template='your_AI_list.html'
    return render(request,template)