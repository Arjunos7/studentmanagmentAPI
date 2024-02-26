from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status






class Studentlist(APIView):  #non primary key based class view
    def get(self,request):
        students = Student.objects.all()
        s=StudentSerializer(students,many=True)
        return Response(s.data)
    def post(self,request):
        s = StudentSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)







class Studentdetail(APIView):  #primary  key based
    def get_object(self,request,pk):
        try:
           return Student.objects.get(pk=pk)
        except:
           raise Http404

    def get(self,request,pk):
        student=self.get_object(request,pk)
        s = StudentSerializer(student)
        return Response(s.data)

    def put(self,request,pk):
        student=self.get_object(request,pk)
        s = StudentSerializer(student, data=request.data)

        if s.is_valid():
                s.save()
                return Response(s.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        student=self.get_object(request,pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




