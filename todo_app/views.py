from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_app/todo_list.html'  # Updated path
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'  # Updated path
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'  # Updated path
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_app/todo_confirm_delete.html'  # Add this template if needed
    success_url = reverse_lazy('todo_list')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todo_app/register.html', {'form': form})  # Updated path

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})  # Updated path

def logout_view(request):
    logout(request)
    return redirect('login')