from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import tasks
from . forms import ToDo_form
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.

class Task_list(ListView):
    model = tasks
    template_name = 'home.html'
    context_object_name = 'task'

class Task_detail(DetailView):
    model = tasks
    template_name = 'detail.html'
    context_object_name = 'tk'

class Task_update(UpdateView):
    model = tasks
    template_name = 'update.html'
    context_object_name = 'tku'
    fields = ['names','priorities','dates']

    def get_success_url(self):
        return reverse_lazy('cld', kwargs={'pk': self.object.id})

class Taskdelete(DeleteView):
    model = tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('clb')

def set(request):
    detail = tasks.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        prioritiez=request.POST.get('priority')
        date=request.POST.get('date')
        accept=tasks(names=name,priorities=prioritiez,dates=date)
        accept.save()
    return render(request,'home.html',{'task':detail})

# def details(request):
#
#
#     return render(request,'detail.html',)
def delete(request,taskid):
    task1 = tasks.objects.get(id=taskid)
    if request.method == 'POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    updating=tasks.objects.get(id=id)
    updates=ToDo_form(request.POST or None,instance=updating)
    if updates.is_valid():
        updates.save()
        return redirect('/')
    return render(request,'edit.html',{'ups':updating,'up':updates})