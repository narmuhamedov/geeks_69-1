from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

#CRUD

class CreateTodoView(generic.CreateView):
    template_name = 'create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        return super(CreateTodoView, self).form_valid(form=form)




#CREATE
# def create_todo_view(request):
#     if request.method == "POST":
#         form_todo = forms.TodoForm(request.POST)
#         if form_todo.is_valid():
#             form_todo.save()
#             return redirect('/todo_list/')
#     else:
#         form_todo = forms.TodoForm()
#     return render(request, 'create_todo.html', {'form': form_todo})

#READ
class ReadTodoView(generic.ListView):
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'
    model = models.Todo
    ordering = ['-id']


# def read_todo_view(request):
#     if request.method == "GET":
#         todo_list = models.Todo.objects.all().order_by('-id')
#     return render(request, 'todo_list.html', {'todo_list': todo_list})

#UPDATE

class UpdateTodoView(generic.UpdateView):
    template_name = 'update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Todo, id=todo_id)

    def form_valid(self, form):
        return super(UpdateTodoView,self).form_valid(form=form)
        





# def update_todo_view(request, id):
#     todo_id = get_object_or_404(models.Todo, id=id)
#     if request.method == "POST":
#         form_todo = forms.TodoForm(request.POST, instance=todo_id)
#         if form_todo.is_valid():
#             form_todo.save()
#             return redirect('/todo_list/')
#     else:
#         form_todo = forms.TodoForm(instance=todo_id)
#     return render(request, 'update_todo.html', {'form': form_todo})

#DELETE

class DeleteTodoView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'todo_id'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Todo, id=todo_id)
    






# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.Todo, id=id)
#     todo_id.delete()
#     return redirect('/todo_list/')