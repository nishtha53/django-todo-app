from django.shortcuts import render
from django.http import HttpResponse
from mytodo.models import ToDo

# Create your views here.
def home(request):
    template_name = 'home.html'
    todo_list = ToDo.objects.all()
    #print(todo_list)
    context = {'app_name':'todoapp','todo_list':todo_list}
    return render(request,template_name,context=context)