from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('todo/update/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]