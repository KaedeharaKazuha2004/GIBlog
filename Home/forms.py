from django import forms
from .models import Post, Category, Comment
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Which topic do you want to discuss?'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'admin', 'value':'' ,'type':'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Which topic do you want to discuss?'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Body': forms.Textarea(attrs={'class': 'form-control'}),
        }