from django import forms

from .models import Document, Detail,Role
from dal import autocomplete
#from django.contrib.auth.models import Role



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', )


class DetailForm(forms.ModelForm):
	
   
    class Meta():
        model = Detail
        fields = ['Document_Name','Employee_Name', 'Address_of_Employee', 'Company_Name', 'Address_of_Company','Roles','Base_Salary', 'Date_of_Agreement', 'Start_Date', 'End_Date', 'Supervisor_Information', 'Bonus', 'Notice_Period', 'Other_Compensation', 'Non_Monetary_Benefits', 'Health_Insurance', '_401k', 'At_will', 'Stock', 'Vacation']
        # widgets = {'Document_Name': forms.HiddenInput()}
        #field_order=['Document_Name','Employee_Name', 'Address_of_Employee', 'Company_Name', 'Address_of_Company', 'Base_Salary', 'Date_of_Agreement', 'Start_Date', 'End_Date', 'Supervisor_Information', 'Bonus', 'Role','Notice_Period', 'Other_Compensation', 'Non_Monetary_Benefits', 'Health_Insurance', '_401k', 'At_will', 'Stock', 'Vacation']

   
        
    def __init__(self, *args, **kwargs):
        colors=[]
        entities=['Document_Name','Employee_Name', 'Address_of_Employee', 'Company_Name', 'Address_of_Company', 'Roles', 'Base_Salary', 'Date_of_Agreement', 'Start_Date', 'End_Date', 'Supervisor_Information', 'Bonus', 'Notice_Period', 'Other_Compensation', 'Non_Monetary_Benefits', 'Health_Insurance', '_401k', 'At_will', 'Stock', 'Vacation']
        # entities = ['Employee_Name']
        placeholder1 = kwargs.pop("dynamic_placeholder")
        #print(len(placeholder1))
        #print(placeholder1)
        try:            
            colors = kwargs.pop("doc_color")
        except:
            print("No colors passed")
        finally:
            print(len(colors))
            super(DetailForm, self).__init__(*args, **kwargs)
            for field in entities:

                
                #self.fields[field].widget.attrs['placeholder'] = placeholder1[entities.index(field)
                self.fields[field].initial = placeholder1[entities.index(field)]
                self.fields[field].blank = True
            if len(colors)==len(entities):
                for field in entities:    
                    self.fields[field].widget=forms.TextInput(attrs={'style':"background-color: {};".format(colors[entities.index(field)])})
            
        