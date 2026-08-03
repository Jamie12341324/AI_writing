from django.shortcuts import render
from django.http import HttpResponse
from .models import AI
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def home(request):
    template='home.html'
    return render(request,template)
#@login_required(login_url="/accounts/login/")
# AI_create
# returns you back to the same page (AI_create) if you have not given a name to create an AI with or
# an AI with that name already exists
# if you have given an AI name then it is saved and you are sent to the AI list page
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
 # AI_create2
# does a similar job to AI_create but it is for renaming an AI instead of creating one
# returns you back to the same page (meal_create2) if you have not given a name to rename an AI with or
# an AI with that name already exists
# if you have given an AI name then it is saved and you are sent to the AI list page
def AI_create2(request,ai_id):
    ais=AI.objects.all().values()
    ai=AI.objects.get(id=ai_id)
    AI_name=ai.name
    if request.method == "POST":
        if request.POST["AI_name"] == '':
            return redirect("AI_create2", ai_id=ai.id)
        AI_records = AI.objects.filter(Q(name=request.POST["AI_name"]) & Q(user_id=request.user.id)).values()
        if AI_records.exists():
            return redirect("AI_create2", ai_id=ai.id)
        ai.name=request.POST["AI_name"]
        ai.save()
        return redirect("your_AI_list")
    else:
        named=True
        context={"AI_name": AI_name,
                 "named": named,
                 "AIs": ais,}
        return render(
            request,
            "AI_create.html",
            context
        )   
def your_AI_list(request):
    AI_results = AI.objects.filter(Q(user_id=request.user.id)).values().order_by("id")
    context = {
        'AI_results': AI_results,
    }
    template ='your_AI_list.html'
    return render(request,template,context)
def AI_delete(request,ai_id):
    ai_to_delete= AI.objects.get(Q(id=ai_id) & Q(user_id=request.user.id))
    ai_to_delete.delete()
    return redirect("your_AI_list")