from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['title', 'slug']

		widgets={
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'})
		}

	def clean_title(self):
		new_title=self.cleaned_data['title'].lower()

		if Tag.objects.filter(title__iexact=new_title).count():
			raise ValidationError('Тег должен быть уникальным. А "{}" уже существует :('.format(new_title))
		return new_title

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'body', 'tags']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст поста'}),
			'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Выберите теги'})
		}