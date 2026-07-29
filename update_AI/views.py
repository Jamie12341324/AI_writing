from django.shortcuts import render

# Create your views here.
def AI_writing(request):
    template='AI_writing.html'
    return render(request,template)
def update_AI(request):
    template='update_AI.html'
    return render(request,template)