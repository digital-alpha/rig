from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer, DetailSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
import time
from UploadMulti.forms import DocumentForm
from UploadMulti.models import Document, Detail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from UploadMulti.forms import DetailForm
import time
from Source.Entity import Entities,display_attributes
import spacy
from spacy import displacy
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

import requests

from django.template.defaulttags import register
from rest_framework.permissions import IsAuthenticated


import os
import pandas


nlp = spacy.load('sample_work_model_300_drop_0.05')
nlp2 = spacy.load("en_core_web_sm")

class DocumentViewset(viewsets.ModelViewSet):
   
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


from django.forms.models import model_to_dict
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def processAPI(request):
   
    documents = Document.objects.all()
    for document in documents:
        if Detail.objects.filter(doc_id=document.id).exists()==False:
            tup=[]
            try:
                id=Detail.objects.latest('id')
                id=model_to_dict(id)['id']
            except:
                id=0

            tup.append(int(id) + 1)
            tup.append(document.file.name)
            with open('media/'+document.file.name, 'r', encoding='UTF-8') as f:
                data2=f.read()
            data2 = data2.lstrip()
            data2 = data2.rstrip()
            doc=nlp(data2)

            obj = Entities()
            mapping = obj.results(doc)
            df = obj.results_to_df(mapping)
            entities=df.to_dict('dict')
            for j in entities.values():
                tup.append(j[0])

            tup.append(document.id)
            print(tup)
            tup=tuple(tup)
            d=Detail(*tup)
            d.save()

            print("IN api view")
    return Response(status=200)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def processApiSingle(request, pk):
    document = get_object_or_404(Document, id=pk)
    tup=[]
    try:
        id=Detail.objects.latest('id')
        id=model_to_dict(id)['id']
    except:
        id=0

    tup.append(int(id) + 1)
    tup.append(document.file.name)
    with open('media/'+document.file.name, 'r', encoding='UTF-8') as f:
        data2=f.read()
    data2 = data2.lstrip()
    data2 = data2.rstrip()
    doc=nlp(data2)

    obj = Entities()
    mapping = obj.results(doc)
    df = obj.results_to_df(mapping)
    entities=df.to_dict('dict')
    for j in entities.values():
        tup.append(j[0])

    tup.append(document.id)
    print(tup)
    tup=tuple(tup)
    d=Detail(*tup)
    d.save()
    print("In single api view")
    return Response(status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def clearAPI(request):

    print(request.method)
    for document in Document.objects.all():
        document.file.delete()
        document.delete()
        wb=Workbook()
        wb.save(filepath)
    for detail in Detail.objects.all():
        detail.delete()
    return Response(status=200)


@api_view()
@permission_classes([IsAuthenticated])
def infoAPI(request,pk):
    
    if request.method == "GET":
        try:
            info=Detail.objects.filter(doc_id=pk)

        except Detail.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DetailSerializer(info, many=True)
        return Response(serializer.data)
    if request.method == "DELETE":
        try:
            info=Detail.objects.filter(doc_id=pk)

        except Detail.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        info.delete()

        return Response({"message": "details deleted"}, status=status.HTTP_204_NO_CONTENT)





class DetailViewset(viewsets.ModelViewSet):
 
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

    permission_classes = [IsAuthenticated]

