from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'text'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'cols': 40})
        }        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }