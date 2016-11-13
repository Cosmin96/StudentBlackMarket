from django import forms
 
from mainapp.models import UploadFile
 
 
class UploadFileForm(forms.ModelForm):
     
	class Meta:
		model = UploadFile
		fields = ['file']