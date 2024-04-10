from rest_framework import generics, permissions
from .models import Todo
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .serializers import TodoSerializer
from .pagination import StandardResultspagination


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultspagination

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
