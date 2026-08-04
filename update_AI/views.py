from django.shortcuts import render, redirect
from django.db.models import Q
from .models import training_text,AI
from django.db.models import Max
# Create your views here.
def AI_writing(request,ai_id):
    template='AI_writing.html'
    return render(request,template)
def update_AI(request,ai_id):
    ai = AI.objects.get(id=ai_id)
    if request.method == "POST":
            if request.POST["train_AI"] == '':
                return redirect("update_AI", ai_id=ai.id)
            ai = AI.objects.get(id=ai_id)
            max_num = training_text.objects.filter(user=request.user,ai=ai.id).aggregate(Max("name2"))["name2__max"]
            text=training_text()
            text.user_id=request.user.id
            text.text_saved=request.POST["train_AI"]
            if max_num==None:
                text.name2=1
            else:
                text.name2=max_num+1
            text.ai=ai
            text.save()
            return redirect("AI_text_list", ai_id=ai.id)
    else:
        training_texts=training_text.objects.all().values()
        context={"training_texts":training_texts,
                 'AI_id':ai_id,
                 "named":False}
        return render(
            request,
            "update_AI.html",
            context
        )
def update_AI2(request,ai_id,text_id):
     context={}
     return render(
                 request,
                 "update_AI.html",
                 context
             )
def text_rename(request,ai_id,text_id):
     context={}
     return render(
                 request,
                 "update_AI.html",
                 context
             )
def text_delete(request,ai_id,text_id):
     context={}
     return render(
                 request,
                 "update_AI.html",
                 context
             )
def AI_text_list(request,ai_id):
    template='AI_text_list.html'
    Text_results=training_text.objects.filter(user=request.user,ai=ai_id)
    ai = AI.objects.get(id=ai_id)
    context={'Text_results':Text_results,
             "ai":ai}
    return render(request,template,context)