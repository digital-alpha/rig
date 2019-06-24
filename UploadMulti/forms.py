from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', )


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
	

	Employee_Name = forms.CharField(
        label='Employee Name',
        widget=forms.TextInput()
    )
	Address_of_Employee = forms.CharField(
        label='Address of Employee',
        widget=forms.TextInput()
    )

	Company_Name = forms.CharField(
        label='Company Name',
        widget=forms.TextInput()
    )

	Address_of_Company = forms.CharField(
        label='Address of Company',
        widget=forms.TextInput()
    )

	Role = forms.CharField(
        label='Role',
        widget=forms.TextInput()
    )

	Base_Salary = forms.CharField(
        label='Base Salary',
        widget=forms.TextInput()
    )

	Date_of_Agreement = forms.CharField(
        label='Date of Agreement',
        widget=forms.TextInput()
    )

	Start_Date = forms.CharField(
        label='Start Date',
        widget=forms.TextInput()
    )

	End_Date = forms.CharField(
        label='End Date',
        widget=forms.TextInput()
    )

	Supervisor_Information = forms.CharField(
        label='Supervisor Information',
        widget=forms.TextInput()
    )

	Bonus = forms.CharField(
        label='Bonus',
        widget=forms.TextInput()
    )

	Notice_Period = forms.CharField(
        label='Notice Period',
        widget=forms.TextInput()
    )

	Other_Compensation = forms.CharField(
        label='Other Compensation',
        widget=forms.TextInput()
    )

	Non_Monetary_Benefits = forms.CharField(
        label='Non Monetary Benefits',
        widget=forms.TextInput()
    )

	Health_Insurance = forms.CharField(
        label='Health Insurance',
        widget=forms.TextInput()
    )

	_401k = forms.CharField(
        label='401k',
        widget=forms.TextInput()
    )


	At_will = forms.CharField(
        label='At will',
        widget=forms.TextInput()
    )

	Stock = forms.CharField(
        label='Stock',
        widget=forms.TextInput()
    )

	Vacation = forms.CharField(
        label='Vacation',
        widget=forms.TextInput()
    )
    
	

	def __init__(self, *args, **kwargs):
		i=0
		entities=['Employee_Name', 'Address_of_Employee', 'Company_Name', 'Address_of_Company', 'Role', 'Base_Salary', 'Date_of_Agreement', 'Start_Date', 'End_Date', 'Supervisor_Information', 'Bonus', 'Notice_Period', 'Other_Compensation', 'Non_Monetary_Benefits', 'Health_Insurance', '_401k', 'At_will', 'Stock', 'Vacation']
		placeholder1 = kwargs.pop("dynamic_placeholder")
		super(AddressForm, self).__init__(*args, **kwargs)
		for field in entities:
			
			#self.fields[field].widget.attrs['placeholder'] = placeholder1[entities.index(field)
			self.fields[field].initial = placeholder1[entities.index(field)]
	
	