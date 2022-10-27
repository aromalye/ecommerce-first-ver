from dataclasses import field
from django import forms
from .models import Coupons

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupons
        fields = ['code']