from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
import time
from .forms import DocumentForm
from .models import Document
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View

from django.http import HttpResponse


from .forms import AddressForm
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
list_values=[]
list_values.append(('Employee Name', 'Address of Employee', 'Company Name', 'Address of Company', 'Role', 'Base Salary', 'Date of Agreement', 'Start Date', 'End Date', 'Supervisor Information', 'Bonus', 'Notice Period', 'Other Compensation', 'Non Monetary Benefits', 'Health Insurance', '401k', 'At will', 'Stock', 'Vacation'))
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
    with open('media/'+doc_obj.file.name, 'r', encoding='UTF-8') as f:
        data2=f.read()
    data2 = data2.lstrip()
    data2 = data2.rstrip()
    doc=nlp(data2)

    obj = Entities()
    mapping = obj.results(doc)
    #print(mapping.shape)
    #print(mapping)
    df = obj.results_to_df(mapping)
    entities=df.to_dict('dict')
    if doc_obj.file.name not in files:
        files.append(doc_obj.file.name)
        for j in entities.values():
            tup.append(j[0])
        list_values.append(tuple(tup))

    for j in entities.values():
        form_ent.append(j[0])
    #print(files)
    #print(entities)
    d=display_attributes()
    color_scheme=d.color_table()
    
   # print(entities.keys())
   # print(color_scheme)

    html = displacy.render(doc, style="ent", page=True,options=d.color_dict())
    DISPLACY_DIR=os.path.join(BASE_DIR,'/UploadMulti/static/Displacy_html')
    print(DISPLACY_DIR +'/doc{}.html')
    with open(BASE_DIR+'/UploadMulti/static' +'/doc{}.html'.format(pk), 'w') as myfile:
        myfile.write(html)


    # if this doesnt work add the file and proceed.SSS
    return render(request, 'UploadMulti/analysis.html', context={'Entity':entities,'File_Name':'doc{}.html'.format(pk),'color':color_scheme,'pk':pk,'form':AddressForm(dynamic_placeholder=form_ent)})

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

    if request.method == 'POST':
<<<<<<< HEAD
        # this is the problem since we have already initialised 
        # and form already exist but the instance is again needs 
        # to be created in order to save the form.
=======

        # this is the problem since we have already initialised 
        # and form already exist but the instance is again needs 
        # to be created in order to save the form.

>>>>>>> 7fcf97e9f8e077f5d6832f606e344ecb67128cee
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("UploadMulti/basic_upload/index.html", RequestContext(request))