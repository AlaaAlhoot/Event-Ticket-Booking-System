from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['full_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ComplaintForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['full_name'].widget = forms.HiddenInput()
            self.fields['email'].widget = forms.HiddenInput()
