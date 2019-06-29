from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
import time
from .forms import DocumentForm
from .models import Document, Detail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import DetailForm
import time
from Entity import Entities,convert_dataturks_to_spacy,Validate,check_validity,display_attributes
import spacy
from spacy import displacy
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

import os

nlp = spacy.load('sample_work_model_300_drop_0.05')
nlp2 = spacy.load("en_core_web_sm")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
import pandas
list_values=[]
files=[]
# Create your views here.
from openpyxl import load_workbook

wb =Workbook()

filepath=os.path.join(BASE_DIR,'UploadMulti/static/Excel_Files/Features.xlsx')
#sheet=wb.active
#sheet.append(('Employee Name', 'Address of Employee', 'Company Name', 'Address of Company', 'Role', 'Base Salary', 'Date of Agreement', 'Start Date', 'End Date', 'Supervisor Information', 'Bonus', 'Notice Period', 'Other Compensation', 'Non Monetary Benefits', 'Health Insurance', '401k', 'At will', 'Stock', 'Vacation'))
wb.save(filepath)

class BasicUploadView(View):
    def get(self, request):
        documents_list = Document.objects.all()
        return render(self.request, 'UploadMulti/basic_upload/index.html', {'documents': documents_list})
        # return redirect('UploadMulti:basic_upload', {'documents': documents_list})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            document = form.save()
            data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


# class ProgressBarUploadView(View):
#     def get(self, request):
#         documents_list = Document.objects.all()
#         return render(self.request, 'UploadMulti/progress_bar_upload/index.html', {'documents': documents_list})

#     def post(self, request):
#         #time.sleep(3)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
#         form = DocumentForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             document = form.save()
#             data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        documents_list = Document.objects.all()
        return render(self.request, 'UploadMulti/drag_and_drop_upload/index.html', {'documents': documents_list})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            document = form.save()
            data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for document in Document.objects.all():
        document.file.delete()
        document.delete()
        wb=Workbook()
        wb.save(filepath)
    return redirect(request.POST.get('next'))

def analysis(request, pk):
    doc_obj = get_object_or_404(Document, pk=pk)
    tup=[]
    form_ent=[]
    form_ent.append(doc_obj.file.name)
    with open('media/'+doc_obj.file.name, 'r', encoding='UTF-8') as f:
        data2=f.read()
    data2 = data2.lstrip()
    data2 = data2.rstrip()
    doc=nlp(data2)

    #obj = Entities()
    #mapping = obj.results(doc)
    #print(mapping.shape)
    #print(mapping)
    #df = obj.results_to_df(mapping)
    #entities=df.to_dict('dict')
    #if doc_obj.file.name not in files:
    #    files.append(doc_obj.file.name)
    #    for j in entities.values():
     #       tup.append(j[0])
      #  list_values.append(tuple(tup))


    # check here whether the file is already in db
    # if so take values from it and insert into form_ent
    # Changes to be made here.

    #for j in entities.values():
    #    j[0] = str(j[0]) 
    #    form_ent.append(j[0])
    #print(form_ent)
    #print(files)
    #print(entities)
    #---------------------------------------
    d=Detail.objects.filter(Document_Name=doc_obj.file.name).values()
    list_result = [entry for entry in d]
    field=Detail._meta.get_fields()
    
    tup=[]
    for f in field:
         tup.append(list_result[0][f.name])

    print(len(tup))
    d=display_attributes()
    color_scheme=d.color_table()
    color=[]
    color.append('#ffffff')
    color.extend(list(color_scheme.values()))
   # print(entities.keys())
    print(color)

    html = displacy.render(doc, style="ent", page=True,options=d.color_dict())
    DISPLACY_DIR=os.path.join(BASE_DIR,'/UploadMulti/static/Displacy_html')
    print(DISPLACY_DIR +'/doc{}.html')
    with open(BASE_DIR+'/UploadMulti/static' +'/doc{}.html'.format(pk), 'w') as myfile:
        myfile.write(html)


    # if this doesnt work add the file and proceed.SSS
    return render(request, 'UploadMulti/analysis.html', context={'File_Name':'doc{}.html'.format(pk),'color':color_scheme,'pk':pk,'form':DetailForm(dynamic_placeholder=tup,doc_color=color)})

    # if this doesnt work add the file and proceed.
    #


   # return render(request, 'analysis.html', {'doc_obj':doc_obj})


from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def csv(request):

    book = load_workbook(filepath)
    list_values=[]
    list_values.append(('Employee Name', 'Address of Employee', 'Company Name', 'Address of Company', 'Role', 'Base Salary', 'Date of Agreement', 'Start Date', 'End Date', 'Supervisor Information', 'Bonus', 'Notice Period', 'Other Compensation', 'Non Monetary Benefits', 'Health Insurance', '401k', 'At will', 'Stock', 'Vacation'))
    val=Detail.objects.all().values()
    for v in val:
        value_list= [entry for entry in v.values()]
        list_values.append(tuple(value_list))
    writer = pd.ExcelWriter(filepath, engine='openpyxl')
    writer.book = book
    writer.sheets = {ws.title: ws for ws in book.worksheets}

    df=pd.DataFrame(list(list_values))
    #print(df)
    for sheetname in writer.sheets:
        df.to_excel(writer,sheet_name=sheetname,  index = False,header= False)

    ws = book[sheetname]
    black_font = Font(bold=True)
    for cell in ws["1:1"]:
        cell.font = black_font

    writer.save()
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filepath)
            return response

    raise Http404
   
    #return redirect(request.POST.get('next'))


def process(request):
    documents = Document.objects.all()
    

    for document in documents: # we can optimize here 
        if Detail.objects.filter(Document_Name=document.file.name).exists()==False:
            tup=[]
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
            
            tup=tuple(tup)
            d=Detail(*tup)
            d.save()

    return render(request, 'UploadMulti/basic_upload/index.html', {'documents':documents})

def save_info(request):
    documents = Document.objects.all()
    if request.method == "POST":
        p_dict = {}
        p_dict.update( {request.POST.get('title') : request.POST.get('input')} )
        print(p_dict.items())
        return render(request, 'UploadMulti/basic_upload/index.html', {'documents':documents})
    else:
        return render(request, 'UploadMulti/basic_upload/index.html', {'documents':documents})

def form_post(request):

    if request.method == "POST":

        p = list(request.POST.values())
        instance=get_object_or_404(Detail,Document_Name=p[1])
        print(p)
        p = p[1:]
        
        
        #detail = Detail()
        # detail.Document_Name = name
        # detail.save()
        form = DetailForm(request.POST,dynamic_placeholder=p,instance=instance)
        # form.fields['Document_Name'] = name
        #print(form)
       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
          
        else:
            print("here")
            messages.error(request, 'The form is invalid.')
            print(form.errors)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    


########################################################################

from rest_framework import viewsets
from .serializers import DocumentSerializer, DetailSerializer

class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    


class DetailViewset(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
