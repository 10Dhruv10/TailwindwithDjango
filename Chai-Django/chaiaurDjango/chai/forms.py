from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
  chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select Chai Variety")
  
#label is to tell user what this form field is about