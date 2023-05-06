from django.shortcuts import render
from .models import Chat, Group

def chat(request, group_name):
    ################Database work #####################
    group = Group.objects.filter(name=group_name).first()
    chats=[]
    if group:
        chats = Chat.objects.filter(group = group)
    else:
        group=Group(name=group_name)
        group.save()

    return render(request,'chat.html',{'group_name':group_name, 'chats':chats})
    #########################################################

    # return render(request,'chat.html',{'group_name':group_name})          #without database