## Proyecto Web XVII

Building a form in Django

### The Form class

forms.pY
_____________________________________________
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
