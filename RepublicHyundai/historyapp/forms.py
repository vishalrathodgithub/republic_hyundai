from django.forms import ModelForm
from .models import *

class RcHistoryForm(ModelForm):
    class Meta:
        model = RcHistory
        fields = "__all__"
        
