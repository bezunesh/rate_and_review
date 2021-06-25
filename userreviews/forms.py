from django.forms import ModelForm
from django.contrib.auth.models import User

def addCssFormControl(form):
    for field in form.fields:
       form.fields[field].widget.attrs.update({'class': 'form-control'})

class SignupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        addCssFormControl(self)
    class Meta:
        model = User
        fields = ['username', 'password','email']