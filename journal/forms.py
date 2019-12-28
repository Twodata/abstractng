from django import forms

from .models import AuthorProfile, Paper, Review, Department, MyMessage

# from django.contrib.auth.models import User

# django-ckeditor
# from django.contrib import admin
# from ckeditor.widgets import CKEditorWidget




class AuthorProfileForm(forms.ModelForm):    
     
    class Meta:
        model = AuthorProfile
        exclude = ['user', 'views']

#        fields = '__all__'


        
        
class PaperForm(forms.ModelForm):
    
    class Meta:
        model = Paper
        exclude = ['author', 'views', 'slug', 'added_by']




class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['text']
        
               
          
        
class DepartmentForm(forms.ModelForm):
    
    class Meta:
        model = Department
        fields = ['department']
        


class MyMessageForm(forms.ModelForm):
    
    class Meta:
        model = MyMessage
        exclude = ['sender', 'to', 'date_added', 'added_by']


class ContactForm(forms.Form):
    contact_name = forms.CharField(required = True)
    contact_email = forms.EmailField(required = True)
    content = forms.CharField(required =True, widget=forms.Textarea)
        
        
