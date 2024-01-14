from rest_framework import viewsets
from .serializer import tasksSerializer
from .models import User
# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = tasksSerializer
    queryset = User.objects.all()
