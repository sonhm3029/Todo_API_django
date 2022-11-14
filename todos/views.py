from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.

from .serializers import TodoSerializer
from .models import Todo

class TodoListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer