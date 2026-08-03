from django.shortcuts import render, redirect
from django.db.models import Q
from .models import training_text,AI
# Create your views here.
def AI_writing(request,ai_id):
    template='AI_writing.html'
    return render(request,template)
def update_AI(request,ai_id):
    template='update_AI.html'
    #return render(request,template,context)
    if request.method == "POST":
            if request.POST["train_AI"] == '':
                return redirect("update_AI", ai_id=ai.id)
            ai_training_records = training_text.objects.filter(Q(user_id=request.user.id)).values()
            if not ai_training_records.exists():
                ai = AI.objects.get(id=ai_id)
                count = training_text.objects.filter(user=request.user,ai=ai.id).count()+1
                text=training_text()
                text.user_id=request.user.id
                text.text_saved=request.POST["train_AI"]
                text.name2=count
                text.ai=ai
                text.save()
                return redirect("AI_text_list", ai_id=ai.id)
            else:
                return redirect("update_AI", ai_id=ai.id)
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
def AI_text_list(request,ai_id):
    template='AI_text_list.html'
    return render(request,template)