from django import forms
from .models import *


class Tbl_User_Form(forms.ModelForm):
    class Meta:
        model=Tbl_user
        exclude=['u_password']
        fields=['u_name','u_email','u_phno','u_address','u_gst','u_panno','u_servicetaxno','u_documents']