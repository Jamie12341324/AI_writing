from django.shortcuts import render, redirect
from django.db.models import Q
from .models import training_text,AI,ai_values
from django.db.models import Max
# . from chatgpt used for import non-django file from another one of my project
from .Mimic1_creative import Records
import random
# Create your views here.
def AI_writing(request,ai_id):
    template='AI_writing.html'
    ai = AI.objects.get(id=ai_id)
    if request.method=="POST":
        records=Records()
        #records.test_full_sequence("Hi there are you ok.",1)
        #records.test_full_sequence("Hi there are you ok.",2)
        #records.test_full_sequence("Hi there are you ok.",3)
        #records.test_full_sequence("Hi there are you ok.",4)
        records.use=False
        ai_values_to_use_A=ai_values.objects.filter(user=request.user,ai=ai.id)
        for ai_values_to_use in ai_values_to_use_A:
            print("ai_values_to_use",ai_values_to_use.group)
            c=0
            L1=len(ai_values_to_use.value_checks)
            while c<L1:
                L2=len(records.test_A)
                if c==L2:
                    records.test_A.append([])
                    records.answer_A.append([])
                    records.data_group_num_A.append([])
                c2=0
                L2=len(ai_values_to_use.value_checks[c])
                while c2<L2:
                    records.test_A[c].append(ai_values_to_use.value_checks[c][c2])
                    records.answer_A[c].append(ai_values_to_use.value_answers[c][c2])
                    records.data_group_num_A[c].append(ai_values_to_use.group[c][c2])
                    c2=c2+1
                c=c+1
        print("records.answer_A",records.answer_A)
        starting_text=request.POST["talk_AI"]
        info="hello"
        info=records.text_central_loop3(starting_text)
        context={"response_text":info,
                 "starting_text":starting_text}
        return render(request,template,context)
    else:
        context={}
        return render(request,template,context)
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
            ai_values_to_save=ai_values()
            ai_values_to_save.value_checks=records.test_A
            ai_values_to_save.value_answers=records.answer_A
            ai_values_to_save.group=records.data_group_num_A
            ai_values_to_save.user_id = request.user.id
            ai_values_to_save.name2 = text.name2
            ai_values_to_save.number = text.number
            ai_values_to_save.ai = ai
            ai_values_to_save.training_text=text
            ai_values_to_save.save()
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
        records=Records()
        records.test_full_sequence(text.text_saved,random.randint(0,4))
        ai_values_to_save=ai_values.objects.get(user=request.user, training_text=text.id)
        ai_values_to_save.value_checks=records.test_A
        ai_values_to_save.value_answers=records.answer_A
        ai_values_to_save.group=records.data_group_num_A
        ai_values_to_save.save()
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
        ai_values_to_save=ai_values.objects.get(user=request.user, training_text=text_to_rename.id)
        ai_values_to_save.name2=text_to_rename.name2
        ai_values_to_save.save()
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