from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import TaskSerializer
from api.models import Task
import io
from rest_framework.parsers import JSONParser

# Create your views here.

"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

"""
Below Function going to display all the tasks store in the data base.
"""
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    Serializer = TaskSerializer(tasks)
    # converting python data to json data  import json renderer
    # json_data = JSONRenderer().render(Serializer.data)

    # return HttpResponse(json_data , content_type ='application/json')
    
    return JsonResponse(Serializer.data ,safe= False )

    # return Response(Serializer.data)



@api_view(['POST'])
def taskCreate(request):
    # json_data = request.body
    # stream = io.BytesIO(json_data)
    # pythondata = JSONParser().parse(stream)
    # serializer = TaskSerializer(data=pythondata)
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        # if serialized data is valid then data will be saved into db
        serializer.save()
    # return Response(serializer.data)
    return JsonResponse(serializer.data ,safe= False )




@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    # json_data = request.body
    # stream = io.BytesIO(json_data)
    # pythondata = JSONParser().parse(stream)
    serializer = TaskSerializer(instance=task, data=request.data)
    # serializer = TaskSerializer(instance = task,data= pythondata)

    if serializer.is_valid():
        serializer.save()
    # return Response(serializer.data)
    return JsonResponse(serializer.data ,safe= True )


@api_view(['DELETE'])
def taskDelete(request, pk):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Task.objects.get(id=id)
    stu.delete()
    return Response("Taks deleted successfully.")


