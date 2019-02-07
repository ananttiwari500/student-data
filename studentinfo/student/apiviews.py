from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import StudentData
from  .serializers import StudentSerializer

# class StudentList(APIView):
#     def get(self, request):
#         stu = StudentData.objects.all()[:20]
#         data = StudentSerializer(stu, many=True).data
#         return Response(data)


class StudentList(generics.ListCreateAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer


# class StudentDetail(APIView):
#     def get(self, request, pk):
#         st = get_object_or_404(StudentData, pk=pk)
#         data = StudentSerializer(st).data
#         return Response(data)


class StudentDetail(generics.RetrieveDestroyAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer

