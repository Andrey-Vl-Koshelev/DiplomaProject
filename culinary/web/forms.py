from django.forms import ModelForm
from .models import Blog
from django import forms


class WebForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'text']
        labels = {
            'name': 'Ваше имя:',
            'text': 'Текст отзыва:'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__field'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form__field'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
