from django import forms

from .models import User

class AnswerForm(forms.Form):
	YourAnswer=forms.CharField(required=False)

class UserForm(forms.ModelForm):
	class Meta:
		model=User 
		fields=['name','username']