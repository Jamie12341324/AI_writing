from django.shortcuts import render, redirect
from django.db.models import Q
from .models import training_text,AI,AI_values
from django.db.models import Max
from Mimic1_creative import Records
import random
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
            max_num = training_text.objects.filter(user=request.user,ai=ai.id).aggregate(Max("number"))["number__max"]
            text=training_text()
            text.user_id=request.user.id
            text.text_saved=request.POST["train_AI"]
            if max_num==None:
                text.name2=str(1)
                text.number=1
            else:
                num=max_num+1
                text.name2=str(num)
                text.number=num
            text.ai=ai
            text.save()
            records=Records()
            records.test_full_sequence(text.text_saved,random.randint(0,4))
            ai_values=AI_values()
            ai_values.value_checks=records.test_A
            ai_values.value_answers=records.answer_A
            ai_values.group=records.data_group_num_A
            ai_values.user_id = request.user.id
            ai_values.name2 = text.name2
            ai_values.number = text.number
            ai_values.ai = ai
            ai_values.save()
            return redirect("AI_text_list", ai_id=ai.id)
    else:
        training_texts=training_text.objects.all().values()
        context={"training_texts":training_texts,
                 'AI_id':ai_id,
                 "new":False,
                 "text":"",}
        return render(
            request,
            "update_AI.html",
            context
        )
def update_AI2(request,ai_id,text_id):
     ai = AI.objects.get(id=ai_id)
     if request.method == "POST":
        if request.POST["train_AI"] == '':
            return redirect("update_AI", ai_id=ai.id)
        text=training_text.objects.get(user=request.user,ai=ai.id,id=text_id)
        text.text_saved=request.POST["train_AI"]
        text.save()
        return redirect("AI_text_list", ai_id=ai.id)
     else:
        text=training_text.objects.get(user=request.user,ai=ai.id,id=text_id)
        context={'AI_id':ai_id,
                "new":True,
                "text":text.text_saved}
        return render(
                    request,
                    "update_AI.html",
                    context
                )
def text_rename(request,ai_id,text_id):
    if request.method=="POST":
        text_to_rename=training_text.objects.get(user=request.user,ai=ai_id,id=text_id)
        text_to_rename.name2=request.POST["text_name"]
        text_to_rename.save()
        context={'AI_id':ai_id,}
        ai = AI.objects.get(id=ai_id)
        return redirect("AI_text_list", ai_id=ai.id)
    else:
        existing_text=training_text.objects.get(user=request.user,ai=ai_id,id=text_id)
        existing_text_name=existing_text.name2
        text_names=training_text.objects.filter(user=request.user,ai=ai_id).values()
        context={'AI_id':ai_id,
                 'text_name':existing_text_name,
                 'text_names':text_names}
        return render(request,'text_rename.html',context)
def text_delete(request,ai_id,text_id):
     text_to_delete=training_text.objects.filter(user=request.user,ai=ai_id,id=text_id)
     text_to_delete.delete()
     context={}
     ai = AI.objects.get(id=ai_id)
     return redirect("AI_text_list", ai_id=ai.id)
def AI_text_list(request,ai_id):
    template='AI_text_list.html'
    Text_results=training_text.objects.filter(user=request.user,ai=ai_id)
    ai = AI.objects.get(id=ai_id)
    context={'Text_results':Text_results,
             "ai":ai}
    return render(request,template,context)