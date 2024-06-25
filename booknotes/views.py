from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Notes
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET','POST'])
def getRoutes(req):
    
    routes=[
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {
                'title':"",
                'body': ""
                },
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {
                'title':"",
                'body': ""
                },
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        }, 
    ]
    
    return Response(routes)


@api_view(['GET'])
def getNotes(req):
    notes=Notes.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(req,currId):
    notes=Notes.objects.get(id=currId)
    # serialized one single object
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)