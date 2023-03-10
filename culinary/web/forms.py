from django.forms import ModelForm
from .models import Blog

class WebForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})