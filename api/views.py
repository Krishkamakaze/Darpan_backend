from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'rollnumber'

    def retrieve(self, request, *args, **kwargs):
        rollnumber = kwargs.get('rollnumber')
        queryset = self.get_queryset().filter(rollnumber=rollnumber)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StatusSearch(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['status']

