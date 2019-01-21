from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['title', 'slug']

		widgets={
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'}),

		}
	def clean_slug(self):
		new_slug=self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Слаг не может быть "create"! Мы его первым заняли :)')
		if Tag.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Слаг должен быть уникальным. А "{}" уже существует :('.format(new_slug))
		return new_slug