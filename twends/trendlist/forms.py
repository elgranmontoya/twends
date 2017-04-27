from django import forms

class TrendDate(forms.Form):
	year = forms.IntegerField(max_value=2017)
	month = forms.IntegerField(max_value=12)
	day = forms.IntegerField(max_value=31)