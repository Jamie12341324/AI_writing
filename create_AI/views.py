from django.shortcuts import render
from .models import AI
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def home(request):
    template='home.html'
    return render(request,template)
#@login_required(login_url="/accounts/login/")
# meal_create
# returns you back to the same page (meal_create) if you have not given a name to create a meal with or
# a meal with that name already exists
# if you have given a meal name then it is saved and you are sent to the meal list page
def AI_create(request):
    if request.method == "POST":
        if request.POST["AI_name"] == '':
            return redirect("/AI_create/")
        ai_records = AI.objects.filter(Q(name=request.POST["AI_name"]) & Q(user_id=request.user.id)).values()
        if not ai_records.exists():
            ai=AI()
            ai.user_id=request.user.id
            ai.name=request.POST["AI_name"]
            ai.save()
            return redirect("your_AI_list")
        else:
            return redirect("AI_create")
    else:
        AIs=AI.objects.all().values()
        context={"AIs":AIs,}
        return render(
            request,
            "AI_create.html",
            context
        )
    
def your_AI_list(request):
    template='your_AI_list.html'
    return render(request,template)