from django import forms
from .models import Bidgely


class Bidgelyform(forms.ModelForm):
    class Meta:
        model=Bidgely
        fields='__all__'
        exclude=['user']

        labels={
            'name':'Name',
            'rollno':'RollNo',
            'age':'Age',
            'email':'Email',
            'department':'Department'
        }
class Uploadform(forms.Form):
    file_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form.control"}))
    file=forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))    

