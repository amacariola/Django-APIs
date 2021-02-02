from rest_framework import viewsets
from .models import Students
from .serializers import StudentsSerializer

# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('firstname')
    serializer_class = StudentsSerializer
